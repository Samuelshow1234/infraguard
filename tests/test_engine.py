from infraguard.core.engine import AuditEngine
from infraguard.core.results import AuditResult


class GoodAuditor:
    def run(self):
        return [AuditResult("example", "test", "PASS", "It works.")]


class BrokenAuditor:
    def run(self):
        raise RuntimeError("simulated failure")


def test_engine_collects_results():
    results = AuditEngine([GoodAuditor()]).run()
    assert len(results) == 1
    assert results[0].status == "PASS"


def test_failed_auditor_does_not_stop_engine():
    results = AuditEngine([BrokenAuditor(), GoodAuditor()]).run()
    assert [r.status for r in results] == ["ERROR", "PASS"]
