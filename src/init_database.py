import logging

from utils.files import read_file
from utils.sql import (
    connect_to_db,
    execute_sql_commands,
)
from paths import SQL_DIR

logger = logging.getLogger(__name__)


def initialize_database():
    logger.info("Initializing database...")

    # init.sql file path
    init_sql_file_path = SQL_DIR / "init.sql"
    sql_commands = read_file(init_sql_file_path)

    execute_sql_commands(connect_to_db(), sql_commands)
    logger.info("Database initialized successfully.")


if __name__ == "__main__":
    initialize_database()
