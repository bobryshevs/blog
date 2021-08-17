from validators import validator
from validators.validator import Validator
from exceptions import NotFound, BadRequest


class CreateValidator(Validator):

    @staticmethod
    def validate(args: dict) -> None:
        '''
            Checking the 'text' and 'author'arguments
        '''
        text = args.get('text')
        if not isinstance(text, str):
            raise BadRequest()

        author = args.get('author')
        if not isinstance(author, str):
            raise BadRequest()

        if not len(author):
            raise BadRequest()
