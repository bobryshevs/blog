from .command import Command


class ReversibleCommand(Command):
    def undo(*args, **kwargs):
        raise NotImplementedError()
