from flask import Request, jsonify
from enums import (
    ActionType,
    HTTP_STATUS
)
from exceptions import (
    BadRequest,
    NotFound,
    Unauthorized,
    Conflict
)
from wrappers import JWTWrapper
from services import (
    ValidateService,
    UserService,
    PostService
)
from presenters import PostPresenter
from models import (
    User,
    Post
)


class CreatePostHandler:
    def __init__(self,
                 jwt_wrapper: JWTWrapper,
                 token_validate_service: ValidateService,
                 post_service: PostService,
                 user_service: UserService,
                 post_presenter: PostPresenter) -> None:
        self.jwt_wrapper = jwt_wrapper
        self.token_validate_service = token_validate_service
        self.user_service = user_service
        self.post_service = post_service
        self.post_presenter = post_presenter

    def handle(self, request, action_type: ActionType) -> tuple[dict, int]:
        try:
            result, status = self.handle_create_post(request)
            return jsonify(result), int(status)
        except (BadRequest, NotFound, Unauthorized, Conflict) as err:
            return jsonify(err.value), err.code

    def handle_create_post(self, request: Request) -> tuple[dict, HTTP_STATUS]:
        access_token: str = self.select_token_from_request(request)
        self.token_validate_service.validate({"token": access_token})

        author: User = self.user_service.get_by_token(access_token)
        args: dict = request.json
        args["author_id"] = author.id
        post: Post = self.post_service.create(args)
        return self.post_presenter.to_json(post), HTTP_STATUS.CREATED

    def select_token_from_request(self, request: Request) -> str:
        bearer: str = request.headers.get("Authorization")
        if bearer is None:
            raise Unauthorized({"msg": "Authorisation header not found"})
        if not bearer.startswith("Bearer "):
            raise BadRequest({"msg": "Invalid Authorization header"})
        token = bearer.split(" ")[1]
        if not token:
            raise BadRequest({"msg": "token not found"})
        return token
