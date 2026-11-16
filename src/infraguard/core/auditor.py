from typing import Protocol

from infraguard.core.results import AuditResult


class Auditor(Protocol):
    def run(self) -> list[AuditResult]: ...
