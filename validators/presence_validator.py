from .base_validator import BaseValidator


class PresenceValidator(BaseValidator):

    def valid(self, args: dict) -> bool:
        if not isinstance(args, dict):
            return False

        if self.key not in args:
            return False

        if args.get(self.key) is None:
            return False

        return True
