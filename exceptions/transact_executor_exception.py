class TransactExecutorException(Exception):
    def __init__(self, message: str, index: int = None) -> None:
        super().__init__(message)
        self.index = index
