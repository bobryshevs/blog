from abc import abstractmethod

from services import TokenService
from flask import (
    Response,
    Request
)

from exceptions import (
    BadRequest,
    Conflict,
    NotFound,
    Unauthorized
)
from models import User
from enums import HTTPStatus


class BaseHandler:
    def __init__(
            self,
            token_service,
            service,
            presenter,
            response_builder) -> None:
        self.token_service: TokenService = token_service
        self.service = service
        self.presenter = presenter
        self.response_builder = response_builder

    def handle(self, request: Request) -> Response:
        principle: User = self.token_service.get_principle(request.headers)
        try:
            result, status = self.execute(request, principle)
            result = self.response_builder.build(
                data=result,
                status=int(status)  # Flask doesn't support enum cast inside
            )
        except (BadRequest, Conflict, NotFound, Unauthorized) as err:
            result = self.response_builder.build(
                data=err.value,
                status=err.code
            )
        return result

    @abstractmethod
    def execute(
        self,
        request: Request,
        principle: User) -> tuple[dict, HTTPStatus]: ...
