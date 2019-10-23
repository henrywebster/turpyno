"""
Unit tests for components.
"""

from pytest import approx  # type: ignore
import numpy as np  # type: ignore
from turpyno.component import (
    IdentifierContext,
    IdentifierFactory,
    RendererContext,
    RendererFactory,
    TypeId,
)


class TestComponent:
    def test_identifier_named(self) -> None:
        factory = IdentifierFactory()
        context = IdentifierContext("Component A")
        identifier = factory.create(context)

        assert "Component A" == identifier.name()
        assert not identifier.alive()
        assert 0 == identifier.eid()
        assert TypeId.IDENTIFIER == identifier.cid()

    def test_identifier_toggle(self) -> None:
        factory = IdentifierFactory()
        context = IdentifierContext("Component A")
        identifier = factory.create(context)
        assert "Component A" == identifier.name()
        assert not identifier.alive()
        assert 0 == identifier.eid()
        assert TypeId.IDENTIFIER == identifier.cid()

        identifier.toggle()
        assert identifier.alive()
        identifier.toggle()
        assert not identifier.alive()

    def test_identifier_unqiue_id(self) -> None:
        factory = IdentifierFactory()
        context_a = IdentifierContext("Component A")
        context_b = IdentifierContext("Component B")
        identifier_a = factory.create(context_a)
        identifier_b = factory.create(context_b)

        assert "Component A" == identifier_a.name()
        assert not identifier_a.alive()
        assert 0 == identifier_a.eid()
        assert TypeId.IDENTIFIER == identifier_a.cid()

        assert "Component B" == identifier_b.name()
        assert not identifier_b.alive()
        assert 1 == identifier_b.eid()
        assert TypeId.IDENTIFIER == identifier_b.cid()

    def test_renderer(self) -> None:
        factory = RendererFactory()
        context = RendererContext(None, 50)
        renderer = factory.create(context)

        assert 50 == renderer.size()
        assert approx(np.array([0, 0, 0], dtype=np.float32)) == renderer.translation()

    def test_renderer_transalte(self) -> None:
        factory = RendererFactory()
        context = RendererContext(None, 50)
        renderer = factory.create(context)

        assert 50 == renderer.size()
        assert approx(np.array([0, 0, 0], dtype=np.float32)) == renderer.translation()

        renderer.translate(np.array([50, 50, 0], dtype=np.float32))
        assert 50 == renderer.size()
        assert approx(np.array([50, 50, 0], dtype=np.float32)) == renderer.translation()
