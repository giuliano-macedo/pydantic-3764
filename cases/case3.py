from ._imports import *


@dataclass
class _Child:
    n: int


class _Root(BaseModel):
    s: str
    c: _Child


class Case3(Case):
    info = CaseInfo(
        root_type="BaseModel",
        child_type="dataclass",
        method="r.dict()",
    )

    def run(self) -> Dict[str, Any]:
        return _Root(
            s="test",
            c=_Child(n=2),
        ).dict()
