import pytest
from mock import Mock
from commands import (
    ReversibleCommand,
    Command
)
from transaction_executor import TransactionExecutor
from exceptions import TransactExecutorException


class TestTransactionExecutor:
    def setup(self):
        # _r --> reversible
        # _c --> cmd
        self.cmd_1_r = Mock()
        self.cmd_2_r = Mock()
        self.cmd_3_r = Mock()
        self.cmd_4_c = Mock()
        self.cmd_5_c = Mock()

        self.cmd_1_r.__class__ = ReversibleCommand
        self.cmd_2_r.__class__ = ReversibleCommand
        self.cmd_3_r.__class__ = ReversibleCommand
        self.cmd_4_c.__class__ = Command
        self.cmd_5_c.__class__ = Command

    def test__calc_number_of_reversible(self):
        command_dict = {
            1: [self.cmd_1_r, self.cmd_4_c, self.cmd_5_c],
            2: [self.cmd_1_r, self.cmd_2_r, self.cmd_4_c],
            3: [self.cmd_1_r, self.cmd_2_r, self.cmd_3_r]
        }

        for number, commands in command_dict.items():
            executor = TransactionExecutor(commands)
            assert executor._calc_number_of_reversible(commands) == number

    def test__check_commands_without_exception(self):
        commands = [self.cmd_1_r, self.cmd_4_c, self.cmd_5_c]  # OK-ORDER
        executor = TransactionExecutor([])
        executor._calc_number_of_reversible = Mock()
        executor._calc_number_of_reversible.return_value = 1

        executor._check_commands(commands)

        executor._calc_number_of_reversible.assert_called_once_with(commands)

    def test__check_commands_with_exception(self):
        commands = [
            self.cmd_1_r, self.cmd_4_c, self.cmd_2_r, self.cmd_4_c  # BAD-ORDER
        ]
        executor = TransactionExecutor([])
        executor._calc_number_of_reversible = Mock()
        executor._calc_number_of_reversible.return_value = 2

        with pytest.raises(TransactExecutorException) as err:
            executor._check_commands(commands)

        assert err.value.index == 1

    def test_execute_without_exception(self):
        commands = [self.cmd_1_r, self.cmd_2_r, self.cmd_3_r, self.cmd_4_c]
        executor = TransactionExecutor(commands)
        model = Mock()

        executor.execute(model)

        for command in commands:
            command.do.assert_called_once_with(model)

    def test_execute_with_exception(self):
        self.cmd_1_r.do.side_effect = Exception("something went wrong")
        commands = [self.cmd_1_r]
        executor = TransactionExecutor(commands)
        model = Mock()

        with pytest.raises(TransactExecutorException):
            executor.execute(model)

        for command in commands:
            command.do.assert_called_once_with(model)

    def test_rollback_call(self):
        commands = [self.cmd_1_r, self.cmd_2_r, self.cmd_3_r, self.cmd_4_c]
        index = 2
        commands[index].do.side_effect = Exception()
        executor = TransactionExecutor(commands)
        model = Mock()

        executor.rollback = Mock()

        with pytest.raises(TransactExecutorException):
            executor.execute(model)

        for command in commands[:index]:
            command.do.assert_called_once_with(model)

        for command in commands[index:]:
            command.assert_not_called()

        executor.rollback.assert_called_once_with(index=index)

    def test_rollback_reversible_commands(self):
        commands = [self.cmd_1_r, self.cmd_2_r, self.cmd_3_r]
        index = 2
        commands[index].do_side_effect = Exception()
        executor = TransactionExecutor(commands)

        executor.rollback(index=index)

        for command in commands[:index + 1]:
            command.undo.assert_called_once()

    def test_rollback_uwith_nreversible_commands(self):
        commands = [self.cmd_1_r, self.cmd_2_r, self.cmd_4_c, self.cmd_5_c]
        index_first_unreversible = 2
        index = 3
        executor = TransactionExecutor(commands)

        err_messages = executor.rollback(index)
        err_messages.reverse()

        for i, err in enumerate(err_messages):
            assert err == str(commands[index_first_unreversible + i])
