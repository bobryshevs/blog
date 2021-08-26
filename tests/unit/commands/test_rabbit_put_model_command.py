from mock import Mock
from commands import RabbitPutModelCommand


class TestRabbitPutModelCommand:

    def test_do(self):
        channel = Mock()
        serializer = Mock()
        serializer.to_json.return_value = None
        model = Mock()
        routing_key = ""

        command = RabbitPutModelCommand(
            channel=channel,
            json_serializer=serializer,
            routing_key=routing_key
        )

        command.do(model)

        serializer.to_json.assert_called_once_with(model)
        channel.basic_publish.assert_called_once_with(
            exchange="",
            routing_key=routing_key,
            body=serializer.to_json.return_value
        )
