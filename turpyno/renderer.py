"""
Classes for rendering.
"""

from pygame import Surface, Rect, draw  # type: ignore
from pygame.font import Font  # type: ignore
import numpy as np  # type: ignore
from turpyno.component import Component


class Renderer(Component):
    """Component that renders."""

    def __init__(self, surface: Surface) -> None:
        self._coloring = np.array([255, 255, 255], dtype=np.uint8)
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

    def render(self) -> None:  # pylint: disable=no-self-use
        """Render to the screen. Should not be called."""
        assert False


class RectangleRenderer(Renderer):
    """Component that renders rectangles."""

    def __init__(self, surface: Surface, rectangle: Rect) -> None:
        super().__init__(surface)
        self._rectangle = rectangle

    def render(self) -> None:
        """Render rectangle to the surface."""
        self._rectangle.x = self._translation[0]
        self._rectangle.y = self._translation[1]
        self._rectangle.w = self._scaling
        self._rectangle.h = self._scaling
        draw.rect(self._surface, tuple(self._coloring), self._rectangle)


class CircleRenderer(Renderer):
    """Component that renders circles."""

    def render(self) -> None:
        """Render circle to the surface."""
        center_x = self._translation[0] + self._scaling
        center_y = self._translation[1] + self._scaling
        draw.circle(
            self._surface,
            tuple(self._coloring),
            (int(center_x), int(center_y)),
            int(self._scaling),
        )


class TextRenderer(Renderer):
    """Component for rendering text."""

    def __init__(self, surface: Surface, text: str, font: Font) -> None:
        super().__init__(surface)
        self._font = font
        self._text = text

    def render(self) -> None:
        """Render text to the surface."""
        placement = (self._translation[0], self._translation[1])
        self._surface.blit(
            self._font.render(self._text, True, self._coloring), placement
        )


class RendererFactory:  # pylint: disable=too-few-public-methods
    """Factory method for renderer components."""

    def __init__(self, surface: Surface, rectangle: Rect = Rect(0, 0, 1, 1)) -> None:
        """Initialize a renderer factory."""
        self._surface = surface
        self._rectangle = rectangle

    def create_rectangle(self) -> Renderer:
        """Create a new rectangle renderer."""
        return RectangleRenderer(self._surface, self._rectangle)

    def create_circle(self) -> Renderer:
        """Create a new circle renderer."""
        return CircleRenderer(self._surface)

    def create_text(self, text: str, font: Font) -> TextRenderer:
        """Create a new text renderer."""
        return TextRenderer(self._surface, text, font)
