from typing import TYPE_CHECKING, Any

__all__ = ("is_ellipsis", "EllipsisType",)

if TYPE_CHECKING:
    import builtins
    EllipsisType = builtins.ellipsis
else:
    EllipsisType = Any


def is_ellipsis(value: Any) -> bool:
    return isinstance(value, type(...))
