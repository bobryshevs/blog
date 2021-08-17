from bson.objectid import ObjectId
from validators.validator import Validator
from exceptions import NotFound 


class DeleteValidator(Validator):

    @staticmethod
    def validate(args: dict, repository) -> None:
        '''
            Checking whether the 'post_id'argument can be represented
            as an instance of the ObjectId class

            Checking the presence of the desired post in the database

        '''
        post_id = args.get('post_id')

        if not ObjectId.is_valid(post_id):
            raise NotFound()

        if not repository.exists(ObjectId(post_id)):
            raise NotFound()
