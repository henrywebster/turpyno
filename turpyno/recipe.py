"""
Some common actions.
"""

import numpy as np  # type: ignore
from turpyno.component import Locator
from turpyno.mover import Mover


def move(mover: Mover, locator: Locator, target: np.array) -> None:
    """Moves the locator to the right."""
    mover.target(target)
    if not mover.obstructed():
        locator.translate(mover.move())
