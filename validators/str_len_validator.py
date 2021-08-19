from .base_validator import BaseValidator


class StrLenValidator(BaseValidator):

    def valid(self, args: dict, _min=1, _max=None) -> bool:
        '''[min, max] --> Including interval boundaries'''

        if not self._check_args_for_valid(_min, _max):
            raise ValueError(
                f"_min and _max must be positive integers "
                f"but {_min =} and {max = } was given"
            )

        if _max is not None:
            return _min <= len(args.get(self.key)) <= _max

        return _min <= len(args.get(self.key))

    def _check_args_for_valid(self, _min: int, _max: int) -> bool:
        if _max is not None:
            return not (_min < 0 or _max < 0)
        return not (_min < 0)
