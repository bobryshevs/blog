from typing import Type
from services.comment_service import CommentService
from models.post import Post
from pymongo import MongoClient
from repositories import PostRepository, CommentRepository
from translators import PostTranslator, CommentTranslator
from presenters import PostPresenter, CommentPresenter
from services import PostService, ValidateService
from validators import (
    PresenceValidator,
    TypeValidator,
    ContentNonZeroStrValidator,
    ContentObjectIdValidator,
    ContentPositiveIntValidator,
    ContentIntRepresentableValidator
)
MONGO_HOST = "localhost"
MONGO_PORT = 27017

mongo_client = MongoClient(f"mongodb://{MONGO_HOST}:{MONGO_PORT}/")

# --- Repositories --- #
post_repository = PostRepository(
    collection=mongo_client.blog_database.posts,
    translator=PostTranslator()
)
comment_repository = CommentRepository(
    collection=mongo_client.blog_data_base.comments,
    translator=CommentTranslator())


# --- Presenters --- #
post_presenter = PostPresenter()
comment_presenter = CommentPresenter()

# --- Validarots --- #

# // post_get_page \\ #
post_get_page_presence_page = PresenceValidator(key='page')
post_get_page_presence_page_size = PresenceValidator(key='page_size')

post_get_page_type_page = TypeValidator(key='page', type_=str)
post_get_page_type_page_size = TypeValidator(key='page_size', type_=str)

post_get_page_content_int_representable_page = ContentIntRepresentableValidator(
    key='page')
post_get_page_content_int_representable_page_size = ContentIntRepresentableValidator(
    'page_size')
post_get_page_content_positive_int_page = ContentPositiveIntValidator('page')
post_get_page_content_positive_int_page_size = ContentPositiveIntValidator(
    'page_size')

# // post_create \\ #
post_presence_text = PresenceValidator(key='text')
post_presence_author = PresenceValidator(key='author')

post_type_text = TypeValidator(key='text', type_=str)
post_type_author = TypeValidator(key='author', type_=str)

post_content_author = ContentNonZeroStrValidator(key='author')


# // post_get_by_id \\ #
post_presence_post_id = PresenceValidator(key='post_id')

post_type_post_id = TypeValidator(key='post_id', type_=str)

post_content_post_id = ContentObjectIdValidator(key='post_id')


# // post_update \\ #

# presense, type, content of "post_id"
# checked with validators from post_get_by_id

# presence, type of "text" chekced with validators from post_create
# presense, type, content of "author" checked with validators f
# from post_create


# // post_delete \\ #

# presense, type, content of "post_id"
# checked with validators from post_get_by_id


# --- Validator Services --- #
post_get_page_validator_service = ValidateService(
    [
        post_get_page_presence_page,
        post_get_page_presence_page_size,
        post_get_page_type_page,
        post_get_page_type_page_size,
        post_get_page_content_int_representable_page,
        post_get_page_content_int_representable_page_size,
        post_get_page_content_positive_int_page,
        post_get_page_content_positive_int_page_size
    ]
)
post_create_validator_service = ValidateService(
    [
        post_presence_text,
        post_presence_author,
        post_type_text,
        post_type_author,
        post_content_author
    ]
)
post_get_by_id_validator_service = ValidateService(
    [
        post_presence_post_id,
        post_type_post_id,
        post_content_post_id
    ]
)
post_update_validator_service = ValidateService(
    [
        post_presence_post_id,
        post_type_post_id,
        post_content_post_id,
        post_presence_text,
        post_type_text,
        post_presence_author,
        post_type_author,
        post_content_author
    ]
)

post_delete_validator_service = ValidateService(
    # Copy of post_get_by_id_validator_service :(
    [
        post_presence_post_id,
        post_type_post_id,
        post_content_post_id
    ]
)
# --- Services --- #
post_service = PostService(post_repository,
                           post_get_page_validator_service,
                           post_create_validator_service,
                           post_get_by_id_validator_service,
                           post_update_validator_service,
                           post_delete_validator_service)
comment_service = CommentService(comment_repository, post_repository)
