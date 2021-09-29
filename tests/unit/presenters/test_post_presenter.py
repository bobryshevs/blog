from bson import ObjectId
from models import Post
from presenters import PostPresenter


class TestPostPresenter:

    def test_to_json(self):
        presenter = PostPresenter()
        model = Post()
        model.id = ObjectId()
        model.title = "title"
        model.content = "content"
        model.author_id = ObjectId()
        model.comment_ids = [ObjectId(), ObjectId(), ObjectId()]

        result = presenter.to_json(model)
        
        assert isinstance(result, dict)
        assert str(model.id) == result["id"]
        assert model.title == result["title"]
        assert model.content == result["content"]
        assert str(model.author_id) == result["author_id"] 
        assert str(model.comment_ids[0]) == result["comment_ids"][0]
        assert str(model.comment_ids[1]) == result["comment_ids"][1]
        assert str(model.comment_ids[2]) == result["comment_ids"][2]