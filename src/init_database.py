from pathlib import Path

from config.logging import start_logger
from utils.files import get_str_from_file
from utils.sql import (
    connect_to_db,
    execute_sql_commands,
    print_sql_command,
)


def main():
    log = start_logger()

    log.info("Initializing script...")

    # Get SQL commands from file
    sql_file_path = Path(__file__).parent / "sql" / "init.sql"
    sql_commands = get_str_from_file(sql_file_path)

    # Debug: Print the SQL commands to be executed
    print_sql_command(sql_commands, title=f"SQL Command from {sql_file_path.name}")

    # Execute SQL commands
    execute_sql_commands(connect_to_db(), sql_commands)
    log.info("Database initialized successfully.")


if __name__ == "__main__":
    main()
