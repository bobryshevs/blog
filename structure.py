from models.post import Post
from pymongo import MongoClient
from repositories import PostRepository, CommentRepository
from translators import PostTranslator
from presenters import PostPresenter
from services import PostService
from validators import PostValidator

MONGO_HOST = "localhost"
MONGO_PORT = 27017

mongo_client = MongoClient(f"mongodb://{MONGO_HOST}:{MONGO_PORT}/")

# --- Repositories --- #
post_repository = PostRepository(client=mongo_client,
                                 translator=PostTranslator()
                                 )
comment_repository = CommentRepository(client=mongo_client)


# --- Presenters --- #
post_presenter = PostPresenter()

# --- Validators --- #
post_validator = PostValidator()


# --- Services --- #
post_service = PostService(post_repository, post_presenter) 
