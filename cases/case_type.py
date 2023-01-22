from dataclasses import dataclass
from typing import Any, Dict, Protocol

@dataclass
class CaseInfo:
    root_type: str
    child_type: str
    method: str

class Case(Protocol):
    info: CaseInfo

    def run(self) -> Dict[str, Any]:
        ...
