from bson import ObjectId
from presenters import UserPresenter
from models import User


class TestUserPresenter:
    def test_to_json(self):
        presenter = UserPresenter()
        user = User()
        user.id = ObjectId()
        user.first_name = "first_name"
        user.last_name = "last_name"

        result = presenter.to_json(user)

        assert isinstance(result, dict)
        assert str(user.id) == result["id"]
        assert user.first_name == result["first_name"]
        assert user.last_name == result["last_name"]
        assert len(result.keys()) == 3
