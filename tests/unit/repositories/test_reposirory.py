from repositories.post_repository import PostRepository
from datetime import datetime
from bson.objectid import ObjectId
from translators import PostTranslator
from mock import (
    Mock,
    MagicMock
)


class TestPostRepository:
    def setup(self):
        self.repository = PostRepository(
            client=Mock(),
            translator=PostTranslator())
        self.col = self.repository.collection

    def teardown(self):
        pass
    
# --- delete_by_id TESTS <<START>> --- #
 
    def test_delete_by_id_post_exists(self):
        '''
            There is a post in the database.
            The ObjectId passed to the function is valid. 
        '''
        expected = True

        documents = [{
            "_id": ObjectId("6111371a6e34b54502afbf3d"),
            "text": "first_document",
            "author": "Sviat",
            "date_of_creation": datetime(2021, 8, 9, 17, 11, 37, 200000)
 
        }]
        self.col.find_one = MagicMock(side_effect=documents)
        self.col.delete_one.return_value = True

        for _ in range(len(documents)):
            result = self.repository.delete_by_id(ObjectId())
            assert isinstance(result, bool)
            assert expected == result
        
        assert self.col.delete_one.call_count == len(documents)


# --- get_by_id TESTS <<START>> --- #
    def test_get_by_id_with_ivalid_objId(self):
        '''
            Request to database contains an invalid objId
        '''

        self.col.find_one.return_value = None
        invalid_id_list = ['', '123', 123, 1.2, [], (), {}]
        
        expected = None
        for invalid_id in invalid_id_list:
            result = self.repository.get_by_id(invalid_id)
            assert expected == result, \
                f'Incorrect response with invalid id' \
                f'which type is {type(invalid_id)}'

    def test_get_by_id_doesnt_existsId(self):
        '''
            The database returns None 
        '''
        
        expected = None
        self.repository.collection.find_one.return_value = None

        result = self.repository.get_by_id(post_id=ObjectId())

        assert result is None
        assert result == expected
        assert self.repository.collection.find_one.call_count == 1

    def test_get_by_id_existsId(self):
        '''
            The database returns an object that exists.
            ObjectId is valid
        '''

        documents = [
            {
                "_id": ObjectId("6111371a6e34b54502afbf3d"),
                "text": "first_document",
                "author": "Sviat",
                "date_of_creation": datetime(2021, 8, 9, 17, 11, 37, 200000)
            },
            {
                "_id": ObjectId("61113c30950e7e9fe536770e"),
                "text": "second_document",
                "author": "Nick",
                "date_of_creation": datetime(2021, 8, 9, 16, 10, 37, 200000)
            }]

        col = self.repository.collection
        col.find_one = MagicMock(side_effect=documents)

        for expected in documents:
            result = self.repository.collection.find_one({ObjectId()})

            assert isinstance(result, dict) is True
            assert expected['_id'] == result['_id']
            assert expected['text'] == result['text']
            assert expected['author'] == result['author']
            assert expected['date_of_creation'] == \
                result['date_of_creation']

        assert col.find_one.call_count == len(documents), \
            f"Mock find_one must be called {len(documents)} times" \
            f"but {col.find_one.call_count} in this case."
# --- get_by_id TESTS <<END>> --- #