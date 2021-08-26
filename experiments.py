from re import I
from bson.objectid import ObjectId
from structure import r, post_repository
from translators import PostTranslator
from models import Post

post = Post()
post.id = ObjectId()
post.title = "title"
post.content = "content"
post.author_id = ObjectId()
post.comment_ids = [ObjectId() for _ in range(10)]


pt = PostTranslator()


to_redis = pt.to_json_str(post)

r.set(post.str_id, to_redis)

from_redis = pt.from_json_str(r.get(post.str_id))

print(from_redis)


post_repository.delete(123)