from models import TokenPair
from .base_presenter import BasePresenter


class TockenPairPresenter(BasePresenter):
    def present(self, model: TokenPair) -> dict:
        return {
            "access": model.access,
            "refresh": model.refresh
        }
