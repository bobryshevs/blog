from data_models.user import User


class UserTranslator:

    def to_mongo(self, user: User) -> dict:
        return {
            'name': user.name,
            'role': user.user_role
        }

    def from_dict(self, usr_dict):
        return User(name=usr_dict['name'])

    def from_mongo(self) -> User:
        pass
