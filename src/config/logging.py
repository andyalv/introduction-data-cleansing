import logging
from rich.logging import RichHandler


def configure_logging(
    level: int = logging.DEBUG, datefmt: str = "[%X]", show_path: bool = True
) -> None:
    logging.basicConfig(
        level=level,
        format="%(message)s",
        datefmt=datefmt,
        handlers=[RichHandler(omit_repeated_times=False, show_path=show_path)],
        force=True,
    )


# Start logger with name "rich" and return the logger instance.
# The logger is configured with the specified logging level, date format, and whether to show the file path in log messages.
def start_logger(
    level: int = logging.DEBUG, datefmt: str = "[%X]", show_path: bool = True
) -> logging.Logger:
    configure_logging(level=level, datefmt=datefmt, show_path=show_path)
    return logging.getLogger("rich")
