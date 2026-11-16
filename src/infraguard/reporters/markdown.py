from infraguard.core.results import AuditResult


def render_markdown(results: list[AuditResult]) -> str:
    lines = [
        "# InfraGuard Audit Report",
        "",
        "| Check | Category | Status | Result |",
        "|---|---|---|---|",
    ]
    for result in results:
        message = result.message.replace("|", "\\|")
        lines.append(f"| {result.name} | {result.category} | {result.status} | {message} |")
    return "\n".join(lines) + "\n"
