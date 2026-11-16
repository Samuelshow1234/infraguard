import psutil

from infraguard.core.results import AuditResult


class MemoryAuditor:
    def __init__(self, warning_threshold: float = 85.0) -> None:
        self.warning_threshold = warning_threshold

    def run(self) -> list[AuditResult]:
        memory = psutil.virtual_memory()
        status = "WARNING" if memory.percent >= self.warning_threshold else "PASS"
        return [
            AuditResult(
                "memory_utilization",
                "system",
                status,
                f"Memory utilization is {memory.percent:.1f}%.",
                value=round(memory.percent, 1),
                threshold=self.warning_threshold,
                recommendation="Investigate memory-consuming processes."
                if status == "WARNING"
                else "",
            )
        ]
