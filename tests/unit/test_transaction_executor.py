import pytest
from mock import Mock
from commands import (
    ReversibleCommand,
    Command
)
import exceptions
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
