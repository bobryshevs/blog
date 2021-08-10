from data_models.post import PostAuthorInterface

ADMIN = 0
USER = 1


class User(PostAuthorInterface):
    def __init__(self, name: str, user_role: int = USER):
        self.__user_role = user_role
        self.__name = name

    @property
    def name(self):
        return self.__name

    @property
    def user_role(self) -> int:
        return self.__user_role
