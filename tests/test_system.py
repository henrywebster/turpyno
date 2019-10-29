"""
Unit tests for systems.
"""

from turpyno.component import (
    IdentifierFactory,
    RendererFactory,
    IdentifierContext,
    RendererContext,
)
from turpyno.entity import EntityFactory
from turpyno.system import RenderSystem


class TestSystem:
    def test_render_system(self) -> None:

        identifier_factory = IdentifierFactory()
        identifier = identifier_factory.create(IdentifierContext("entity a"))
        renderer_factory = RendererFactory()
        renderer = renderer_factory.create(RendererContext(None, None))
        entity_factory = EntityFactory()
        entity = entity_factory.create([identifier, renderer])

        system = RenderSystem()
        assert system.handles(entity)
        system.register(entity)
