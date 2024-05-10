from jsii import implements
from aws_cdk import (
    ILocalBundling,
    BundlingOptions,
    Stack,
    DockerImage,
    Duration,
    aws_iam,
    CfnOutput,
)
from aws_cdk import aws_lambda as lambda_
from logging import getLogger
import sys
import os
import subprocess
from factories.base import BaseFactory


@implements(ILocalBundling)
class PythonLambdaBundler:
    """
    Utility class to bundle a Lambda function locally
    """

    def __init__(self, path: str, lambda_layer: bool = False) -> None:
        self.path = path
        self.lambda_layer = lambda_layer
        self.logger = getLogger(__name__)

    def try_bundle(self, output_dir: str, options: BundlingOptions) -> bool:
        if sys.platform != "linux":
            self.logger.error("Local bundling only supported on Linux")
            return False
        if sys.version_info < (3, 11):
            self.logger.error("Local bundling requires Python 3.11+")
            return False
        layer_path = (
            f"python/lib/python3.{sys.version_info.minor}/site-packages"
            if self.lambda_layer
            else ""
        )
        self.logger.info(f"Bundle {self.path} to {output_dir}")
        try:
            requirements = f"{self.path}/requirements.txt"
            requirements_cmd = (
                f"pip install -r {requirements} -t {output_dir}/{layer_path}"
            )
            cp_command = f"cp -r {self.path}/* {output_dir}/{layer_path}"
            if os.path.exists(requirements):
                subprocess.run(requirements_cmd, shell=True, check=True)
            subprocess.run(cp_command, shell=True, check=True)
            self.logger.info(f"Lambda bundled successfully: {output_dir}")
            return True
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Error bundling lambda: {e}")
            return False


class PythonLambdaFactory(BaseFactory):
    def __init__(self, stack: Stack, stage: str, prefix: str, env: dict = {}):
        super().__init__(stack, stage, prefix)
        self.env = {"STAGE": stage, **env}
        self.build_image = DockerImage.from_registry(
            "public.ecr.aws/sam/build-python3.11:latest-x86_64"
        )
        self.default_policy = aws_iam.PolicyStatement(
            actions=["secretsmanager:GetSecretValue", "sqs:SendMessage"],
        )

    def bundle(self, path: str) -> BundlingOptions:
        """
        Bundle a Lambda function, using a Docker image if necessary
        """
        return BundlingOptions(
            image=self.build_image,
            local=PythonLambdaBundler(path),
            command=[
                "bash",
                "-c",
                "if [ -f requirements.txt ]; then pip install -r requirements.txt -t /asset-output; fi && cp -au . /asset-output",
            ],
        )

    def new_function(
        self,
        name: str,
        folder: str,
        index: str,
        handler: str,
        timeout: int = 900,
        memory_size: int = 256,
        layers: list = [],
        environment: dict = {},
        policies: list = [],
        use_default_policy: bool = True,
    ):
        """
        Create a new Lambda function
        :param name: The name of the function, the prefix and stage will be added
        :param folder: The path to the Lambda function code
        :param index: The name of the file containing the Lambda handler
        :param handler: The name of the Lambda handler function
        :param timeout: The function timeout in seconds (default 900)
        :param memory_size: The function memory size in MB (default 256)
        :param layers: A list of Lambda layers to attach to the function
        :param environment: A dictionary of environment variables
        :param policies: A list of IAM policies to attach to the function
        :param use_default_policy: Whether to attach the default policy to the function, this policie allows to get values from secret manager and send message to sqs (default True)
        """

        if use_default_policy:
            policies.append(self.default_policy)
        func = lambda_.Function(
            self.stack,
            self.name(name),
            function_name=self.name(name),
            runtime=lambda_.Runtime.PYTHON_3_11,
            handler=f"{index}.{handler}",
            code=lambda_.Code.from_asset(folder, bundling=self.bundle(folder)),
            environment={**self.env, **environment},
            timeout=Duration.seconds(timeout),
            memory_size=memory_size,
            layers=layers,
            initial_policy=policies,
        )
        CfnOutput(
            self.stack,
            f"{name} deployed to:",
            value=func.function_name,
        )
        return func

    def new_layer(self, name: str, folder: str):
        """
        Create a new Lambda layer
        :param name: The name of the layer, the prefix and stage will be added
        :param folder: The path to the layer code
        """
        name = self.name(name)
        layer = lambda_.LayerVersion(
            self.stack,
            name,
            layer_version_name=name,
            code=lambda_.Code.from_asset(folder, bundling=self.bundle(folder)),
            compatible_runtimes=[lambda_.Runtime.PYTHON_3_11],
        )
        return layer
