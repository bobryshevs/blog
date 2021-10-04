from models import Post
from structure import post_repository
from tests.factories.post_factory import PostFactory


class TestPostRepository:
    def setup(self):
        self.repository = post_repository
        self.collection = post_repository.collection
        self.factory = PostFactory()

    def teardown(self):
        post_repository.collection.delete_many({})

    def test_get_page_no_posts(self):
        self.collection.delete_many({})
        page = 1
        page_size = 2

        pages = self.repository.get_page(page, page_size)

        assert pages == []

    def test_get_page_first(self):
        NUMBER_OF_DOCUMENTS = 10
        PAGE = 1
        PAGE_SIZE = 3
        data: list[dict] = self.factory.get_many_documents(NUMBER_OF_DOCUMENTS)
        self.collection.insert_many(data)

        page: list[Post] = self.repository.get_page(
            page=PAGE,
            page_size=PAGE_SIZE
        )
        assert len(page) == PAGE_SIZE

        for i in range(len(page)):
            data_post: dict = data[-(i + 1)]  # from the tail
            page_post: Post = page[i]

            assert data_post["title"] == page_post.title
            assert data_post["content"] == page_post.content
            assert data_post["author_id"] == page_post.author_id
            assert data_post["comment_ids"] == page_post.comment_ids

    def test_get_page_middle(self):
        NUMBER_OF_DOCUMENTS = 10
        PAGE = 3
        PAGE_SIZE = 3

        data: list[dict] = self.factory.get_many_documents(NUMBER_OF_DOCUMENTS)
        self.collection.insert_many(data)

        page: list[Post] = self.repository.get_page(
            page=PAGE,
            page_size=PAGE_SIZE
        )

        assert len(page) == PAGE_SIZE

        data_post_1 = data[3]  # NUMBER_OF_DOCUMENTS-(PAGE-1)*PAGE_SIZE-NUMPOST
        data_post_2 = data[2]
        data_post_3 = data[1]

        assert page[0].title == data_post_1["title"]
        assert page[0].content == data_post_1["content"]
        assert page[0].author_id == data_post_1["author_id"]
        assert page[0].comment_ids == data_post_1["comment_ids"]

        assert page[1].title == data_post_2["title"]
        assert page[1].content == data_post_2["content"]
        assert page[1].author_id == data_post_2["author_id"]
        assert page[1].comment_ids == data_post_2["comment_ids"]

        assert page[2].title == data_post_3["title"]
        assert page[2].content == data_post_3["content"]
        assert page[2].author_id == data_post_3["author_id"]
        assert page[2].comment_ids == data_post_3["comment_ids"]

    def test_get_page_out_of_range(self):
        NUMBER_OF_DOCUMENTS = 10
        PAGE = 800
        PAGE_SIZE = 1200

        data: list[dict] = self.factory.get_many_documents(NUMBER_OF_DOCUMENTS)
        self.collection.insert_many(data)

        page: list[Post] = self.repository.get_page(
            page=PAGE,
            page_size=PAGE_SIZE
        )

        assert len(page) == 0
