from typing import Any

__all__ = ("is_ellipsis",)


def is_ellipsis(value: Any) -> bool:
    return isinstance(value, type(...))
