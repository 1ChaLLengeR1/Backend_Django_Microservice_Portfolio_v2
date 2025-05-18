from typing import TypedDict, Union, Dict, Any, List, Literal


class RepositoryOneUserByLoginPasswordInput(TypedDict, total=True):
    login: str
    password: str


class RepositoryOneUserByLoginPasswordOutput(TypedDict, total=True):
    id: str
    login: str
    last_login: str
    created_at: str
