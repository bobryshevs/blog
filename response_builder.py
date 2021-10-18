import json
from flask import Response


class ResponseBuilder:

    def build(self, data: dict, status: int) -> Response:
        response = Response(
            json.dumps(data),
            status=status,
            mimetype="application/json"
        )
        return response
