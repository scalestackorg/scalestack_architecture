from aws_cdk.aws_secretsmanager import Secret
from aws_cdk import Stack
from datadog_cdk_constructs_v2 import Datadog


class DatadogFactory:
    """
    Factory class for creating Datadog constructs
    """

    def __init__(
        self,
        stack: Stack,
        stage: str,
        api_secret_name: str = "infra/datadog/key",
        api_secret_key: str = "datadog-api-key",
        extension_layer_version: int = 56,
        site="us5.datadoghq.com",
        dd_log_level="ERROR",
    ):
        """
        Initialize the DatadogFactory
        :param stack: The stack to create the construct in
        :param stage: The stage of the stack (e.g. dev, prod)
        :param api_secret_name: The name of the secret in Secrets Manager
        :param api_secret_key: The key of the secret in Secrets Manager
        :param extension_layer_version: The version of the Datadog Lambda extension layer (default 56)
        :param site: The Datadog site to send data to (default us5.datadoghq.com)
        :param dd_log_level: The log level of the logs generated by the Datadog extension (default ERROR)
        """
        self.stack = stack
        self.name = stack.stack_name + "-datadog"
        self.stack = stack
        self.stage = stage
        self.secret = Secret.from_secret_name_v2(
            self.stack, secret_name=api_secret_name, id=api_secret_key
        )
        self.extension_layer_version = extension_layer_version
        self.site = site
        self.dd_log_level = dd_log_level

    def python_monitoring(self, layer_version: int = 92):
        """
        Create a Datadog construct for Python monitoring
        :param layer_version: The version of the Python Lambda layer to use
        :return: Datadog
        """
        return Datadog(
            self.stack,
            self.name,
            env=self.stage,
            site=self.site,
            extension_layer_version=self.extension_layer_version,
            python_layer_version=layer_version,
            api_key_secret=self.secret,
            log_level=self.dd_log_level,
            service=self.stack.stack_name,
            capture_lambda_payload=True,
            flush_metrics_to_logs=True,
            enable_profiling=True,
            enable_merge_xray_traces=True,
            enable_cold_start_tracing=True,
            decode_authorizer_context=True,
        )
