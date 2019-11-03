"""
Classes for managing different scenes on the screen.
"""

from typing import List
from pygame import Surface  # type: ignore
from turpyno.component import Component
from turpyno.keymap import Keymap
from turpyno.system import RenderSystem
from turpyno.entity import EntityFactory, Entity


class Scene:
    """Class to manage scene state."""

    def render(self) -> Surface:  # pylint: disable=no-self-use
        """Does nothing."""
        assert False

    def action(self, key: int) -> None:  # pylint: disable=unused-argument,no-self-use
        """Does nothing."""
        assert False


class GameScene(Scene):
    """Class for a rendered scene."""

    def __init__(self, keymap: Keymap, render_system: RenderSystem) -> None:
        self._keymap = keymap
        self._render_system = render_system
        self._entities: List[Entity] = []
        self._entity_factory = EntityFactory()

    def render(self) -> Surface:
        """Render the scene to the surface and return."""
        return self._render_system.render()

    def action(self, key: int) -> None:
        """Perform an action based on the keymap."""
        self._keymap.action(key)

    def create_entity(self, components: List[Component]) -> Entity:
        """Create an entity of components for this scene."""
        entity = self._entity_factory.create(components)
        self._entities.append(entity)
        self._render_system.register(entity)
        return entity
