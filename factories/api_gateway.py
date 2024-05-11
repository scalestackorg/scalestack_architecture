from aws_cdk import aws_apigateway as apigw
from aws_cdk import CfnOutput, Stack
from aws_cdk.aws_lambda import Function
from factories.base import BaseFactory


class ApiGatewayFactory(BaseFactory):
    def __init__(self, stack: Stack, stage: str, prefix: str):
        super().__init__(stack, stage, prefix)

    def new_rest_api(self, api_name: str):
        api = apigw.RestApi(
            self.stack,
            self.name(api_name),
            rest_api_name=self.name(api_name),
            deploy_options=apigw.StageOptions(stage_name=self.stage),
        )
        CfnOutput(
            self.stack,
            f"{self.name(api_name)} URL",
            value=api.url,
        )
        return api

    @staticmethod
    def new_rest_lambda_integration(
        api: apigw.RestApi, lambda_function: Function, path: str, method: str = "GET"
    ):
        return api.root.add_resource(path).add_method(
            method,
            apigw.LambdaIntegration(lambda_function),
        )
