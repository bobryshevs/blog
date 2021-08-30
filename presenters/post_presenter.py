from models import Post


class PostPresenter:

    def to_json(self, post: Post) -> dict:
        return {
            "id": str(post.id),
            "title": post.title,
            "content": post.content,
            "author_id": str(post.author_id),
            "comment_ids": post.str_comment_ids
        }
