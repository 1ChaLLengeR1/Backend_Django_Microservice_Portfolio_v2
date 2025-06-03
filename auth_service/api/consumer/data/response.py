from typing import TypedDict, Union, Dict, Any, List, Literal, Optional

type_module = Literal['user']
type_error = Literal[
    'not_found', 'missing_fields', 'missing_headers', 'critical', 'expectation_failed', 'not_valid',
    'permission', 'unique',
]


class Error(TypedDict, total=True):
    message: str
    type_module: type_module
    type_error: type_error
