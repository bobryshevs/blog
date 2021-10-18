from abc import ABC, abstractmethod
from models import Model


class BasePresenter(ABC):
    @abstractmethod
    def present(self, model: Model): ...
