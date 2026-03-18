from src.config.logging import start_logger
from src.utils.sql import connect_to_db, copy_expert
from src.paths import DATA_DIR, PROJECT_ROOT


def export_database():
    log = start_logger()
    tables = ["clientes", "visitas_mensuales", "compra_restaurante"]

    for table in tables:
        log.info(f"Exporting table '{table}' to CSV...")
        file_path = DATA_DIR / "export" / f"{table}.csv"
        copy_expert(
            connect_to_db(), f"COPY {table} TO STDOUT WITH CSV HEADER", file_path
        )
        log.info(
            f"Table '{table}' exported successfully to '{file_path.relative_to(PROJECT_ROOT)}'"
        )

    log.info("All tables exported successfully.")


if __name__ == "__main__":
    export_database()
