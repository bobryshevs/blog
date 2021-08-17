class Validator:

    @staticmethod
    def to_int(arg: any):
        try:
            return int(arg)
        except ValueError:
            return None

    @staticmethod
    def validate_non_negative_int(value: any) -> None:
        value = Validator.to_int(value)
        if value is None:
            raise TypeError()

        if value < 1:
            raise ValueError()
