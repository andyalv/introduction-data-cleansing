import psycopg2
from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax

from src.config.settings import settings


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
    except Exception as e:
        raise Exception(f"Error executing SQL commands: {e}")
    finally:
        cursor.close()


# Print the provided SQL command in a formatted and visually appealing way using the rich library.
def print_sql_command(sql_command: str, title: str = "SQL Command") -> None:
    console = Console()
    syntax = Syntax(sql_command, "sql", theme="monokai", line_numbers=True)
    panel = Panel(syntax, title=title, border_style="blue")
    console.print(panel)
