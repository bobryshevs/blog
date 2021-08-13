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


# --- update TESTS <<START>> --- #


# --- create TESTS <<START>> --- #

    def test_create_invalid_text(self):
        '''
            The post will not be created, because the author field is not valid
        '''
        valid_author = 'valid_author'
        invalid_texts = [1, 1.1, {}, [], set(), ObjectId()]
        expected = None

        for invalid_text in invalid_texts:
            result = self.repository.create(invalid_text, valid_author)
            assert result is None

    def test_create_invalid_author(self):
        '''
            The post will not be created, because the author field is not valid
        '''
        valid_text = 'valid_text'
        invalid_authors = [1, 1.1, {}, [], set(), ObjectId()]
        expected = None

        for invalid_author in invalid_authors:
            result = self.repository.create(valid_text, invalid_author)

            assert result is None

    def test_create_valid_text_and_author(self):
        '''
            The post is being created successfully 
        '''
        valid_data = [
            {
                "id": ObjectId(),
                "text": '',
                "author": ''
            },
            {
                "id": ObjectId(),
                "text": 'abc',
                "author": 'auth'
            },
            {
                "id": ObjectId(),
                "text": 'very_long_text'*100,
                "author": 'very_long_fullname'*100
            }
        ]
        expected = [data['id'] for data in valid_data]

        for i, data in enumerate(valid_data):
            self.col.insert_one().inserted_id = expected[i]
            result = self.repository.create(data['text'], data['author'])

            assert isinstance(result, ObjectId)
            assert expected[i] == result

# --- create TESTS <<END>> --- #


# --- delete_by_id TESTS <<START>> --- #

    def test_delete_by_id_post_doesnt_exists(self):
        '''
            There is no such post in the database,
            but the objId is valid
        '''
        expected = False
        self.col.find_one.return_value = None

        valid_id_list = [
            '6111371a6e34b54502afbf3d',
            '61113799d359477d3a6669af',
            '61113c30950e7e9fe536770e'
        ]

        for valid_id in valid_id_list:
            result = self.repository.delete_by_id(valid_id)

            assert isinstance(result, bool)
            assert expected == result


    def test_delete_by_id_invalid_objId(self):
        '''
            There is no such post in the database,
            since an invalid objId was passed.
        '''
        expected = False

        self.col.find_one.return_value = None
        invalid_id_list = ['', '123', 123, 1.2, [], (), {}]

        for invalid_id in invalid_id_list:
            result = self.repository.delete_by_id(invalid_id)

            assert isinstance(result, bool)
            assert expected == result


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


# --- delete_by_id TESTS <<END>> --- #


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

# --- get_by_id TESTS <<END>> --- #
