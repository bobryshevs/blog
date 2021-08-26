from commands import Command
from exceptions import TransactExecutorException


class TransactionExecutor:
    def __init__(self, commands: list[Command]) -> None:
        self.commands: list[Command] = commands

    def execute(self):
        for i, command in enumerate(self.commands):
            try:
                command.do()
            except Exception as err:
                self.rollback(index=i)
                TransactExecutorException(str(err))

    def rollback(self, index: int):
        for i in range(index, -1, -1):
            self.commands[i].undo()
