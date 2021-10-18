from exceptions.not_found import NotFound
import pytest
from bson.objectid import ObjectId
from mock import Mock


from services import PostService
from models import Post, User


class TestPostService:
    def setup(self):
        self.repository = Mock()
        self.user_service = Mock()
        self.get_page_validate_service = Mock()
        self.create_validate_service = Mock()
        self.object_id_validate_service = Mock()
        self.update_validate_service = Mock()
        self.get_by_id_validate_service = self.object_id_validate_service

        self.service = PostService(
            repository=self.repository,
            user_service=self.user_service,
            get_page_validate_service=self.get_page_validate_service,
            create_validate_service=self.create_validate_service,
            object_id_validate_service=self.object_id_validate_service,
            update_validate_service=self.update_validate_service
        )

    def test_create(self):
        principle = User(id=ObjectId())
        self.service.principle_check_none = Mock(return_value=None)

        self.create_validate_service.validate = Mock(return_value=True)

        post_id = ObjectId()
        self.repository.create = Mock(return_value=post_id)

        args = {
            "title": "title",
            "content": "content",
            "author_id": principle.id,
        }

        result = self.service.create(args=args, principle=principle)

        assert isinstance(result, Post)
        assert result.title == args["title"]
        assert result.content == args["content"]
        assert result.author_id == args["author_id"]

        self.service.principle_check_none.assert_called_once_with(
            principle
        )

        self.create_validate_service.validate.assert_called_once_with(args)
        self.repository.create.assert_called_once()

    def test_get_by_id_exists(self):
        self.get_page_validate_service.validate = Mock(return_value=True)

        args = {"id": ObjectId()}

        get_by_id_value = Post(id=args["id"])
        self.repository.get_by_id = Mock(return_value=get_by_id_value)

        result = self.service.get_by_id(args)

        assert isinstance(result, Post)
        self.get_by_id_validate_service.validate.assert_called_once_with(args)
        self.repository.get_by_id.assert_called_once_with(get_by_id_value.id)
        assert result.id == args["id"]

    def test_get_by_id_not_found(self):
        self.get_by_id_validate_service.validate = Mock(return_value=True)

        get_by_id_value = None
        self.repository.get_by_id = Mock(return_value=get_by_id_value)

        args = {"id": ObjectId()}
        with pytest.raises(NotFound) as err:
            self.service.get_by_id(args)

        assert err.value.code == 404
        self.get_by_id_validate_service.validate.assert_called_once_with(args)
        self.repository.get_by_id.assert_called_once_with(args["id"])

    def test_update_not_found(self):
        self.service.principle_check_none = Mock(return_value=None)
        self.update_validate_service.validate = Mock(return_value=True)
        self.service.get_by_id = Mock(side_effect=NotFound({}))

        principle = User(id=ObjectId())
        args = {
            "id": ObjectId(),
            "title": "tile of the post",
            "content": "post_text",
            "author_id": principle.id
        }
        with pytest.raises(NotFound) as err:
            self.service.update(args, principle)

        assert err.value.code == 404
        self.service.principle_check_none.assert_called_once_with(principle)
        self.update_validate_service.validate.assert_called_once_with(args)
        self.service.get_by_id.assert_called_once_with(args["id"])

    def test_update_exists(self):
        self.service.principle_check_none = Mock(return_value=None)
        self.update_validate_service.validate = Mock(return_value=True)

        principle = User(id=ObjectId())

        post = Post(id=ObjectId())
        post.author_id = principle.id
        self.service.get_by_id = Mock(return_value=post)

        self.repository.update = Mock(return_value=None)

        args = {
            "id": post.id,
            "title": "title",
            "content": "content",
            "author_id": principle.id
        }
        result = self.service.update(args, principle)

        self.service.principle_check_none.assert_called_once_with(principle)
        self.update_validate_service.validate.assert_called_once_with(args)
        self.service.get_by_id.assert_called_once_with(args["id"])
        self.repository.update.assert_called_once()
        assert isinstance(result, Post)
        assert result.id == args["id"]
        assert result.title == args["title"]
        assert result.content == args["content"]
        assert result.author_id == args["author_id"]

    def test_delete_not_found(self):
        args = {"id": ObjectId()}
        expected_post = None
        post_service = PostService(*self.mock_arg_list)
        post_service.get_by_id = Mock(return_value=None, side_effect=NotFound)

        principle = Mock()
        principle.id = ObjectId()

        with pytest.raises(NotFound):
            post_service.delete(args, principle)
        post_service.delete_validate_service.validate \
            .assert_called_once_with(args)

    def test_delete_exists(self):

        args = {"id": ObjectId()}
        expected_post = Post()
        expected_post.author_id = args["id"]
        post_service = PostService(*self.mock_arg_list)
        post_service.get_by_id = Mock(return_value=expected_post)

        principle = Mock()
        principle.id = args["id"]

        post_service.delete(args, principle)

        post_service.delete_validate_service.validate \
            .assert_called_once_with(args)
        post_service.repository.delete.assert_called_once_with(args['id'])

    def test_get_page(self):
        args = {
            "page": 1,
            "page_size": 3
        }
        expected_list = []
        post_service = PostService(*self.mock_arg_list)
        post_service.repository.get_page.return_value = expected_list

        result_list = post_service.get_page(args)

        post_service.get_page_validate_service.validate \
            .assert_called_once_with(args)
        post_service.repository.get_page.assert_called_once_with(
            args['page'],
            args['page_size']
        )
        assert expected_list == result_list
