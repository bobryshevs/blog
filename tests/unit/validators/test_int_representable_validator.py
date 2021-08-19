from validators import IntRepresentableValidator


class TestIntRepresentableValidator:

    def test_valid_value_invalid(self):
        key = "page"
        args = {key: "1.3"}
        validator = IntRepresentableValidator(key=key)

        assert validator.valid(args) is False

    def test_valid_value_valid(self):
        key = "page"
        args = {key: "123"}
        validator = IntRepresentableValidator(key=key)

        assert validator.valid(args) is True
