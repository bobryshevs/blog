from bcrypt import (
    hashpw,
    gensalt,
)


class BcryptWrapper:

    def gen_password_hash(self, passwd: str, salt: bytes = None) -> bytes:
        if salt is None:
            salt = self.gen_salt()
        return hashpw(passwd.encode(), salt)

    def gen_salt(self, rounds: int = 6) -> bytes:
        return gensalt(rounds)
