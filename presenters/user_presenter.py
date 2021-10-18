from models import User
from .base_presenter import BasePresenter


class UserPresenter(BasePresenter):
    def present(self, user: User) -> dict:
        return {
            "id": str(user.id),
            "first_name": user.first_name,
            "last_name": user.last_name,
        }
