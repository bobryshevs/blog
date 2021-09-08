from .base_logger import BaseLogger


class LoggersFactory:
    def __init__(self) -> None:
        base = BaseLogger()
        self.class_to_logger = {
            "<class 'repositories.mongo_repository.MongoRepository'>": base,
            "<class 'repositories.post_repository.PostRepository'>": base
        }

    def get_logger(self, object_link):
        return self.class_to_logger[str(type(object_link))]
