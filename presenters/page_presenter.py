from models import Page
from .base_presenter import BasePresenter


class PagePresenter(BasePresenter):
    def __init__(self, item_presetner) -> None:
        self.item_presetner: BasePresenter = item_presetner

    def present(self, page: Page) -> dict:
        page.items = [self.item_presetner.present(item) for item in page.items]
        return {
            "items": page.items,
            "page": page.page,
            "page_size": page.page_size,
            "page_count": page.page_count
        }
