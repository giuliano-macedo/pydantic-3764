from ._imports import *


@pydantic_dataclass
class _Child:
    n: int


@dataclass
class _Root:
    s: str
    c: _Child


class Case8(Case):
    info = CaseInfo(
        root_type="dataclass",
        child_type="Pydantic dataclass",
        method="asdict(r)",
    )

    def run(self) -> Dict[str, Any]:
        return asdict(
            _Root(
                s="test",
                c=_Child(n=2),  # type: ignore
            )
        )
