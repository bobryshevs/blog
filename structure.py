
from bson.objectid import ObjectId
from dotenv import dotenv_values

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
    UserPresenter,
    TockenPairPresenter
)
from services import (
    PostService,
    UserService,
    ValidateService,
    TokenService
)
from validators import (
    PresenceValidator,
    TypeValidator,
    ObjectIdValidator,
    PositiveIntValidator,
    StrLenValidator,
    EmailValidator,
    UniqueFieldValidator,
    JWTValidator
)
from wrappers import (
    BcryptWrapper,
    JWTWrapper
)
from enums import TimeConstants
from handlers import (
    CreatePostHandler,
    GetPostHandler,
    DeletePostHandler
)
from response_builder import ResponseBuilder

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
jwt_wrapper = JWTWrapper(
    encryption_algorithm=config["JWT_ENCRYPTION_ALGORITHM"],
    key=config["JWT_KEY"],
    access_token_expiration=TimeConstants.QUARTER_OF_AN_HOUR,
    refresh_token_expiration=TimeConstants.MOUNTH
)


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
token_pair_presenter = TockenPairPresenter()
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
type_author_id_validator = TypeValidator(key="author_id", type_=ObjectId)
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

correct_email_validator = EmailValidator(key="email")
user_unique_email_validator = UniqueFieldValidator(
    key="email",
    repository=user_repository)


# / users login validators \\ #
# * presence_email_validator defined in     "users create validators"
# * presence_password_validator defined in  "users create validators"
# * type_email_validator defined in         "users create validators"
# * type_password_validator defined in      "users create validators"
# * email_validator defined in              "users create validators"

# / users refresh validators \\ #
presence_refresh_validator = PresenceValidator(key="refresh")
refresh_jwt_validator = JWTValidator(
    dict_key="refresh",
    encryption_key=config["JWT_KEY"]
)

# / users logout validators \\ #
presence_access_validator = PresenceValidator(key="access")
access_jwt_validator = JWTValidator(
    dict_key="access",
    encryption_key=config["JWT_KEY"]
)


# / token validators \ #
presence_token_validator = PresenceValidator(key="token")
type_token_validator = TypeValidator(key="token", type_=str)
jwt_token_validator = JWTValidator(
    dict_key="token",
    encryption_key=config["JWT_KEY"]
)

# --- Validator Services --- #

# /* User Validate Services \* #
user_create_validate_service = ValidateService(
    [
        presence_email_validator,
        presence_password_validator,
        presence_first_name_validator,
        presence_last_name_validator,

        type_email_validator,
        type_password_validator,
        type_first_name_validator,
        type_last_name_validator,

        correct_email_validator,
        user_unique_email_validator
    ]
)

user_login_validate_service = ValidateService(
    [
        presence_email_validator,
        presence_password_validator,

        type_email_validator,
        type_password_validator,

        correct_email_validator
    ]
)

user_logout_validate_service = ValidateService(
    [
        presence_access_validator,
        access_jwt_validator
    ]
)

user_refresh_validate_service = ValidateService(
    [
        presence_refresh_validator,
        refresh_jwt_validator
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

token_validate_service = ValidateService(
    [
        presence_token_validator,
        type_token_validator,
        jwt_token_validator
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
    jwt_wrapper=jwt_wrapper,
    create_validate_service=user_create_validate_service,
    login_validate_service=user_login_validate_service,
    refresh_validate_service=user_refresh_validate_service,
    logout_validate_service=user_logout_validate_service
)

token_service = TokenService(
    jwt_wrapper=jwt_wrapper,
    user_service=user_service,
    token_validate_service=token_validate_service
)

# -- RESPONSE BUILDERS -- #
response_builder = ResponseBuilder()

# - Handlers - #

# -- Post handlers -- #

# ___ CREATE_POST_HANDLER ___ #
create_post_handler = CreatePostHandler(
    token_service=token_service,
    service=post_service,
    presenter=post_presenter,
    response_builder=response_builder
)

# ___ GET_POST_HANDLER ___ #
get_post_handler = GetPostHandler(
    token_service=token_service,
    service=post_service,
    presenter=post_presenter,
    response_builder=response_builder
)

# ___ DELETE_POST_HANDLER ___ #
delete_post_handler = DeletePostHandler(
    token_service=token_service,
    service=post_service,
    presenter=post_presenter,
    response_builder=response_builder
)
