from bcrypt import (
    checkpw,
    hashpw,
    gensalt,
)


class BcryptWrapper:

    def gen_passwd_hash(self, passwd: str, salt: bytes = None) -> bytes:
        if salt is None:
            salt = self.gen_salt()
        return hashpw(passwd.encode(), salt)

    def check_passwd(self, passwd: str, passwd_hash: bytes) -> bool:
        return checkpw(
            password=passwd.encode("utf8"),
            hashed_password=passwd_hash
        )

    def gen_salt(self, rounds: int = 6) -> bytes:
        return gensalt(rounds)
