class BaseFactory:
    def __init__(self, stack, stage, prefix):
        self.stack = stack
        self.stage = stage
        self.prefix = prefix

    def name(self, name: str):
        if self.prefix:
            return f"{self.prefix}_{self.stage}_{name}"
        return f"{self.stage}_{name}"
