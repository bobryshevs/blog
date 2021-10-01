from repositories import MongoRepository


class UniqueFieldValidator:
    def __init__(self, key: str, repository: MongoRepository) -> None:
        self.key: str = key
        self.repository: MongoRepository = repository

    def valid(self, args: dict) -> bool:
        user = self.repository.get_one_by_field(self.key, args[self.key])
        return user is None

    def error(self) -> str:
        return f"Error in {self.key}. A user with such email already exists."
