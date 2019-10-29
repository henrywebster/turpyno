"""
Unit tests for components.
"""

from pygame import Rect, Surface  # type: ignore
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
        surface = Surface((100, 100))
        rectangle = Rect(0, 0, 1, 1)
        context = RendererContext(surface, rectangle)
        renderer = factory.create(context)

        assert approx(np.array([255, 255, 255], dtype=np.uint8)) == renderer.coloring()
        assert approx(1.0) == renderer.scaling()
        assert approx(np.array([0, 0, 0], dtype=np.float32)) == renderer.translation()

        renderer.render()
        assert approx(1.0) == rectangle.w
        assert approx(1.0) == rectangle.h
        assert approx(0.0) == rectangle.x
        assert approx(0.0) == rectangle.y

    def test_renderer_transalte(self) -> None:
        factory = RendererFactory()
        surface = Surface((100, 100))
        rectangle = Rect(0, 0, 1, 1)
        context = RendererContext(surface, rectangle)
        renderer = factory.create(context)

        assert approx(np.array([255, 255, 255], dtype=np.uint8)) == renderer.coloring()
        assert approx(1.0) == renderer.scaling()
        assert approx(np.array([0, 0, 0], dtype=np.float32)) == renderer.translation()

        renderer.translate(np.array([50, 50, 0], dtype=np.float32))
        assert approx(np.array([255, 255, 255], dtype=np.uint8)) == renderer.coloring()
        assert approx(1.0 == renderer.scaling())
        assert approx(np.array([50, 50, 0], dtype=np.float32)) == renderer.translation()

        renderer.render()
        assert approx(1.0) == rectangle.w
        assert approx(1.0) == rectangle.h
        assert approx(50.0) == rectangle.x
        assert approx(50.0) == rectangle.y

    def test_renderer_scale(self) -> None:
        factory = RendererFactory()
        surface = Surface((100, 100))
        rectangle = Rect(0, 0, 1, 1)
        context = RendererContext(surface, rectangle)
        renderer = factory.create(context)

        assert approx(np.array([255, 255, 255], dtype=np.uint8)) == renderer.coloring()
        assert approx(1.0) == renderer.scaling()
        assert approx(np.array([0, 0, 0], dtype=np.float32)) == renderer.translation()

        renderer.scale(20.0)
        assert approx(np.array([255, 255, 255], dtype=np.uint8)) == renderer.coloring()
        assert approx(20.0) == renderer.scaling()
        assert approx(np.array([0, 0, 0], dtype=np.float32)) == renderer.translation()

        renderer.render()
        assert approx(20.0) == rectangle.w
        assert approx(20.0) == rectangle.h
        assert approx(0.0) == rectangle.x
        assert approx(0.0) == rectangle.y

    def test_renderer_color(self) -> None:
        factory = RendererFactory()
        surface = Surface((100, 100))
        rectangle = Rect(0, 0, 1, 1)
        context = RendererContext(surface, rectangle)
        renderer = factory.create(context)

        assert approx(np.array([255, 255, 255], dtype=np.uint8)) == renderer.coloring()
        assert approx(1.0) == renderer.scaling()
        assert approx(np.array([0, 0, 0], dtype=np.float32)) == renderer.translation()

        renderer.color(np.array([0, 0, 255], dtype=np.uint8))
        assert approx(np.array([0, 0, 255], dtype=np.uint8)) == renderer.coloring()
        assert approx(1.0) == renderer.scaling()
        assert approx(np.array([0, 0, 0], dtype=np.float32)) == renderer.translation()

        renderer.render()
        assert approx(1.0) == rectangle.w
        assert approx(1.0) == rectangle.h
        assert approx(0.0) == rectangle.x
        assert approx(0.0) == rectangle.y
