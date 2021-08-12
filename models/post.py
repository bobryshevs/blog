from datetime import datetime


class Post:
    def __init__(self, text: str, author: str, date_of_creation: str, m_id=None):
        self.m_id = m_id
        self.text: str = text
        self.author: str = author
        self.date_of_creation: str = date_of_creation
        # Todo: проверка корректности даты


    def is_equal(self, other) -> bool:
        return \
            self.m_id == other.m_id and \
            self.text == other.text and \
            self.author == other.author and \
            self.date_of_creation == other.date_of_creation   

    




