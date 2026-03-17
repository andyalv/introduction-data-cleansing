import logging

import psycopg2

from src.config.settings import settings
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
