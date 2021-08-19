from .base_validator import BaseValidator


class NonZeroStrValidator(BaseValidator):

    def valid(self, args: dict) -> bool:
        value = args.get(self.key)
        return len(value) > 0
