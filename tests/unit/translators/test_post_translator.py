import pytest
from translators.post_tranlator import PostTranslator
from models.post import Post






class TestPostTranslator:
    @classmethod
    def setup_class(self):
        self.post_translator = PostTranslator()

        self.valid_post_without_m_id = Post(
            text="Text_for_post",
            author="Sviatoslav Bobryshev",
            date_of_creation="2021-08-11T16:52:25.551959"
        )
        
    @classmethod
    def teardown_class(self):
        pass



    def test_to_mongo(self):
        valid_dict = {
            "text": "Text_for_post",
            "author": "Sviatoslav Bobryshev",
            "date_of_creation": "2021-08-11T16:52:25.551959"
        }
        
        assert valid_dict==self.post_translator.to_mongo(
                           self.valid_post_without_m_id), \
               "PostTranslator.to_mongo returns INVALID dict"

                    
    



