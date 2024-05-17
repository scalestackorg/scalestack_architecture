from aws_cdk import aws_apigateway as apigw
from aws_cdk import CfnOutput, Stack
from aws_cdk.aws_lambda import Function
from constructs import Construct
from .base import BaseFactory


class ApiGatewayFactory(BaseFactory):
    def __init__(self, stack: Stack, scope: Construct, stage: str, prefix: str = ""):
        super().__init__(stack, stage, prefix, scope)

    def new_rest_api(self, api_name: str):
        api = apigw.RestApi(
            self.stack,
            self.name(api_name),
            rest_api_name=self.name(api_name),
            deploy_options=apigw.StageOptions(stage_name=self.stage),
        )
        CfnOutput(
            self.scope,
            f"{self.name(api_name)}-URL",
            value=api.url,
        )
        return api

    @staticmethod
    def new_rest_lambda_integration(
        api: apigw.RestApi, lambda_function: Function, path: str, method: str = "GET"
    ):
        if path:
            resource = api.root.add_resource(path)
        else:
            resource = api.root
        return resource.add_method(
            method,
            apigw.LambdaIntegration(lambda_function),
        )
