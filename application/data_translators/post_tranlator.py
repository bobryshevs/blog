from application.data_models.post import Post

class PostTranslator:

    def to_mongo(self, post: Post) -> dict:
        return {
            "text": post.text,
            "img": post.img_link,
            "author": post.author,
            "create_date": post.create_date
        }