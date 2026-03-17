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


def copy_expert(
    conn: psycopg2.extensions.connection, sql_command: str, file_path: Path
) -> None:
    try:
        validate_file_path(file_path)
        display_path = file_path.relative_to(PROJECT_ROOT)

        cursor = conn.cursor()
        content = read_file(file_path)
        cursor.copy_expert(sql_command, StringIO(content))
        conn.commit()
        display_code_block(sql_command, lexer="sql", title="COPY Command Executed")
        display_code_block(
            code=content,
            limit_code_lines=10,
            lexer="text",
            title=f"Data Copied from {display_path}",
        )
        logger.info(f"Data copied successfully from {display_path}")
    except Exception as e:
        logger.error(f"Error copying data from {file_path}: {e}")
        raise Exception(f"Error copying data from {file_path}: {e}")
    finally:
        cursor.close()
