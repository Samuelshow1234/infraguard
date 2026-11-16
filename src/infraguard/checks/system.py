import platform

import psutil

from infraguard.core.results import AuditResult


class SystemAuditor:
    def run(self) -> list[AuditResult]:
        cpu = psutil.cpu_percent(interval=0.3)
        return [
            AuditResult(
                "hostname", "system", "PASS", f"Hostname: {platform.node()}", value=platform.node()
            ),
            AuditResult(
                "operating_system",
                "system",
                "PASS",
                f"Platform: {platform.system()} {platform.release()}",
                value=f"{platform.system()} {platform.release()}",
            ),
            AuditResult(
                "cpu_utilization",
                "system",
                "WARNING" if cpu >= 85 else "PASS",
                f"CPU utilization is {cpu:.1f}%.",
                value=cpu,
                threshold=85,
                recommendation="Investigate sustained high CPU usage." if cpu >= 85 else "",
            ),
        ]
