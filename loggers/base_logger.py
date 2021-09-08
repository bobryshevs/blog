import logging.config
from logging import Logger
from .settings import logger_config


class BaseLogger(object):
    def __init__(self, logger_config: dict = logger_config) -> None:
        logging.config.dictConfig(logger_config)
        self.debug_logger: Logger = logging.getLogger("base_debug_logger")
        self.info_logger: Logger = logging.getLogger("base_info_logger")
        self.warning_logger: Logger = logging.getLogger("base_warning_logger")
        self.error_logger: Logger = logging.getLogger("base_error_logger")
        self.critical_logger: Logger = logging.getLogger(
            "base_critical_logger")

        self.level_to_func: dict = self.get_level_to_function_dict()

    def debug(self, message) -> None:
        self.debug_logger.debug(message)

    def info(self, message) -> None:
        self.info_logger.info(message)

    def warning(self, message) -> None:
        self.warning_logger.warning(message)

    def error(self, message) -> None:
        self.error_logger.error(message)

    def critical(self, message) -> None:
        self.critical_logger.critical(message)

    def init_log(self, object_link, level="DEBUG"):
        self.level_to_func[level](f"The {object_link} has been initialized")

    def log(self, message, level="INFO"):
        self.level_to_func[level](message)

    def get_level_to_function_dict(self) -> dict:
        return {
            "DEBUG": self.debug,
            "INFO": self.info,
            "WARNING": self.warning,
            "ERROR": self.error,
            "CRITICAL": self.critical
        }
