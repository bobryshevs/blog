

class StrLenValidator():
    def __init__(self, key: str) -> None:
        self.key = key

    def valid(self, args: dict, min_len=None, max_len=None) -> bool:
        '''[min_len, max_len] --> Including interval boundaries'''
        if not isinstance(args.get(self.key), str):
            return self.__skip()

        if min_len is None and max_len is None:  # (None, None)
            return True

        if min_len is not None and max_len is None:  # (int, None)
            return min_len <= len(args.get(self.key))

        if min_len is None and max_len is not None:  # (None, int)
            return max_len <= len(args.get(self.key))

        return min_len <= len(args.get(self.key)) <= max_len  # (int, int)

    def __skip(self):
        return True
