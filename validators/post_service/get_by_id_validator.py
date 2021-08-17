from exceptions import BadRequest, NotFound
from validators.validator import Validator
from bson import ObjectId


class GetByIdValidator(Validator):

    @staticmethod
    def validate(args: dict, repository) -> None:
        '''
            Checking whether the 'post_id'argument can be represented
            as an instance of the ObjectId class.
            Checking the presence of the desired post in the database
        '''
        post_id = args.get('post_id')
        if not ObjectId.is_valid(post_id):
            raise NotFound()

        if repository.get_by_id(ObjectId(post_id)) is None:
            raise NotFound()
        
