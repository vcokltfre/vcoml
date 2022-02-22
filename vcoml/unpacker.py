from textwrap import dedent, indent
from typing import Any
from re import compile
from random import randint


STRING = compile(r'^"(?P<content>(\\"|[^"])+)"$')
INTEGER = compile(r'^\d+$')
FLOAT = compile(r'^\d+\.\d+$')


class ParsingError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


def _get_identifier(value: str) -> str | int | float:
    if match := STRING.search(value):
        return match.group("content")
    elif match := INTEGER.search(value):
        return int(match.group())
    elif match := FLOAT.search(value):
        return float(match.group())

    raise ParsingError(f"Invalid identifier: {value}")

def _get_blocks(code: str, sym: str) -> list[str]:
    lines = code.split("\n")
    line = 0

    blocks = []
    block = ""

    while True:
        _line = lines[line]

        if _line.startswith(sym):
            if block:
                blocks.append(block)
                block = ""

            block += _line + "\n"
        elif _line:
            block += _line + "\n"

        line += 1

        if line >= len(lines):
            if block:
                blocks.append(block)

            break

    return blocks

def unpack(code: str) -> Any:
    code = code.strip()

    if code == "ya":
        return True
    elif code == "na":
        return False
    elif code == "idk":
        return None

    elif code.startswith(":"):
        data = {}

        for block in _get_blocks(code, ":"):
            lines = block.split("\n")
            key = _get_identifier(lines[0][1:])

            data[key] = unpack(dedent("\n".join(lines[1:])))

        return data

    elif code.startswith(">"):
        data = []

        for block in _get_blocks(code, ">"):
            lines = block.split("\n")
            data.append(unpack(dedent("\n".join(lines[1:]))))

        return data

    else:
        return _get_identifier(code)
