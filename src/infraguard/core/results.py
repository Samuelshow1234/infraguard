from dataclasses import asdict, dataclass
from typing import Any


@dataclass
class AuditResult:
    name: str
    category: str
    status: str
    message: str
    value: Any = None
    threshold: Any = None
    recommendation: str = ""

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
