from translators import CommentTranslator, comment_translator
from pymongo.mongo_client import MongoClient
from bson import ObjectId
from repositories.repository import MongoRepository
from models import Comment


class CommentRepository(MongoRepository):
    def __init__(self, translator, collection):
        super().__init__(translator, collection)

    # def create(self, comment: Comment) -> ObjectId:
    #     return self.coll.insert_one(self.translator.to_document(comment)) \
    #         .inserted_id

    # def get_by_id(self, comment_id: ObjectId) -> Comment:
    #     comment = self.coll.find_one({"_id": comment_id})
    #     if not comment:
    #         return None
    #     return self.translator.from_document(comment)

    # def update(self, comment: Comment) -> Comment:
    #     self.coll.update_one(
    #         {"_id": comment.id},
    #         {"$set": self.translator.to_document(comment)})
    #     return comment

    # def delete(self, comment_id) -> None:
    #     self.coll.delete_one({'_id': comment_id})

    # def exists(self, comment_id: ObjectId) -> bool:
    #     return self.get_by_id(comment_id) is not None
