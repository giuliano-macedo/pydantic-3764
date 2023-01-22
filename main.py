from dataclasses import asdict, dataclass
from typing import List
from cases.cases import cases
from tabulate import TableFormat, tabulate


@dataclass
class _PrintInfo:
    root_type: str
    child_type: str
    method: str
    output: str
    returned_expected_output: str


def main() -> None:
    print_infos: List[_PrintInfo] = []
    for case in cases:
        output = case.run()
        returned_expected_output = "_Pydantic__Child" not in repr(output)

        print_infos.append(
            _PrintInfo(
                root_type=case.info.root_type,
                child_type=case.info.child_type,
                method=case.info.method,
                output=repr(output),
                returned_expected_output=["No", "Yes"][int(returned_expected_output)],
            )
        )
    
    print(
        tabulate(
            [asdict(p) for p in print_infos],
            headers={
                "root_type": "Root type",
                "child_type": "Child type",
                "method": "method",
                "output": "output",
                "returned_expected_output": "returned expected output?",
            },
            tablefmt="github",
        )
    )


if __name__ == "__main__":
    main()
