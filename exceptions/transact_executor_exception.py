class TransactExecutorException(Exception):
    def __init__(self, index: int, message: str) -> None:
        super().__init__(message)
        self.index = index
