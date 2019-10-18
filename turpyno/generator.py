"""
Helpers for generating in Turpyno
"""

from typing import Generator


def unique_id() -> Generator[int, None, None]:
    """Generate a new ID every time by counting up"""
    counter: int = 0
    while True:
        current, counter = counter, counter + 1
        yield current
