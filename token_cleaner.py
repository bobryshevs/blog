from math import ceil
from repositories import UserRepository
from models import User
from validators import JWTValidator
from exceptions import BadRequest


class TokenCleaner:
    def __init__(self,
                 user_repository: UserRepository,
                 token_validator: JWTValidator) -> None:
        self.repository: UserRepository = user_repository
        self.token_validator = token_validator

    def clean(self, page_size: int = 100):
        number_page: int = self.calc_number_page(page_size)
        for page_number in range(number_page):
            user_token_page: list[User] = self.repository.get_user_token(
                page=page_number,
                page_size=page_size
            )
            self.handle_users(user_token_page)

    def handle_users(self, user_page: list[User]):
        for user in user_page:
            self.remove_bad_tokens(user)

    def remove_bad_tokens(self, user: User):
        bad_token_indexes = []
        for index, token_pair in enumerate(user.tokens):
            try:
                self.token_validator.valid({"token": token_pair.refresh})
            except BadRequest:
                bad_token_indexes.append(index)

        for correction, bad_index in enumerate(bad_token_indexes):
            del user.tokens[bad_index - correction]

    def calc_number_page(self, page_size: int) -> int:
        users_count = self.repository.documents_count()
        number_page = ceil(users_count / page_size)
        return number_page if number_page != 0 else 1
