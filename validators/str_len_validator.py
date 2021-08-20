

class StrLenValidator():
    def __init__(self, key: str) -> None:
        self.key = key

    def valid(self, args: dict, min_len=None, max_len=None) -> bool:
        '''[min_len, max_len] --> Including interval boundaries'''
        if min_len is None and max_len is None:
            return True

        if max_len is not None:
            return min_len <= len(args.get(self.key)) <= max_len

        return min_len <= len(args.get(self.key))
