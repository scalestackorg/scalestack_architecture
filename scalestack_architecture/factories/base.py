class BaseFactory:
    def __init__(self, stack, stage, prefix, scope):
        self.stack = stack
        self.stage = stage
        self.prefix = prefix
        self.scope = scope

    def name(self, name: str):
        if self.prefix:
            return f"{self.prefix}_{self.stage}_{name}"
        return f"{self.stage}_{name}"
