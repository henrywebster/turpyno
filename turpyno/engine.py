"""
Class for the engine.
"""

from enum import Enum, auto
from typing import List
import pygame  # type: ignore

from turpyno.component import (
    Component,
    Identifier,
    IdentifierContext,
    IdentifierFactory,
)
from turpyno.entity import Entity, EntityFactory
from turpyno.renderer import (
    CircleRendererContext,
    Renderer,
    RectangleRendererContext,
    RendererFactory,
)
from turpyno.system import RenderSystem


class VideoMode(Enum):
    """Enum for types of video displays."""

    NOOP = (auto(),)
    DISPLAY = auto()


class Engine:  # pylint: disable=too-many-instance-attributes
    """Manages the global engine."""

    def __init__(self, width: int, height: int) -> None:
        self._entities: List[Entity] = []
        self._entity_factory = EntityFactory()
        self._identifier_factory = IdentifierFactory()
        self._renderer_factory = RendererFactory()
        self._render_system = RenderSystem()
        self._rectangle = pygame.Rect(0, 0, 1, 1)
        self._surface = pygame.Surface((width, height))
        self._screen: pygame.Surface = None

    def setup(self, video_mode: VideoMode) -> None:
        """Initialize engine."""
        pygame.init()
        if video_mode == VideoMode.NOOP:
            self._screen = self._surface
        else:
            self._screen = pygame.display.set_mode(
                (self._surface.get_width(), self._surface.get_height())
            )

    def create_identifier(self, context: IdentifierContext) -> Identifier:
        """Create an identifier component."""
        return self._identifier_factory.create(context)

    def create_rectangle_renderer(self) -> Renderer:
        """Create a renderer. Beware the hack."""
        context = RectangleRendererContext(self._surface, self._rectangle)
        return self._renderer_factory.create_rectangle(context)

    def create_circle_renderer(self) -> Renderer:
        """Create a circle renderer."""
        context = CircleRendererContext(self._surface)
        return self._renderer_factory.create_circle(context)

    def create_entity(self, components: List[Component]) -> Entity:
        """Create an entity of components."""
        entity = self._entity_factory.create(components)
        self._entities.append(entity)
        self._render_system.register(entity)
        return entity

    def entities(self) -> List[Entity]:
        """Return the list of entities in the engine."""
        return self._entities

    def render(self) -> None:  # pylint: disable=no-self-use
        """Run render system."""
        self._render_system.render()
        self._screen.blit(self._surface, (0, 0))
        pygame.display.flip()
