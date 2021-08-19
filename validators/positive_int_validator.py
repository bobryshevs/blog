from .base_validator import BaseValidator


class PositiveIntValidator(BaseValidator):

    def valid(self, args: dict) -> bool:
        return int(args.get(self.key)) > 0
