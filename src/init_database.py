from src.config.logging import start_logger
from src.utils.files import read_file
from src.utils.sql import (
    connect_to_db,
    execute_sql_commands,
)
from src.paths import SQL_DIR


def initialize_database():
    log = start_logger()
    log.info("Initializing database...")

    # init.sql file path
    init_sql_file_path = SQL_DIR / "init.sql"
    sql_commands = read_file(init_sql_file_path)

    execute_sql_commands(connect_to_db(), sql_commands)
    log.info("Database initialized successfully.")


if __name__ == "__main__":
    initialize_database()
