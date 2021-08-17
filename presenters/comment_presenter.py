from models import Comment


class CommentPresenter:

    def to_json(self, comment: Comment) -> dict:
        return {
            "id": comment.id,
            "text": comment.text,
            "author": comment.author,
            "post_id": str(comment.post_id),
            "date_of_creation": comment.date_of_creation,
        }