from models import TokenPair


class TockenPairPresenter:
    def to_json(self, model: TokenPair) -> dict:
        return {
            "access": model.access,
            "refresh": model.refresh
        }
