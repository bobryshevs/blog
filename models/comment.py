from datetime import datetime


class Comment:
    def __init__(self, text: str, author: str, post_id: str):
        self.text: str = text
        self.author: str = author
        self.post_id: str = post_id
        self.date_of_creation: str = datetime.now().isoformat()
