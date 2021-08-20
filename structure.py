from services.comment_service import CommentService
from pymongo import MongoClient
from repositories import (
    PostRepository,
    CommentRepository
)
from translators import (
    PostTranslator,
    CommentTranslator
)
from presenters import (
    PostPresenter,
    CommentPresenter
)
from services import (
    PostService,
    ValidateService
)
from validators import (
    PresenceValidator,
    TypeValidator,
    ObjectIdValidator,
    PositiveIntValidator,
    IntRepresentableValidator,
    StrLenValidator
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
presence_page_validator = PresenceValidator(key='page')
presence_page_size_vaidator = PresenceValidator(key='page_size')

type_page_validator = TypeValidator(key='page', type_=str)
type_page_size_validator = TypeValidator(key='page_size', type_=str)

int_representable_page_validator = IntRepresentableValidator(
    key='page')
int_representable_page_size_validator = IntRepresentableValidator(
    'page_size')
positive_int_page_validator = PositiveIntValidator('page')
positive_int_page_size_validator = PositiveIntValidator(
    'page_size')

# // post_create \\ #
presence_text_validator = PresenceValidator(key='text')
presence_author_validator = PresenceValidator(key='author')

type_text_validator = TypeValidator(key='text', type_=str)
type_author_validator = TypeValidator(key='author', type_=str)

content_author_validator = StrLenValidator(key='author')


# // post_get_by_id \\ #
presence_id_validator = PresenceValidator(key='post_id')

type_str_id_validator = TypeValidator(key='post_id', type_=str)

object_id_validator = ObjectIdValidator(key='post_id')


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
get_page_validate_service = ValidateService(
    [
        presence_page_validator,
        presence_page_size_vaidator,
        type_page_validator,
        type_page_size_validator,
        int_representable_page_validator,
        int_representable_page_size_validator,
        positive_int_page_validator,
        positive_int_page_size_validator
    ]
)
create_validate_service = ValidateService(
    [
        presence_text_validator,
        presence_author_validator,
        type_text_validator,
        type_author_validator,
        content_author_validator
    ]
)
object_id_validate_service = ValidateService(
    [
        presence_id_validator,
        type_str_id_validator,
        object_id_validator
    ]
)
post_update_validator_service = ValidateService(
    [
        presence_id_validator,
        type_str_id_validator,
        object_id_validator,
        presence_text_validator,
        type_text_validator,
        presence_author_validator,
        type_author_validator,
        content_author_validator
    ]
)

# --- Services --- #
post_service = PostService(post_repository,
                           get_page_validate_service,
                           create_validate_service,
                           object_id_validate_service,
                           post_update_validator_service,
                           )
comment_service = CommentService(comment_repository, post_repository)
