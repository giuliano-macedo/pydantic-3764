from ._imports import *


class _Child(BaseModel):
    n: int


class _Root(BaseModel):
    s: str
    c: _Child


class Case1(Case):
    info = CaseInfo(
        root_type="BaseModel",
        child_type="BaseModel",
        method="r.dict()",
    )

    def run(self) -> Dict[str, Any]:
        return _Root(
            s="test",
            c=_Child(n=2),
        ).dict()
