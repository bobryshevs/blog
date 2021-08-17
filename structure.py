from services.comment_service import CommentService
from models.post import Post
from pymongo import MongoClient
from repositories import PostRepository, CommentRepository
from translators import PostTranslator, CommentTranslator
from presenters import PostPresenter, CommentPresenter
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
comment_presenter = CommentPresenter()

# --- Services --- #
post_service = PostService(post_repository)
comment_service = CommentService(comment_repository, post_repository)
