from src.config.logging import start_logger
from src.utils.sql import connect_to_db, execute_sql_commands, copy_expert
from src.utils.files import read_file
from src.paths import SQL_DIR, DATA_DIR


def import_dataset():
    log = start_logger()

    log.info("Importing dataset script...")
    conn = connect_to_db()

    # Paths to SQL scripts and CSV file
    temp_stage_table_sql_path = SQL_DIR / "temp_stage_table.sql"
    insert_imports_sql_path = SQL_DIR / "insert_imports.sql"
    copy_command_sql_path = SQL_DIR / "copy_command.sql"
    csv_file_path = DATA_DIR / "dataset_clientes_cafeteria.csv"

    # Execute 'temp_stage_table.sql' to create the temporary staging table
    execute_sql_commands(conn, read_file(temp_stage_table_sql_path))

    # Execute 'copy_command.sql' to load data from the CSV file into the staging table
    copy_expert(conn, read_file(copy_command_sql_path), csv_file_path)

    # Execute 'insert_imports.sql' to transfer data from the staging table to the main tables
    execute_sql_commands(conn, read_file(insert_imports_sql_path))

    log.info("Dataset imported successfully.")
    conn.close()


if __name__ == "__main__":
    import_dataset()
