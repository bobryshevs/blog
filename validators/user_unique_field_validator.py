from repositories import UserRepository


class UserUniqueFieldValidator:
    def __init__(self, key: str, repository: UserRepository) -> None:
        self.key: str = key
        self.repository: UserRepository = repository

    def valid(self, args: dict) -> bool:
        user = self.repository.get(name=self.key, value=args["key"])
        if user is not None:
            return False
        return True

    def error(self) -> str:
        return f"Error in {self.key}. A user with such email already exists."
