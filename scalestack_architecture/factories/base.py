from aws_cdk import Stack
from constructs import Construct


class BaseFactory:
    def __init__(self, stack: Stack, stage: str, prefix: str, scope: Construct = None):
        self.stack = stack
        self.stage = stage
        self.prefix = prefix
        self.scope = (
            scope or stack
        )  # if the scope (parent stack) is not provided, use the stack itself

    def name(self, name: str):
        if self.prefix:
            return f"{self.prefix}_{self.stage}_{name}"
        return f"{self.stage}_{name}"
