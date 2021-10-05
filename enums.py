from enum import IntEnum


class TokenType(IntEnum):
    ACCESS = 1
    REFRESH = 2


class TimeConstants(IntEnum):
    SECOND = 1
    MINUTE = 60
    QUARTER_OF_AN_HOUR = 900
    HOUR = 3600
    DAY = 86400
    MOUNTH = 2592000  # 30 days
