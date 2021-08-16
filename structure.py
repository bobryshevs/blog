from models.post import Post
from pymongo import MongoClient
from repositories import PostRepository, CommentRepository
from translators import PostTranslator, CommentTranslator
from presenters import PostPresenter
from services import PostService

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


# --- Services --- #
post_service = PostService(post_repository, post_presenter)
