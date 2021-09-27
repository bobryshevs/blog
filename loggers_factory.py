from loggers import BaseLogger


class LoggersFactory:

    def __init__(self) -> None:
        self.base = BaseLogger()
        self.special_classes = ["BusyClass"]

    def get(self):
        return self.base

    def get_logger(self, obj_link):
        obj_name = obj_link.__class__.__name__.lower()

        if "handler" in obj_name:
            return self.base  # Todo: define special logger

        if "repository" in obj_name:
            return self.base  # Todo: define special logger

        if obj_name in self.special_classes:
            return self.base  # Todo: define special logger


loggers_factory = LoggersFactory()
