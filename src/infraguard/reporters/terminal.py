from rich.console import Console
from rich.table import Table

from infraguard.core.results import AuditResult


def render_terminal(results: list[AuditResult]) -> None:
    table = Table(title="InfraGuard Audit Report")
    table.add_column("Check", style="cyan")
    table.add_column("Status")
    table.add_column("Result")
    styles = {
        "PASS": "green",
        "WARNING": "yellow",
        "CRITICAL": "red",
        "ERROR": "red",
        "INFO": "blue",
    }
    for result in results:
        style = styles.get(result.status, "white")
        table.add_row(result.name, f"[{style}]{result.status}[/{style}]", result.message)
    console = Console()
    console.print(table)
    counts = {
        s: sum(r.status == s for r in results)
        for s in ("PASS", "WARNING", "CRITICAL", "ERROR", "INFO")
    }
    console.print("  ".join(f"{k}: {v}" for k, v in counts.items() if v))
