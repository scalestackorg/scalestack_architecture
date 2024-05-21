from aws_cdk import Stack
from constructs import Construct


class BaseFactory:
    def __init__(self, stack: Stack, stage: str, prefix: str, scope: Construct):
        self.stack = stack
        self.stage = stage
        self.prefix = prefix
        self.scope = scope

    def name(self, name: str):
        if self.prefix:
            return f"{self.prefix}_{self.stage}_{name}"
        return f"{self.stage}_{name}"
