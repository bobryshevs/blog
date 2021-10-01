from .user_factory import UserFactory
from .mongo_repository_factory import (
    MongoRepositoryFactory,
    MongoTestModel,
    MongoTestModelTranslator
)

user_factory = UserFactory()
mongo_repository_factory = MongoRepositoryFactory()
mongo_test_model_translator = MongoTestModelTranslator()
