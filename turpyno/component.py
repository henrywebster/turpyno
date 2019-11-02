"""
Unit tests for the component class.
"""

import numpy as np  # type: ignore
from pygame import Rect  # type: ignore
from turpyno.generator import unique_id


class Component:  # pylint: disable=too-few-public-methods
    """Super class for all components."""


class Identifier(Component):
    """Component that identifies."""

    def __init__(self, eid: int, name: str) -> None:
        self._eid = eid
        self._name = name
        self._alive = False

    def eid(self) -> int:
        """Return the entity id field."""
        return self._eid

    def name(self) -> str:
        """Return the name field."""
        return self._name

    def alive(self) -> bool:
        """Return if the entity is alive."""
        return self._alive

    def toggle(self) -> bool:
        """Switch to opposite state and return the new value."""
        self._alive = not self._alive
        return self._alive


class IdentifierFactory:  # pylint: disable=too-few-public-methods
    """Factory method for identifier components."""

    def __init__(self) -> None:
        self._generator = unique_id()

    def create(self, name: str) -> Identifier:
        """Create a new named identifier."""
        return Identifier(next(self._generator), name)


class Locator(Component):
    """Class for setting the local transformation of a component."""

    def __init__(self, offset: np.array) -> None:
        self._translation = offset

    def translate(self, translation: np.array) -> None:
        """Set the translation of the locator."""
        self._translation = translation

    def translation(self) -> np.array:
        """Get the translation of the locator."""
        return self._translation


class LocatorFactory:  # pylint: disable=too-few-public-methods
    """Factory for locator components."""

    def create(  # pylint: disable=no-self-use
        self, offset: np.array = np.array([0, 0, 0], dtype=np.float32)
    ) -> Locator:
        """Create a new mover."""
        return Locator(offset)


class Collider(Component):
    """Class for collision."""

    def __init__(self, hitbox: Rect) -> None:
        self._hitbox = hitbox

    def query(self, hitbox: Rect) -> bool:
        """Test if this collider is colliding."""
        return self._hitbox.colliderect(hitbox)

    def hitbox(self) -> Rect:
        """Return the hitbox of the component."""
        return self._hitbox

    def update(self, location: np.array, scale: float) -> None:
        """Update a hitbox."""
        self._hitbox.x = location[0]
        self._hitbox.y = location[1]
        self._hitbox.w = scale
        self._hitbox.h = scale


class ColliderFactory:  # pylint: disable=too-few-public-methods
    """Factory for colliders."""

    def create(self) -> Collider:  # pylint: disable=no-self-use
        """Create a new collider."""
        return Collider(Rect(0, 0, 0, 0))
