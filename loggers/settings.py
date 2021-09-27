
logger_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "BaseJsonFormatter": {
            "()": "pythonjsonlogger.jsonlogger.JsonFormatter",
            "format": "%(asctime)s %(levelname)s %(name)s %(message)s"
        }
    },

    "handlers": {
        "base_debug_console_handler": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "BaseJsonFormatter"
        },
        "base_info_console_handler": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "BaseJsonFormatter"
        },
        "base_warning_console_handler": {
            "class": "logging.StreamHandler",
            "level": "WARNING",
            "formatter": "BaseJsonFormatter"
        },
        "base_error_console_handler": {
            "class": "logging.StreamHandler",
            "level": "ERROR",
            "formatter": "BaseJsonFormatter"
        },
        "base_critical_console_handler": {
            "class": "logging.StreamHandler",
            "level": "CRITICAL",
            "formatter": "BaseJsonFormatter"
        },
        "base_debug_file_handler": {
            "class": "logging.FileHandler",
            "filename": "./logs/debug.log",
            "mode": "w",
            "level": "DEBUG",
            "formatter": "BaseJsonFormatter"
        },
        "base_info_file_handler": {
            "class": "logging.FileHandler",
            "filename": "./logs/info.log",
            "mode": "w",
            "level": "INFO",
            "formatter": "BaseJsonFormatter"
        },
        "base_warning_file_handler": {
            "class": "logging.FileHandler",
            "filename": "./logs/warning.log",
            "mode": "w",
            "level": "WARNING",
            "formatter": "BaseJsonFormatter"
        },
        "base_error_file_handler": {
            "class": "logging.FileHandler",
            "filename": "./logs/error.log",
            "mode": "w",
            "level": "ERROR",
            "formatter": "BaseJsonFormatter"
        },
        "base_critical_file_handler": {
            "class": "logging.FileHandler",
            "filename": "./logs/critical.log",
            "mode": "w",
            "level": "CRITICAL",
            "formatter": "BaseJsonFormatter"
        },
    },
    "loggers": {
        "base_debug_logger": {
            "level": "DEBUG",
            "handlers": ["base_debug_console_handler",
                         "base_debug_file_handler"]
        },
        "base_info_logger": {
            "level": "INFO",
            "handlers": ["base_info_console_handler",
                         "base_info_file_handler"]
        },
        "base_warning_logger": {
            "level": "WARNING",
            "handlers": ["base_warning_console_handler",
                         "base_warning_file_handler"]
        },
        "base_error_logger": {
            "level": "ERROR",
            "handlers": ["base_error_console_handler",
                         "base_error_file_handler"]
        },
        "base_critical_logger": {
            "level": "CRITICAL",
            "handlers": ["base_critical_console_handler",
                         "base_critical_file_handler"]
        }
    }
}
