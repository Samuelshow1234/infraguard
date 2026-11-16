from infraguard.core.results import AuditResult
from infraguard.reporters.json_report import render_json
from infraguard.reporters.markdown import render_markdown


def test_json_report():
    output = render_json([AuditResult("disk", "disk", "PASS", "OK")])
    assert '"name": "disk"' in output


def test_markdown_report():
    output = render_markdown([AuditResult("disk", "disk", "PASS", "OK")])
    assert "| disk | disk | PASS | OK |" in output
