"""
Unit tests for systems.
"""

from typing import Callable
from pygame import Surface  # type: ignore
from turpyno.component import IdentifierFactory, LocatorFactory
from turpyno.entity import EntityFactory
from turpyno.renderer import RendererFactory
from turpyno.system import RenderSystemFactory


class TestSystem:
    def test_render_system(self) -> None:

        system_factory = RenderSystemFactory()
        s: Callable[[Surface], RendererFactory] = lambda surface: RendererFactory(
            surface
        )
        system = system_factory.create(Surface((1, 1)), s)

        identifier_factory = IdentifierFactory()
        identifier = identifier_factory.create("entity a")
        renderer_factory = system.renderer_factory()
        renderer = renderer_factory.create_rectangle()
        locator_factory = LocatorFactory()
        locator = locator_factory.create()
        entity_factory = EntityFactory()
        entity = entity_factory.create([identifier, renderer, locator])

        assert system.handles(entity)
        system.register(entity)
