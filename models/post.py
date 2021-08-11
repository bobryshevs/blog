from datetime import datetime


class Post:
    def __init__(self, text: str, author: str, date_of_creation: str):
        self.m_id = None
        self.text: str = text
        self.author: str = author
        self.date_of_creation: str = date_of_creation
        # Todo: проверка корректности даты

    




