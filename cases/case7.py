from ._imports import *


class _Child(BaseModel):
    n: int


@dataclass
class _Root:
    s: str
    c: _Child


class Case7(Case):
    info = CaseInfo(
        root_type="dataclass",
        child_type="BaseModel",
        method="asdict(r)",
    )

    def run(self) -> Dict[str, Any]:
        return asdict(
            _Root(
                s="test",
                c=_Child(n=2),
            )
        )
