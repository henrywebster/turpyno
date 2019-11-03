"""
Class for moving entities.
"""

from typing import List, Optional
import numpy as np  # type: ignore
from turpyno.component import Component, Collider


class Mover(Component):
    """This component handles movement."""

    def __init__(self, offset: np.array, obstructs: List[Collider]) -> None:
        self._target = np.array([0, 0, 0], dtype=np.float32)
        self._translation = offset
        self._velocity = 1.0
        self._obstructs = obstructs

    def target(self, aim: np.array) -> None:
        """Set where to aim the mover."""
        self._target = aim

    def velocitize(self, velocity: float) -> None:
        """Set how much velocity."""
        self._velocity = velocity

    def obstructed(self) -> bool:
        """Check if there is something in the way."""
        candidate = np.add(self._translation, np.multiply(self._target, self._velocity))
        for collider in self._obstructs:  # multithread!
            if collider.query_point(candidate[0], candidate[1]):
                return True
        return False

    def move(self) -> np.array:
        """Set a new translation based on target and velocity."""
        self._translation = np.add(
            self._translation, np.multiply(self._target, self._velocity)
        )
        return self._translation


class MoverFactory:  # pylint: disable=too-few-public-methods
    """Factory for mover components."""

    def create(  # pylint: disable=no-self-use
        self,
        offset: np.array = np.array([0, 0, 0], dtype=np.float32),
        obstructs: Optional[List[Collider]] = None,
    ) -> Mover:
        """Create a new mover."""
        if obstructs is None:
            return Mover(offset, [])
        return Mover(offset, obstructs)
