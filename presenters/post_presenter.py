from models.post import Post


class PostPresenter:

    def to_json(self, post: Post) -> dict:
        return {
            "text": post.text,
            "author": post.author,
            "date_of_creation": post.date_of_creation,
            "_id": post.id
        }
    
