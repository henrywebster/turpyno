"""
Unit tests for systems.
"""

from turpyno.component import IdentifierFactory, LocatorFactory
from turpyno.entity import EntityFactory
from turpyno.renderer import RendererFactory
from turpyno.system import RenderSystem


class TestSystem:
    def test_render_system(self) -> None:

        identifier_factory = IdentifierFactory()
        identifier = identifier_factory.create("entity a")
        renderer_factory = RendererFactory(None, None)
        renderer = renderer_factory.create_rectangle()
        locator_factory = LocatorFactory()
        locator = locator_factory.create()
        entity_factory = EntityFactory()
        entity = entity_factory.create([identifier, renderer, locator])

        system = RenderSystem()
        assert system.handles(entity)
        system.register(entity)
