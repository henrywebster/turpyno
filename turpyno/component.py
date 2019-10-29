"""
Unit tests for the component class.
"""

from enum import Enum
from typing import NamedTuple

import numpy as np  # type: ignore
from pygame import Rect, Surface, draw  # type: ignore

from turpyno.generator import unique_id


class TypeId(Enum):
    """Types enum for components."""

    IDENTIFIER = (1,)
    RENDERER = 2


IdentifierContext = NamedTuple("IdentifierContext", [("name", str)])
RendererContext = NamedTuple(
    "RendererContext", [("surface", Surface), ("rectangle", Rect)]
)


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

    def __init__(self, surface: Surface, rectangle: Rect) -> None:
        super().__init__(TypeId.RENDERER)
        self._coloring = np.array([255, 255, 255], dtype=np.uint8)
        self._rectangle = rectangle
        self._scaling = 1.0
        self._surface = surface
        self._translation = np.array([0, 0, 0], dtype=np.float32)

    def coloring(self) -> np.array:
        """Return the color of the renderer."""
        return self._coloring

    def color(self, coloring: np.array) -> None:
        """Set the color."""
        self._coloring = coloring

    def scaling(self) -> float:
        """Return the scaling."""
        return self._scaling

    def scale(self, scaling: float) -> None:
        """Set the scale."""
        self._scaling = scaling

    def translation(self) -> np.array:
        """Return the translation."""
        return self._translation

    def translate(self, translation: np.array) -> None:
        """Translate the component."""
        self._translation = translation

    def render(self) -> None:
        """Render to the screen."""
        self._rectangle.x = self._translation[0]
        self._rectangle.y = self._translation[1]
        self._rectangle.w = self._scaling
        self._rectangle.h = self._scaling
        draw.rect(self._surface, tuple(self._coloring), self._rectangle)


class RendererFactory:  # pylint: disable=too-few-public-methods,no-self-use
    """Factory method for renderer components."""

    def create(self, context: RendererContext) -> Renderer:
        """Create a new renderer."""
        return Renderer(context.surface, context.rectangle)
