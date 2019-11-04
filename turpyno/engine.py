"""
Class for the engine.
"""
from typing import List
import pygame  # type: ignore
from pygame import Surface, display  # type: ignore

from turpyno.entity import Entity, EntityFactory
from turpyno.scene import Scene


class EngineError(Exception):
    """Error regarding engine."""


class Engine:
    """Manages the engine."""

    def __init__(self, screen: Surface) -> None:
        self._entities: List[Entity] = []
        self._entity_factory = EntityFactory()
        self._display = screen
        self._scene = Scene()
        self._stopped = False

    def stage(self, scene: Scene) -> None:
        """Stage a scene to the main window."""
        self._scene = scene

    def act(self, key: int) -> None:
        """Perform some action based on key."""
        self._scene.action(key)

    def stop(self) -> None:
        """Perform clean up tasks."""
        self._stopped = True

    def stopped(self) -> bool:
        """Query if stopped."""
        return self._stopped

    def render(self) -> None:
        """Run render system."""
        self._display.blit(self._scene.render(), (0, 0))
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

    def create(self, width: int, length: int) -> Engine:
        """Creates an engine."""
        if self._headless:
            return Engine(Surface((width, length)))
        if not display.get_init():
            raise EngineError("Display not initialized!")
        return Engine(display.set_mode((width, length)))
