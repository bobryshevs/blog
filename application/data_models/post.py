from datetime import datetime


class PostAuthorInterface:

    def user_role(self) -> int:
        raise NotImplementedError


class Post:
    def __init__(self, text: str, author: PostAuthorInterface, date_of_creation: datetime = datetime.now()):
        self.__text = text
        self.__author = author
        self.__date_of_creation = date_of_creation

    @property
    def text(self) -> str:
        return self.__text

    @property
    def author(self) -> PostAuthorInterface:
        return self.__author

    @property
    def create_date(self) -> datetime:
        return self.__date_of_creation

    def to_json(self):
        return str(self.__dict__)


if __name__ == '__main__':
    pass
