from datetime import datetime


class Comment:
    def __init__(self, text: str, user_id: int, date_of_creation: datetime, post_id: int):
        self.__text = text
        self.__user_id = user_id
        self.__date_of_creation = date_of_creation
        self.__post_id = post_id

    @property
    def text(self) -> str:
        return self.__text

    @property
    def user_id(self) -> int:
        return self.__user_id

    @property
    def date_of_creation(self) -> datetime:
        return self.__date_of_creation

    @property
    def post_id(self):
        return self.__post_id
