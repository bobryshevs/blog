from bson import ObjectId
from models import Post
from exceptions import (
    IncorrectPageValue,
    IncorrectPageSizeValue,
    IncorrectPostIdType,
    IncorrectPageSizeType,
    IncorrectPageType
)


class PostValidator:

    def check_get_page_args(self, page: int, page_size: int) -> bool:
        if not isinstance(page, int):
            raise IncorrectPageType

        if not self._is_non_negative(page):
            raise IncorrectPageValue

        if not isinstance(page_size, int):
            raise IncorrectPageSizeType

        if not self._is_non_negative(page):
            raise IncorrectPageSizeValue

        return True

    def check_get_by_id_args(self, post_id) -> bool:
        if not isinstance(post_id, ObjectId):
            raise IncorrectPostIdType
        return True

    def check_delete_args(self, post_id) -> bool:
        if not isinstance(post_id, ObjectId):
            raise IncorrectPostIdType
        return True

    def check_create_args(self, post) -> bool:
        if not isinstance(post, Post):
            raise

    def _is_non_negative(self, number) -> bool:
        return number > 0


if __name__ == "__main__":
    pv = PostValidator()
    pv.check_get_page_args(-1, -2)
