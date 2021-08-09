from datetime import datetime


class PostAuthorInterface:

    def user_role(self) -> int:
        raise NotImplementedError


class Post:
    def __init__(self, text: str, img_link: str, author: PostAuthorInterface, create_date: datetime = datetime.now()):
        self.__text = text
        self.__img_link = img_link
        self.__author = author
        self.__create_date = create_date

    @property
    def text(self) -> str:
        return self.__text

    @property
    def img_link(self) -> str:
        return self.__img_link

    @property
    def author(self) -> PostAuthorInterface:
        return self.__author

    @property
    def create_date(self) -> datetime:
        return self.__create_date

    def to_json(self):
        return str(self.__dict__)


if __name__ == '__main__':
    pass
