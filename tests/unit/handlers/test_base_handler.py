from flask import Response
from bson import ObjectId
from mock import Mock
import pytest

from handlers.base_handler import BaseHandler
from models import User
from exceptions import (
    BadRequest,
    Conflict,
    NotFound,
    Unauthorized,
    Forbidden
)


class TestBaseHandler:
    def setup(self):
        self.token_service = Mock()
        self.service = Mock()
        self.presenter = Mock()
        self.response_builder = Mock()
        self.response_status = 1337
        self.handler = BaseHandler(
            token_service=self.token_service,
            service=self.service,
            presenter=self.presenter,
            response_builder=self.response_builder,
            success_http_status_code=self.response_status
        )

    def test_handle(self):
        user_id = ObjectId()

        get_principle_val = User(id=user_id)
        self.token_service.get_principle = Mock(return_value=get_principle_val)

        execute_value = User(id=user_id)
        self.handler.execute = Mock(return_value=execute_value)

        presenter_value = {"id": user_id}
        self.presenter.present = Mock(return_value=presenter_value)

        response_builder_value = Response(status=int(self.response_status))
        self.response_builder.build = Mock(return_value=response_builder_value)

        request = Mock()
        request.headers = {"Authorization": "Bearer big_token_string"}
        result = self.handler.handle(request)

        assert isinstance(result, Response)
        self.token_service.get_principle.assert_called_once_with(
            request.headers
        )
        self.handler.execute.assert_called_once_with(
            request,
            get_principle_val
        )
        self.presenter.present.assert_called_once_with(execute_value)
        self.response_builder.build.assert_called_once_with(
            data=presenter_value,
            status=int(self.response_status)
        )
        assert result == response_builder_value
