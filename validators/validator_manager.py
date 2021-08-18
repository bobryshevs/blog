from validators import (
    ExistenceValidator,
    TypeValidator,
    ContentValidator
)


class ValidatorManager:
    def __init__(self) -> None:
        self.key_map = {}

    def create_validator(self, key: str,
                         value_type: type,
                         validator_link: type):

        if not (key, value_type) in self.key_map:
            if not isinstance(validator_link, ExistenceValidator):
                raise ValueError(
                    f"key '{key}' doesn't have ExistenceValidator")

            key_map_item = {
                'existence_validator': False,
                'type_validator': False,
                'content_validator': False
            }
