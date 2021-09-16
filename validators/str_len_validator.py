

class StrLenValidator():
    def __init__(self, key: str, min_len=None, max_len=None) -> None:
        self.key = key
        self.min_len = min_len
        self.max_len = max_len

    def valid(self, args: dict) -> bool:
        '''[min_len, max_len] --> Including interval boundaries'''
        if not isinstance(args.get(self.key), str):
            return self.__skip()

        # (None, None)
        if self.min_len is None and self.max_len is None:
            return True

        # (int, None)
        if self.min_len is not None and self.max_len is None:
            return self.min_len <= len(args.get(self.key))

        # (None, int)
        if self.min_len is None and self.max_len is not None:
            return self.max_len >= len(args.get(self.key))

        # (int, int)
        return self.min_len <= len(args.get(self.key)) <= self.max_len

    def error(self) -> str:
        return \
            f"Error in [{self.key}]. Given value not in" \
            "[{self.min_len}, {self.max_len}]"

    def __skip(self):
        return True
