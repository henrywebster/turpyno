"""
Unit tests for the component class.
"""

from enum import Enum
from typing import NamedTuple

import numpy as np  # type: ignore
from pygame import Surface, draw  # type: ignore

from turpyno.generator import unique_id


class TypeId(Enum):
    """Types enum for components."""

    IDENTIFIER = (1,)
    RENDERER = 2


IdentifierContext = NamedTuple("IdentifierContext", [("name", str)])
RendererContext = NamedTuple("RendererContext", [("surface", Surface), ("size", int)])


class Component:  # pylint: disable=too-few-public-methods
    """Super class for all components."""

    def __init__(self, type_id: TypeId):
        self.type = type_id

    def cid(self) -> TypeId:
        """Return the unique identifier for this component type."""
        return self.type


class Identifier(Component):
    """Component that identifies."""

    def __init__(self, eid: int, name: str) -> None:
        super().__init__(TypeId.IDENTIFIER)
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

    def create(self, context: IdentifierContext) -> Identifier:
        """Create a new named identifier."""
        return Identifier(next(self._generator), context.name)


class Renderer(Component):
    """Component that renders."""

    def __init__(self, size: int, surface: Surface) -> None:
        super().__init__(TypeId.RENDERER)
        self._size = size
        self._translation = np.array([0, 0, 0], dtype=np.float32)
        self._surface = surface

    def size(self) -> int:
        """Return the size."""
        return self._size

    def translation(self) -> np.array:
        """Return the translation."""
        return self._translation

    def translate(self, translation: np.array) -> None:
        """Translate the component."""
        self._translation = translation

    def render(self) -> None:
        """Render to the screen."""
        draw.rect(self._surface, (0, 0, 255), (200, 200, 200, 200))


class RendererFactory:  # pylint: disable=too-few-public-methods,no-self-use
    """Factory method for renderer components."""

    def create(self, context: RendererContext) -> Renderer:
        """Create a new renderer."""
        return Renderer(context.size, context.surface)
