"""
Class for the game systems.
"""

from typing import List

from turpyno.component import Identifier, Renderer
from turpyno.entity import Entity


class RenderSystem:
    """Class for rendering system."""

    def __init__(self) -> None:
        self._entities: List[Entity] = []

    @classmethod
    def handles(cls, entity: Entity) -> bool:
        """Return true if an entity has all the needed component types."""
        return entity.has(Identifier) and entity.has(Renderer)

    def register(self, entity: Entity) -> None:
        """Put this entity in the processing list."""
        self._entities.append(entity)

    def render(self) -> None:
        """Render to the screen."""
        for entity in self._entities:
            entity.get(Renderer).render()
