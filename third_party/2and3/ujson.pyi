# Stubs for ujson
# See: https://pypi.python.org/pypi/ujson
from typing import Any, IO, Optional

__version__ = ...  # type: str

def encode(obj: Any,
    ensure_ascii: bool = ...,
    double_precision: bool = ...,
    encode_html_chars: bool = ...,
    escape_forward_slashes: bool = ...,
    sort_keys: bool = ...,
    indent: int = ...,
    ) -> str: ...

def dumps(obj: Any,
    ensure_ascii: bool = ...,
    double_precision: bool = ...,
    encode_html_chars: bool = ...,
    escape_forward_slashes: bool = ...,
    sort_keys: bool = ...,
    indent: int = ...,
    ) -> str: ...

def dump(obj: Any,
    fp: IO[str],
    ensure_ascii: bool = ...,
    double_precision: bool = ...,
    encode_html_chars: bool = ...,
    escape_forward_slashes: bool = ...,
    sort_keys: bool = ...,
    indent: int = ...,
    ) -> None: ...

def decode(s: str,
    precise_float: bool = ...,
    ) -> Any: ...

def loads(s: str,
    precise_float: bool = ...,
    ) -> Any: ...

def load(fp: IO[str],
    precise_float: bool = ...,
    ) -> Any: ...
