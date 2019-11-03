"""
Classes that represent scripts.
"""

from typing import Callable
import numpy as np  # type: ignore
from turpyno.component import Locator
from turpyno.mover import Mover
from turpyno.recipe import move


def move_right(mover: Mover, locator: Locator) -> Callable[[], None]:
    """Closure to contain move right script."""

    return lambda: move(mover, locator, np.array([1, 0, 0], dtype=np.float32))


def move_left(mover: Mover, locator: Locator) -> Callable[[], None]:
    """Closure to contain move left."""

    return lambda: move(mover, locator, np.array([-1, 0, 0], dtype=np.float32))


def move_up(mover: Mover, locator: Locator) -> Callable[[], None]:
    """Closure to contain move up."""

    return lambda: move(mover, locator, np.array([0, -1, 0], dtype=np.float32))


def move_down(mover: Mover, locator: Locator) -> Callable[[], None]:
    """Closure to contain move down."""

    return lambda: move(mover, locator, np.array([0, 1, 0], dtype=np.float32))
