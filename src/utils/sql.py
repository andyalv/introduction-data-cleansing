from io import StringIO
import logging
from pathlib import Path

import psycopg2

from src.config.settings import settings
from src.paths import PROJECT_ROOT
from src.utils.files import read_file, validate_file_path
from src.utils.render import display_code_block

logger = logging.getLogger(__name__)


# Connect to the PostgreSQL database using the provided connection parameters and return the connection object
def connect_to_db():
    return psycopg2.connect(
        host=settings.PGHOST,
        port=settings.PGPORT,
        dbname=settings.PGDATABASE,
        user=settings.PGUSER,
        password=settings.PGPASSWORD,
    )


# Execute the provided SQL commands using the given database connection.
# If an error occurs during execution, it raises an exception.
# Finally, it ensures that the cursor is closed after execution.
def execute_sql_commands(
    conn: psycopg2.extensions.connection, sql_commands: str
) -> None:
    try:
        cursor = conn.cursor()
        cursor.execute(sql_commands)
        conn.commit()
        display_code_block(sql_commands, lexer="sql", title="Commands Executed")
        logger.info("SQL commands executed successfully")
    except Exception as e:
        logger.error(f"Error executing SQL commands: {e}")
        raise Exception(f"Error executing SQL commands: {e}")
    finally:
        cursor.close()


# Copies data from a file to a PostgreSQL database using the COPY command.
# It validates the file path, reads the content of the file, and executes the COPY command using a cursor.
# If any error occurs during the process, it raises an exception with a descriptive message.
# Finally, it ensures that the cursor is closed after execution.
def copy_expert(
    conn: psycopg2.extensions.connection, sql_command: str, file_path: Path
) -> None:
    if "STDOUT" in sql_command.upper():
        copy_expert_to_stdout(conn, sql_command, file_path)
    elif "STDIN" in sql_command.upper():
        copy_expert_to_stdin(conn, sql_command, file_path)
    else:
        raise ValueError("SQL command must contain either STDOUT or STDIN.")


def copy_expert_to_stdin(
    conn: psycopg2.extensions.connection, sql_command: str, file_path: Path
) -> None:
    try:
        validate_file_path(file_path)
        display_path = file_path.relative_to(PROJECT_ROOT)

        file_content = read_file(file_path)
        cursor = conn.cursor()
        cursor.copy_expert(sql_command, StringIO(file_content))

        conn.commit()

        display_code_block(sql_command, lexer="sql", title="COPY Command Executed")
        logger.info(f"Data imported successfully from '{display_path}'")
    except Exception as e:
        logger.error(f"Error copying data from '{file_path}': {e}")
        raise Exception(f"Error copying data from '{file_path}': {e}")
    finally:
        cursor.close()


def copy_expert_to_stdout(
    conn: psycopg2.extensions.connection, sql_command: str, file_path: Path
) -> None:
    try:
        cursor = conn.cursor()

        with open(file_path, "w", encoding="utf-8") as f:
            cursor.copy_expert(sql_command, f)

        conn.commit()
        display_code_block(sql_command, lexer="sql", title="COPY Command Executed")

        display_path = file_path.relative_to(PROJECT_ROOT)
        logger.info(f"Data exported successfully to '{display_path}'")
    except Exception as e:
        logger.error(f"Error copying data to '{file_path}': {e}")
        raise Exception(f"Error copying data to '{file_path}': {e}")
    finally:
        cursor.close()
