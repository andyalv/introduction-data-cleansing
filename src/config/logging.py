import logging
from rich.logging import RichHandler


def start_logger(
    level: int = logging.INFO, datefmt: str = "[%X]", show_path: bool = True
) -> logging.Logger:
    logging.basicConfig(
        level=level,
        format="%(message)s",
        datefmt=datefmt,
        handlers=[RichHandler(omit_repeated_times=False, show_path=show_path)],
    )

    return logging.getLogger("rich")
