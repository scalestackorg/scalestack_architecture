from aws_cdk import aws_apigateway as apigw

from aws_cdk import CfnOutput, Stack, aws_sqs, aws_iam
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

    def new_sqs_integration(
        self,
        endpoint: str,
        sqs: aws_sqs.Queue,
        api: apigw.RestApi,
        method: str = "POST",
    ):
        role = aws_iam.Role(
            self.stack,
            self.name("APIGatewayRole"),
            assumed_by=aws_iam.ServicePrincipal("apigateway.amazonaws.com"),
            role_name=self.name("APIGatewayRole"),
        )
        sqs.grant_send_messages(role)
        integration = apigw.AwsIntegration(
            service="sqs",
            path=sqs.queue_name,
            options=apigw.IntegrationOptions(
                integration_responses=[{"statusCode": "200"}],
                credentials_role=role,
                request_parameters={
                    "integration.request.header.Content-Type": "'application/x-www-form-urlencoded'"
                },
                request_templates={
                    "application/json": 'Action=SendMessage&MessageBody={"data":$input.body}'
                },
                passthrough_behavior=apigw.PassthroughBehavior.WHEN_NO_MATCH,
            ),
        )
        api.root.add_resource(path_part=endpoint).add_method(
            method,
            integration,
            method_responses=[{"statusCode": "200"}],
            authorization_type=apigw.AuthorizationType.NONE,
        )
        CfnOutput(
            self.scope,
            "ApiEndpointSQS",
            value=f"{method}: {api.rest_api_id}.execute-api.{self.stack.region}.amazonaws.com/{self.stage}/{endpoint}",
        )
