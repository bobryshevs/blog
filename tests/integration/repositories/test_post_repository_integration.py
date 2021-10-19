from models import Post, Page
from structure import post_repository
from tests.factories.post_factory import PostFactory


class TestPostRepositoryIntegration:
    def setup(self):
        self.repository = post_repository
        self.collection = post_repository.collection
        self.factory = PostFactory()

    def teardown(self):
        post_repository.collection.delete_many({})

    def test_get_page_no_posts(self):
        self.collection.delete_many({})
        page_value = 1
        page_size_value = 2
        default_page_count = 1

        page = self.repository.get_page(page_value, page_size_value)

        assert isinstance(page, Page)
        assert page.items == []
        assert page.page == page_value
        assert page.page_size == page_size_value
        assert page.page_count == default_page_count

    def test_get_page_first(self):
        NUMBER_OF_DOCUMENTS = 10
        page_value = 1
        page_size_value = 3
        page_count_value = 4  # NUMBER_OF_DOCUMENTS / PAGE_SIZE (/|\)

        data: list[dict] = self.factory.get_many_documents(NUMBER_OF_DOCUMENTS)
        self.collection.insert_many(data)

        page: dict = self.repository.get_page(
            page=page_value,
            page_size=page_size_value
        )

        assert len(page.items) == page_size_value
        assert page.page == page_value
        assert page.page_size == page_size_value
        assert page.page_count == page_count_value

        data = data[::-1]

        for i in range(len(page.items)):
            data_post: dict = data[i]
            page_post: Post = page.items[i]

            assert data_post["title"] == page_post.title
            assert data_post["content"] == page_post.content
            assert data_post["author_id"] == page_post.author_id
            assert data_post["comment_ids"] == page_post.comment_ids

    def test_get_page_middle(self):
        NUMBER_OF_DOCUMENTS = 10
        page_value = 3
        page_size_value = 3
        page_count_value = 4

        data: list[dict] = self.factory.get_many_documents(NUMBER_OF_DOCUMENTS)
        self.collection.insert_many(data)

        page: Page = self.repository.get_page(
            page=page_value,
            page_size=page_size_value
        )

        assert len(page.items) == page_size_value
        assert page.page_count == page_count_value

        data_post_1 = data[3]  # NUMBER_OF_DOCUMENTS-(PAGE-1)*PAGE_SIZE-NUMPOST
        data_post_2 = data[2]
        data_post_3 = data[1]

        assert page.items[0].title == data_post_1["title"]
        assert page.items[0].content == data_post_1["content"]
        assert page.items[0].author_id == data_post_1["author_id"]
        assert page.items[0].comment_ids == data_post_1["comment_ids"]

        assert page.items[1].title == data_post_2["title"]
        assert page.items[1].content == data_post_2["content"]
        assert page.items[1].author_id == data_post_2["author_id"]
        assert page.items[1].comment_ids == data_post_2["comment_ids"]

        assert page.items[2].title == data_post_3["title"]
        assert page.items[2].content == data_post_3["content"]
        assert page.items[2].author_id == data_post_3["author_id"]
        assert page.items[2].comment_ids == data_post_3["comment_ids"]

    def test_get_page_out_of_range(self):
        NUMBER_OF_DOCUMENTS = 10
        page_value = 800
        page_size_value = 1200
        page_count_value = 1

        data: list[dict] = self.factory.get_many_documents(NUMBER_OF_DOCUMENTS)
        self.collection.insert_many(data)

        page: dict = self.repository.get_page(
            page=page_value,
            page_size=page_size_value
        )

        assert len(page.items) == 0
        assert page.page == page_value
        assert page.page_size == page_size_value
        assert page.page_count == page_count_value
