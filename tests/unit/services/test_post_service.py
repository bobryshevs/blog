from exceptions.not_found import NotFound
import pytest
from bson.objectid import ObjectId
from mock import Mock


from services import PostService
from models import Post


class TestPostService:
    def setup(self):
        repository = Mock()
        get_page_validate_service = Mock()
        create_validate_service = Mock()
        object_id_validate_service = Mock()
        update_validate_service = Mock()

        self.mock_arg_list = [
            repository,
            get_page_validate_service,
            create_validate_service,
            object_id_validate_service,
            update_validate_service
        ]

    def test_create(self):
        args = {
            "title": "title",
            "content": "content",
            "author_id": ObjectId(),
        }
        expected_id = ObjectId()
        post_service = PostService(*self.mock_arg_list)
        post_service.repository.create.return_value = expected_id

        result_post = post_service.create(args)

        post_service.create_validate_service.validate.assert_called_once_with(
            args
        )
        post_service.repository.create.assert_called_once()
        assert expected_id == result_post.id

    def test_get_by_id_exists(self):
        args = {"id": ObjectId()}
        post_service = PostService(*self.mock_arg_list)
        expected_post = Post()
        post_service.repository.get_by_id.return_value = expected_post

        result_post = post_service.get_by_id(args)

        post_service.get_by_id_validate_service.validate \
            .assert_called_once_with(args)
        post_service.repository.get_by_id.assert_called_once_with(args['id'])
        assert expected_post == result_post

    def test_get_by_id_not_found(self):
        args = {"id": ObjectId()}
        post_service = PostService(*self.mock_arg_list)
        expected_post = None
        post_service.repository.get_by_id.return_value = expected_post

        with pytest.raises(NotFound):
            post_service.get_by_id(args)

        post_service.get_by_id_validate_service.validate \
            .assert_called_once_with(args)
        post_service.repository.get_by_id.assert_called_once_with(args['id'])

    def test_update_not_found(self):
        args = {
            "id": ObjectId(),
            "text": "post_text",
            "author": "sviatoslav"
        }
        expected_post = None
        post_service = PostService(*self.mock_arg_list)
        post_service.repository.get_by_id.return_value = expected_post

        with pytest.raises(NotFound):
            post_service.update(args)

        post_service.update_validate_service.validate \
            .assert_called_once_with(args)
        post_service.repository.get_by_id.assert_called_once_with(args['id'])

    def test_update_exists(self):
        args = {
            "id": ObjectId(),
            "title": "title",
            "content": "content",
            "author_id": ObjectId()
        }
        expected_post = Post()
        post_service = PostService(*self.mock_arg_list)
        post_service.repository.get_by_id.return_value = expected_post

        post_service.update(args)

        post_service.update_validate_service.validate \
            .assert_called_once_with(args)
        post_service.repository.get_by_id.assert_called_once_with(args['id'])
        post_service.repository.update.assert_called_once()

    def test_delete_not_found(self):
        args = {"id": ObjectId()}
        expected_post = None
        post_service = PostService(*self.mock_arg_list)
        post_service.repository.exists.return_value = expected_post

        with pytest.raises(NotFound):
            post_service.delete(args)
        post_service.delete_validate_service.validate \
            .assert_called_once_with(args)

    def test_delete_exists(self):
        args = {"id": ObjectId()}
        expected_post = Post()
        post_service = PostService(*self.mock_arg_list)
        post_service.repository.exists.return_value = expected_post

        post_service.delete(args)

        post_service.delete_validate_service.validate \
            .assert_called_once_with(args)
        post_service.repository.exists.assert_called_once_with(args['id'])
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
