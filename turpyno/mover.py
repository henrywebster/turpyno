"""
Class for moving entities.
"""

import numpy as np  # type: ignore
from turpyno.component import Component


class Mover(Component):
    """This component handles movement."""

    def __init__(self, offset: np.array) -> None:
        self._target = np.array([0, 0, 0], dtype=np.float32)
        self._translation = offset
        self._velocity = 1.0

    def target(self, aim: np.array) -> None:
        """Set where to aim the mover."""
        self._target = aim

    def velocitize(self, velocity: float) -> None:
        """Set how much velocity."""
        self._velocity = velocity

    def move(self) -> np.array:  # pylint: disable=no-self-use
        """Set a new translation based on target and velocity."""
        self._translation = np.add(
            self._translation, np.multiply(self._target, self._velocity)
        )
        return self._translation


class MoverFactory:  # pylint: disable=too-few-public-methods
    """Factory for mover components."""

    def create(  # pylint: disable=no-self-use
        self,  # pylint: disable=bad-continuation
        offset: np.array = np.array(  # pylint: disable=bad-continuation
            [0, 0, 0], dtype=np.float32  # pylint: disable=bad-continuation
        ),  # pylint: disable=bad-continuation
    ) -> Mover:
        """Create a new mover."""
        return Mover(offset)
