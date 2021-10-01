
from dotenv import dotenv_values
from pika import (
    PlainCredentials,
    BlockingConnection,
    ConnectionParameters
)

from json_serializers import JsonPostSerializer
from pymongo import MongoClient
from repositories import (
    PostRepository,
    UserRepository,
)
from translators import (
    PostTranslator,
    UserTranslator
)
from presenters import (
    PostPresenter,
    UserPresenter
)
from services import (
    PostService,
    UserService,
    ValidateService
)
from validators import (
    PresenceValidator,
    TypeValidator,
    ObjectIdValidator,
    PositiveIntValidator,
    StrLenValidator,
    EmailValidator,
    UniqueFieldValidator
)
from wrappers import (
    BcryptWrapper
)
config = dotenv_values(".env")

# --- Mongo --- #
MONGO_HOST = config["MONGO_HOST"]
MONGO_PORT = config["MONGO_PORT"]
MONGO_USER = config["MONGO_USER"]
MONGO_PASSWORD = config["MONGO_PASSWORD"]

mongo_client = MongoClient(f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@"
                           f"{MONGO_HOST}:{MONGO_PORT}")

# --- Wrappers --- #
bcrypt_wrapper = BcryptWrapper()


# --- JsonSerializers --- #
json_post_serializer = JsonPostSerializer()

# --- Translators --- #
post_tranlator = PostTranslator()
user_translator = UserTranslator()

# --- Repositories --- #
post_repository = PostRepository(
    collection=mongo_client.blog_database.posts,
    translator=post_tranlator
)
user_repository = UserRepository(
    collection=mongo_client.blog_database.users,
    translator=user_translator
)

# --- Presenters --- #
post_presenter = PostPresenter()
user_presenter = UserPresenter()
# --- Validarots --- #

# / post_get_page \\ #
presence_page_validator = PresenceValidator(key="page")
presence_page_size_vaidator = PresenceValidator(key="page_size")

type_page_validator = TypeValidator(key="page", type_=int)
type_page_size_validator = TypeValidator(key="page_size", type_=int)

positive_int_page_validator = PositiveIntValidator("page")
positive_int_page_size_validator = PositiveIntValidator(
    "page_size")

# / post_create \\ #
presence_title_validator = PresenceValidator(key="title")
presence_author_id_validator = PresenceValidator(key="author_id")
presence_content_validator = PresenceValidator(key="content")

type_title_validator = TypeValidator(key="title", type_=str)
type_author_id_validator = TypeValidator(key="author_id", type_=str)
type_content_validator = TypeValidator(key="content", type_=str)

content_title_validator = StrLenValidator(key="title")
content_author_id_validator = StrLenValidator(key="author")

object_id_author_id_validator = ObjectIdValidator(key="author_id")

# / post_get_by_id \\ #
presence_id_validator = PresenceValidator(key="id")

type_str_id_validator = TypeValidator(key="id", type_=str)

object_id_validator = ObjectIdValidator(key="id")


# / post_update \\ #

# presense, type, content of "post_id"
# checked with validators from post_get_by_id

# presense, type, content of "author_id", "title" checked with validators
# from post_create


# / post_delete \\ #

# presense, type, content of "post_id"
# checked with validators from post_get_by_id


# / users create validators \\ #
presence_email_validator = PresenceValidator(key="email")
presence_password_validator = PresenceValidator(key="password")
presence_first_name_validator = PresenceValidator(key="first_name")
presence_last_name_validator = PresenceValidator(key="last_name")


type_email_validator = TypeValidator(key="email", type_=str)
type_password_validator = TypeValidator(key="password", type_=str)
type_first_name_validator = TypeValidator(key="first_name", type_=str)
type_last_name_validator = TypeValidator(key="last_name", type_=str)

email_validator = EmailValidator(key="email")
user_unique_email_validator = UniqueFieldValidator(
    key="email",
    repository=user_repository)

# --- Validator Services --- #

# /* User Validate Services \* #
create_user_validate_service = ValidateService(
    [
        presence_email_validator,
        presence_password_validator,
        presence_first_name_validator,
        presence_last_name_validator,

        type_email_validator,
        type_password_validator,
        type_first_name_validator,
        type_last_name_validator,

        email_validator,
        user_unique_email_validator
    ]
)


# /* Post Validate Services \* #
get_page_validate_service = ValidateService(
    [
        presence_page_validator,
        presence_page_size_vaidator,
        type_page_validator,
        type_page_size_validator,
        positive_int_page_validator,
        positive_int_page_size_validator
    ]
)
create_validate_service = ValidateService(
    [
        presence_title_validator,
        presence_author_id_validator,
        presence_content_validator,
        type_title_validator,
        type_author_id_validator,
        type_content_validator,
        content_title_validator,
        content_author_id_validator,
        object_id_author_id_validator
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
        presence_title_validator,
        presence_author_id_validator,
        presence_id_validator,
        presence_content_validator,
        type_author_id_validator,
        type_title_validator,
        type_content_validator,
        content_author_id_validator,
        content_title_validator,
        object_id_author_id_validator,
        object_id_validator
    ]
)

# --- Services --- #
post_service = PostService(post_repository,
                           get_page_validate_service,
                           create_validate_service,
                           object_id_validate_service,
                           post_update_validator_service,
                           )

user_service = UserService(
    repository=user_repository,
    bcrypt_wrapper=bcrypt_wrapper,
    create_validate_service=create_user_validate_service
)
