from mock import Mock

from handlers.base_handler import BaseHandler


class TestBaseHandler:
    def setup(self):
        self.token_service = Mock()
        self.service = Mock()
        self.presenter = Mock()
        self.response_builder = Mock()
        self.handler = BaseHandler(
            token_service=self.token_service,
            service=self.service,
            presenter=self.presenter,
            response_builder=self.response_builder
        )

    def test_handle(self):
        exec_result = {}
        exec_status = 200
        self.handler.execute = Mock(return_value=(exec_result, exec_status))
        request = Mock()
        headers = {}
        request.headers = headers
        user = object()
        response = object()

        self.token_service.get_principle.return_value = user
        self.response_builder.build.return_value = response

        handler_result = self.handler.handle(request)

        self.token_service.get_principle.assert_called_once_with(headers)
        self.handler.execute.assert_called_once_with(request, user)
        self.response_builder.build.assert_called_once_with(
            data=exec_result,
            status=exec_status
        )
        assert handler_result == response
