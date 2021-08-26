class Command:

    def do(self, *args, **kwargs) -> None:
        raise NotImplementedError()


class ReversibleCommand(Command):
    def undo(*args, **kwargs):
        raise NotImplementedError()
