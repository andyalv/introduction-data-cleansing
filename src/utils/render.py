from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from rich.table import Table


# Print the provided code block in a formatted and visually appealing way using the rich library.
def display_code_block(
    code: str, lexer: str, title: str = "Code Block", limit_code_lines: int = None
) -> None:
    # If limit_code_lines is set and the code has more lines than the limit, truncate the code and add a note about truncation.
    if limit_code_lines and len(code.splitlines()) > limit_code_lines:
        code_lines = code.splitlines()
        code = f"{'\n'.join(code_lines[:limit_code_lines])}\n... (truncated {len(code_lines) - limit_code_lines} lines)"

    console = Console()
    syntax = Syntax(code, lexer=lexer, theme="monokai", line_numbers=True)
    panel = Panel(syntax, title=title, border_style="blue")
    console.print(panel)
