from models import Model
from commands import (
    Command,
    ReversibleCommand,
)
from exceptions import TransactExecutorException


class TransactionExecutor:
    def __init__(self, commands: list[Command]) -> None:
        self._check_commands(commands)
        self.commands: list[Command] = commands

    def execute(self, model: Model):
        for i, command in enumerate(self.commands):
            try:
                command.do(model)
            except Exception as err:
                self.rollback(index=i)
                TransactExecutorException(str(err))

    def rollback(self, index: int):
        for i in range(index, -1, -1):
            self.commands[i].undo()

    def _check_commands(self, commands: list[Command]) -> None:
        number_of_reversible = self._calc_number_of_reversible(commands)
        number_of_unreversible = len(commands) - number_of_reversible
        for index, command in enumerate(commands[: -number_of_unreversible]):
            if not isinstance(command, ReversibleCommand):
                raise TransactExecutorException(
                    index=index,
                    message=f"Invalid order of passed commands.\n"
                            f"Unreversible command with {index = }"
                )
        return

    def _calc_number_of_reversible(self, commands: list[Command]) -> int:
        number = 0
        for command in commands:
            if isinstance(command, ReversibleCommand):
                number += 1
        return number
