from models import User


class UserPresenter:
    def to_json(self, user: User) -> dict:
        # Не отдаю фронту почту, так как может повлечь проблемы приватности
        return {
            "id": str(user.id),
            "first_name": user.first_name,
            "last_name": user.last_name,
        }
