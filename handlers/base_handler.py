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
    Unauthorized,
    Forbidden
)
from models import User, Model


class BaseHandler:
    def __init__(
            self,
            token_service,
            service,
            presenter,
            response_builder,
            success_http_status_code: int) -> None:
        self.token_service: TokenService = token_service
        self.service = service
        self.presenter = presenter
        self.response_builder = response_builder
        self.success_http_status_code = success_http_status_code

    def handle(self, request: Request) -> Response:
        try:
            principle: User = self.token_service.get_principle(request.headers)
            result = self.execute(request, principle)
            result = self.presenter.present(result) if result else {}
            result = self.response_builder.build(
                data=result,
                status=self.success_http_status_code
            )
        except (BadRequest, Conflict, NotFound, Unauthorized, Forbidden) as e:
            result = self.response_builder.build(
                data=e.value,
                status=e.code
            )
        return result

    @abstractmethod
    def execute(self, request: Request, principle: User) -> Model: ...
