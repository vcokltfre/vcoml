from textwrap import indent
from typing import Any


def _padded(func):
    def deco(obj: Any, *, level: int = 0) -> str:
        pad = "  " * level
        return indent(func(obj, level=level), pad)
    return deco

@_padded
def pack(obj: Any, *, level: int = 0) -> str:
    if isinstance(obj, bool):
        return "ya" if obj else "na"
    elif isinstance(obj, str):
        val = obj.replace('"', '\\"')
        return f'"{val}"'
    elif obj is None:
        return "idk"
    elif isinstance(obj, (int, float)):
        return str(obj)

    elif isinstance(obj, dict):
        blocks = []

        for key, value in obj.items():
            block = f":{pack(key)}\n"
            block += pack(value, level=1)

            blocks.append(block)

        return "\n".join(blocks)

    elif isinstance(obj, (list, tuple)):
        blocks = []

        for value in obj:
            block = ">\n"
            block += pack(value, level=1)

            blocks.append(block)

        return "\n".join(blocks)

    return ""
