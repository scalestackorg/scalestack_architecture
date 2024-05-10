class BaseFactory:
    def __init__(self, stack, stage, prefix):
        self.stack = stack
        self.stage = stage
        self.prefix = prefix

    def name(self, name: str):
        if self.prefix:
            return f"{self.prefix}-{name}-{self.stage}"
        return f"{name}-{self.stage}"
