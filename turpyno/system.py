"""
Class for the game systems.
"""

from typing import List, Callable
from pygame import Surface  # type: ignore
from turpyno.component import Identifier, Locator
from turpyno.renderer import Renderer, RendererFactory
from turpyno.entity import Entity


class RenderSystem:
    """Class for rendering system."""

    def __init__(self, surface: Surface, factory: RendererFactory) -> None:
        self._entities: List[Entity] = []
        self._factory = factory
        self._surface = surface

    def renderer_factory(self) -> RendererFactory:
        """Return a renderer factory that will draw when this system renders."""
        return self._factory

    @classmethod
    def handles(cls, entity: Entity) -> bool:
        """Return true if an entity has all the needed component types."""
        return entity.has(Identifier) and entity.has(Renderer) and entity.has(Locator)

    def register(self, entity: Entity) -> None:
        """Put this entity in the processing list."""
        self._entities.append(entity)

    def render(self) -> Surface:
        """Render to the surface."""
        self._surface.fill((0, 0, 0))
        for entity in self._entities:
            translation = entity.get(Locator).translation()
            renderer = entity.get(Renderer)
            renderer.translate(translation)
            renderer.render()
        return self._surface


class RenderSystemFactory:  # pylint: disable=too-few-public-methods
    """Class for creating a render system."""

    def create(  # pylint: disable=no-self-use
        self, surface: Surface, factory: Callable[[Surface], RendererFactory]
    ) -> RenderSystem:
        """Creates a render system."""
        return RenderSystem(surface, factory(surface))
