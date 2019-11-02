"""
Class for the engine.
"""
from typing import List
import pygame  # type: ignore
from pygame import Surface, display  # type: ignore

from turpyno.component import Component
from turpyno.entity import Entity, EntityFactory
from turpyno.keymap import Keymap
from turpyno.system import RenderSystem


class EngineError(Exception):
    """Error regarding engine."""


class Engine:
    """Manages the engine."""

    def __init__(self, buff: Surface, screen: Surface, keymap: Keymap) -> None:
        self._entities: List[Entity] = []
        self._entity_factory = EntityFactory()
        self._render_system = RenderSystem()
        self._display = screen
        self._back_buffer = buff
        self._keymap = keymap

    def get_buffer(self) -> Surface:
        """Temporary method to get surface."""
        return self._back_buffer

    def create_entity(self, components: List[Component]) -> Entity:
        """Create an entity of components."""
        entity = self._entity_factory.create(components)
        self._entities.append(entity)
        self._render_system.register(entity)
        return entity

    def entities(self) -> List[Entity]:
        """Return the list of entities in the engine."""
        return self._entities

    def act(self, key: int) -> None:
        """Perform some action based on key."""
        self._keymap.action(key)

    def render(self) -> None:
        """Run render system."""
        self._back_buffer.fill((0, 0, 0))
        self._render_system.render()
        self._display.blit(self._back_buffer, (0, 0))
        display.flip()


class EngineFactory:
    """Factory class for engines."""

    def __init__(self, headless: bool) -> None:
        """Creates a new engine factory."""
        self._headless = headless

    def initialize(self) -> None:
        """This initializes the pygame globals."""
        if not self._headless:
            assert not display.get_init()
            pygame.init()

    def create(self, width: int, length: int, keymap: Keymap) -> Engine:
        """Creates an engine."""
        if self._headless:
            shared_surface = Surface((width, length))
            return Engine(shared_surface, shared_surface, keymap)
        if not display.get_init():
            raise EngineError("Display not initialized!")
        return Engine(
            Surface((width, length)), display.set_mode((width, length)), keymap
        )
