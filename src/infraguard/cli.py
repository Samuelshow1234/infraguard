import typer

from infraguard.checks.disk import DiskAuditor
from infraguard.checks.memory import MemoryAuditor
from infraguard.checks.system import SystemAuditor
from infraguard.core.engine import AuditEngine
from infraguard.reporters.json_report import render_json
from infraguard.reporters.markdown import render_markdown
from infraguard.reporters.terminal import render_terminal

app = typer.Typer(
    name="infraguard",
    help="A lightweight infrastructure health auditing toolkit.",
    no_args_is_help=True,
)


@app.command()
def audit(
    output_format: str = typer.Option(
        "terminal",
        "--format",
        help="Output format: terminal, json, or markdown.",
    ),
) -> None:
    if output_format not in {"terminal", "json", "markdown"}:
        raise typer.BadParameter("Choose terminal, json, or markdown.")
    engine = AuditEngine([SystemAuditor(), MemoryAuditor(), DiskAuditor()])
    results = engine.run()
    if output_format == "json":
        typer.echo(render_json(results))
    elif output_format == "markdown":
        typer.echo(render_markdown(results))
    else:
        render_terminal(results)


if __name__ == "__main__":
    app()
