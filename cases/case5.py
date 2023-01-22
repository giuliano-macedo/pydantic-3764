from ._imports import *

@pydantic_dataclass
class _Child:
    n: int


@pydantic_dataclass
class _Root:
    s: str
    c: _Child


class Case5(Case):
    info = CaseInfo(
        root_type="Pydantic dataclass",
        child_type="Pydantic dataclass",
        method="asdict(r)",
    )

    def run(self) -> Dict[str, Any]:
        return asdict(
            _Root(  # type: ignore
                s="test",
                c=_Child(n=2),  # type: ignore
            )
        )
