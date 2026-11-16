import psutil

from infraguard.core.results import AuditResult


class DiskAuditor:
    def __init__(self, warning_threshold: float = 85.0) -> None:
        self.warning_threshold = warning_threshold

    def run(self) -> list[AuditResult]:
        results = []
        for partition in psutil.disk_partitions(all=False):
            try:
                usage = psutil.disk_usage(partition.mountpoint)
            except (PermissionError, OSError):
                continue
            status = "WARNING" if usage.percent >= self.warning_threshold else "PASS"
            results.append(
                AuditResult(
                    f"disk_usage:{partition.mountpoint}",
                    "disk",
                    status,
                    f"{partition.mountpoint} is {usage.percent:.1f}% used.",
                    value=round(usage.percent, 1),
                    threshold=self.warning_threshold,
                    recommendation=f"Investigate disk usage on {partition.mountpoint}."
                    if status == "WARNING"
                    else "",
                )
            )
        if not results:
            results.append(
                AuditResult(
                    "disk_usage",
                    "disk",
                    "INFO",
                    "No accessible mounted filesystems were found.",
                )
            )
        return results
