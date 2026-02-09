from rich.console import Console
from rich.table import Table

def display_output(title, rows):
    table = Table(title=title,leading=1)
    table.add_column("Tag", justify="right", style="#61afef", no_wrap=True)
    table.add_column("Command", style="#a4d482", no_wrap=True)
    table.add_column("Description", style="#d4ddee")
    for r in rows:
        table.add_row(r[1],r[2], r[3])
    console = Console()
    console.print(table)
    