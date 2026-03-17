import logging
from pathlib import Path

from src.paths import PROJECT_ROOT

logger = logging.getLogger(__name__)


# Read a string from a file and return it.
# If the file is empty or an error occurs during reading, it raises an exception.
def read_file(file_path: Path) -> str:
    try:
        # Ensure the file exists before attempting to read it by validating the file path.
        #  This will raise a FileNotFoundError if the file does not exist, which we can catch and log appropriately.
        validate_file_path(file_path)
        display_path = file_path.relative_to(
            PROJECT_ROOT
        )  # Relative path for logging purposes

        # Read the content of the file as a string
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

    # Ensure that any OSError (e.g., file not found, permission issues) is caught and logged, and then re-raised with a descriptive message.
    except OSError as e:
        logger.exception(f"Error reading file at '{display_path}': {e}")
        raise OSError(f"Error reading file at '{display_path}': {e}") from e

    # Catch any other unexpected exceptions that may occur during file reading, log them, and re-raise with a descriptive message.
    except Exception as e:
        logger.exception(f"Unexpected error reading file at '{display_path}': {e}")
        raise Exception(
            f"Unexpected error reading file at '{display_path}': {e}"
        ) from e

    # If the content is empty (only whitespace), raise an exception
    if not content.strip():
        logger.error(f"File at '{display_path}' is empty")
        raise ValueError(f"File at '{display_path}' is empty")

    logger.debug(
        f"File at '{display_path}' read successfully with {len(content)} characters"
    )

    return content


# Validate that a file exists at the given path. If it does, return the path; otherwise, raise a FileNotFoundError.
# Logging is optional; if a logger is provided, it will log the error or success messages.
def validate_file_path(file_path: Path) -> None:
    display_path = file_path.relative_to(PROJECT_ROOT)

    if not file_path.exists():
        logger.error("File not found at '%s'", display_path)
        raise FileNotFoundError(f"File not found at '{display_path}'")

    logger.debug("File found at '%s'", display_path)

    return None
