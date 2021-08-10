from application.data_models.comment import Comment


class CommentTranslator:

    def to_mongo(self, comment: Comment):
        return {
            "user_id": comment.user_id,
            "text": comment.text,
            "date_of_creation": comment.timestamp_of_creation,
            "post_id": comment.post_id
        }
