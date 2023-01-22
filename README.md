## Pydantic issue 3764 - Basemodel.dict not converting std python dataclasses children
This repo contains example code for the issue [pydantic#3764](https://github.com/pydantic/pydantic/issues/3764)


# pre-requisites
* python
* pyenv
* pipenv
* make

# Installing
```
pipenv install -d
```

# Running
make run_pydantic_1.9.0
make run_pydantic_1.9.2
make run_pydantic_1.10.0

# Results

## pydantic 1.9.0

make run_pydantic_1.9.0
pipenv install pydantic==1.9.0 >/dev/null 2>&1 && pipenv run python main.py
| Root type          | Child type         | method    | output                                                   | returned expected output?   |
|--------------------|--------------------|-----------|----------------------------------------------------------|-----------------------------|
| BaseModel          | BaseModel          | r.dict()  | {'s': 'test', 'c': {'n': 2}}                             | Yes                         |
| BaseModel          | Pydantic dataclass | r.dict()  | {'s': 'test', 'c': _Child(n=2)}                          | Yes                         |
| BaseModel          | dataclass          | r.dict()  | {'s': 'test', 'c': _Pydantic__Child_93938887786864(n=2)} | No                          |
| Pydantic dataclass | BaseModel          | asdict(r) | {'s': 'test', 'c': _Child(n=2)}                          | Yes                         |
| Pydantic dataclass | Pydantic dataclass | asdict(r) | {'s': 'test', 'c': {'n': 2}}                             | Yes                         |
| Pydantic dataclass | dataclass          | asdict(r) | {'s': 'test', 'c': {'n': 2}}                             | Yes                         |
| dataclass          | BaseModel          | asdict(r) | {'s': 'test', 'c': _Child(n=2)}                          | Yes                         |
| dataclass          | Pydantic dataclass | asdict(r) | {'s': 'test', 'c': {'n': 2}}                             | Yes                         |
| dataclass          | dataclass          | asdict(r) | {'s': 'test', 'c': {'n': 2}}                             | Yes                         |

## pydantic 1.9.2

make run_pydantic_1.9.2
pipenv install pydantic==1.9.2 >/dev/null 2>&1 && pipenv run python main.py
| Root type          | Child type         | method    | output                                                   | returned expected output?   |
|--------------------|--------------------|-----------|----------------------------------------------------------|-----------------------------|
| BaseModel          | BaseModel          | r.dict()  | {'s': 'test', 'c': {'n': 2}}                             | Yes                         |
| BaseModel          | Pydantic dataclass | r.dict()  | {'s': 'test', 'c': _Child(n=2)}                          | Yes                         |
| BaseModel          | dataclass          | r.dict()  | {'s': 'test', 'c': _Pydantic__Child_94812215630720(n=2)} | No                          |
| Pydantic dataclass | BaseModel          | asdict(r) | {'s': 'test', 'c': _Child(n=2)}                          | Yes                         |
| Pydantic dataclass | Pydantic dataclass | asdict(r) | {'s': 'test', 'c': {'n': 2}}                             | Yes                         |
| Pydantic dataclass | dataclass          | asdict(r) | {'s': 'test', 'c': {'n': 2}}                             | Yes                         |
| dataclass          | BaseModel          | asdict(r) | {'s': 'test', 'c': _Child(n=2)}                          | Yes                         |
| dataclass          | Pydantic dataclass | asdict(r) | {'s': 'test', 'c': {'n': 2}}                             | Yes                         |
| dataclass          | dataclass          | asdict(r) | {'s': 'test', 'c': {'n': 2}}                             | Yes                         |

## pydantic 1.10.0

make run_pydantic_1.10.0
pipenv install pydantic==1.10.0 >/dev/null 2>&1 && pipenv run python main.py
| Root type          | Child type         | method    | output                          | returned expected output?   |
|--------------------|--------------------|-----------|---------------------------------|-----------------------------|
| BaseModel          | BaseModel          | r.dict()  | {'s': 'test', 'c': {'n': 2}}    | Yes                         |
| BaseModel          | Pydantic dataclass | r.dict()  | {'s': 'test', 'c': _Child(n=2)} | Yes                         |
| BaseModel          | dataclass          | r.dict()  | {'s': 'test', 'c': _Child(n=2)} | Yes                         |
| Pydantic dataclass | BaseModel          | asdict(r) | {'s': 'test', 'c': _Child(n=2)} | Yes                         |
| Pydantic dataclass | Pydantic dataclass | asdict(r) | {'s': 'test', 'c': {'n': 2}}    | Yes                         |
| Pydantic dataclass | dataclass          | asdict(r) | {'s': 'test', 'c': {'n': 2}}    | Yes                         |
| dataclass          | BaseModel          | asdict(r) | {'s': 'test', 'c': _Child(n=2)} | Yes                         |
| dataclass          | Pydantic dataclass | asdict(r) | {'s': 'test', 'c': {'n': 2}}    | Yes                         |
| dataclass          | dataclass          | asdict(r) | {'s': 'test', 'c': {'n': 2}}    | Yes                         |