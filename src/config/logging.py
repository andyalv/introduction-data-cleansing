import logging
from rich.logging import RichHandler


def start_logger(level: int = logging.INFO, datefmt: str = "[%X]") -> logging.Logger:
    logging.basicConfig(
        level=level,
        format="%(message)s",
        datefmt=datefmt,
        handlers=[RichHandler(omit_repeated_times=False, show_path=True)],
    )

    return logging.getLogger("rich")
