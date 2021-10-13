import json
from flask import Response

from enums import HTTPStatus


class ResponseBuilder:

    def build(self, data: dict, status: HTTPStatus) -> Response:
        response = Response(
            json.dumps(data),
            status=status,
            mimetype="application/json"
        )
        return response
