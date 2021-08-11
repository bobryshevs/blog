from pymongo.mongo_client import MongoClient
from bson import ObjectId
from repositories.repository import Repository


class CommentRepository(Repository):
    def __init__(self, client: MongoClient) -> None:
        self.client = client
        self.db = client.blog_database
        self.collection = client.blog_database.comments

    
    def get_comment_by_id(self, comment_id: str):
        obj_comment_id = ObjectId(comment_id)
        comment = self.collection.find_one({'_id': obj_comment_id})
        self.change_element_objID_to_str(comment)
        return comment

    
    def get_comment_pages(self, page_size: int, page_number: int) -> list:
        comments = list(self.collection.find().sort('_id', -1) \
            .skip(page_number*page_size-page_size) \
            .limit(page_size))
        self.change_list_elements_objID_to_str(comments)
        return comments