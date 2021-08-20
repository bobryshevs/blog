

class IntRepresentableValidator():
    def __init__(self, key: str) -> None:
        self.key = key

    def valid(self, args: dict) -> bool:
        try:
            # argument must be a string:
            #           // int("1.3") -> Exception
            #           // int(1.3)   ->  1
            # check it in type_validators
            int(args.get(self.key))
            return True
        except (TypeError, ValueError):
            return False
