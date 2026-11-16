import json

from infraguard.core.results import AuditResult


def render_json(results: list[AuditResult]) -> str:
    return json.dumps([result.to_dict() for result in results], indent=2)
