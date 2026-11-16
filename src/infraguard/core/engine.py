from collections.abc import Iterable

from infraguard.core.auditor import Auditor
from infraguard.core.results import AuditResult


class AuditEngine:
    def __init__(self, auditors: Iterable[Auditor]) -> None:
        self.auditors = list(auditors)

    def run(self) -> list[AuditResult]:
        results: list[AuditResult] = []

        for auditor in self.auditors:
            try:
                results.extend(auditor.run())

            except Exception:  # noqa: BLE001
                results.append(
                    AuditResult(
                        name=auditor.__class__.__name__.lower(),
                        category="internal",
                        status="ERROR",
                        message="Audit check could not complete.",
                        recommendation="Review the application logs and platform support.",
                    )
                )

        return results
