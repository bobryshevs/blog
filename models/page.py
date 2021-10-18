from .model import Model


class Page(Model):
    def __init__(self) -> None:
        self.items: list[dict] = []
        self.page: int = None
        self.page_size: int = None
        self.page_count: int = None
