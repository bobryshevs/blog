
import redis
from dotenv import dotenv_values
from pika import (
    PlainCredentials,
    BlockingConnection,
    ConnectionParameters
)

from json_serializers import JsonPostSerializer
from services.comment_service import CommentService
from pymongo import MongoClient
from repositories import (
    PostRepository,
    CommentRepository
)
from translators import (
    PostTranslator,
    CommentTranslator,
    post_tranlator
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

config = dotenv_values(".env")

# --- Mongo --- #
MONGO_HOST = config["MONGO_HOST"]
MONGO_PORT = config["MONGO_PORT"]
MONGO_USER = config["MONGO_USER"]
MONGO_PASSWORD = config["MONGO_PASSWORD"]

mongo_client = MongoClient(f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@"
                           f"{MONGO_HOST}:{MONGO_PORT}")


#  --- Redis --- #
REDIS_HOST = config["REDIS_HOST"]
REDIS_PORT = config["REDIS_PORT"]
DB_NUMBER = 0

redis_obj = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    db=DB_NUMBER
)


# --- RabbitMQ --- #
RMQ_USERNAME = config["RABBITMQ_DEFAULT_USER"]
RMQ_PASSWORD = config["RABBITMQ_DEFAULT_PASS"]
RMQ_HOST = config["RABBITMQ_HOST"]
rmq_credentials = PlainCredentials(
    username=RMQ_USERNAME,
    password=RMQ_PASSWORD
)
rmq_connection = BlockingConnection(
    ConnectionParameters(
        host=RMQ_HOST,
        credentials=rmq_credentials
    )
)
rmq_channel = rmq_connection.channel()

# --- JsonSerializers --- #
json_post_serializer = JsonPostSerializer()

# --- Translators --- #
post_tranlator = PostTranslator()

# --- Repositories --- #
post_repository = PostRepository(
    collection=mongo_client.blog_database.posts,
    translator=post_tranlator
)
comment_repository = CommentRepository(
    collection=mongo_client.blog_data_base.comments,
    translator=CommentTranslator())


# --- Presenters --- #
post_presenter = PostPresenter()
comment_presenter = CommentPresenter()

# --- Validarots --- #

# // post_get_page \\ #
presence_page_validator = PresenceValidator(key="page")
presence_page_size_vaidator = PresenceValidator(key="page_size")

type_page_validator = TypeValidator(key="page", type_=int)
type_page_size_validator = TypeValidator(key="page_size", type_=int)

positive_int_page_validator = PositiveIntValidator("page")
positive_int_page_size_validator = PositiveIntValidator(
    "page_size")

# // post_create \\ #
presence_title_validator = PresenceValidator(key="title")
presence_author_id_validator = PresenceValidator(key="author_id")
presence_content_validator = PresenceValidator(key="content")

type_title_validator = TypeValidator(key="title", type_=str)
type_author_id_validator = TypeValidator(key="author_id", type_=str)
type_content_validator = TypeValidator(key="content", type_=str)

content_title_validator = StrLenValidator(key="title")
content_author_id_validator = StrLenValidator(key="author")

object_id_author_id_validator = ObjectIdValidator(key="author_id")

# // post_get_by_id \\ #
presence_id_validator = PresenceValidator(key="id")

type_str_id_validator = TypeValidator(key="id", type_=str)

object_id_validator = ObjectIdValidator(key="id")


# // post_update \\ #

# presense, type, content of "post_id"
# checked with validators from post_get_by_id

# presense, type, content of "author_id", "title" checked with validators
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
comment_service = CommentService(comment_repository, post_repository)
