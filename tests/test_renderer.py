"""
Unit tests for renderers.
"""

from pygame import Rect, Surface  # type: ignore
from pytest import approx  # type: ignore
import numpy as np  # type: ignore
from turpyno.renderer import (
    CircleRendererContext,
    RectangleRendererContext,
    RendererFactory,
)


class TestRenderer:
    def test_rectangle_renderer(self) -> None:
        factory = RendererFactory()
        surface = Surface((100, 100))
        rectangle = Rect(0, 0, 1, 1)
        context = RectangleRendererContext(surface, rectangle)
        renderer = factory.create_rectangle(context)

        assert approx(np.array([255, 255, 255], dtype=np.uint8)) == renderer.coloring()
        assert approx(1.0) == renderer.scaling()
        assert approx(np.array([0, 0, 0], dtype=np.float32)) == renderer.translation()

        renderer.render()
        assert approx(1.0) == rectangle.w
        assert approx(1.0) == rectangle.h
        assert approx(0.0) == rectangle.x
        assert approx(0.0) == rectangle.y

    def test_rectangle_renderer_transalte(self) -> None:
        factory = RendererFactory()
        surface = Surface((100, 100))
        rectangle = Rect(0, 0, 1, 1)
        context = RectangleRendererContext(surface, rectangle)
        renderer = factory.create_rectangle(context)

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

    def test_rectangle_renderer_scale(self) -> None:
        factory = RendererFactory()
        surface = Surface((100, 100))
        rectangle = Rect(0, 0, 1, 1)
        context = RectangleRendererContext(surface, rectangle)
        renderer = factory.create_rectangle(context)

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

    def test_rectangle_renderer_color(self) -> None:
        factory = RendererFactory()
        surface = Surface((100, 100))
        rectangle = Rect(0, 0, 1, 1)
        context = RectangleRendererContext(surface, rectangle)
        renderer = factory.create_rectangle(context)

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

    def test_circle_renderer(self) -> None:
        factory = RendererFactory()
        surface = Surface((100, 100))
        context = CircleRendererContext(surface)
        renderer = factory.create_circle(context)

        assert approx(np.array([255, 255, 255], dtype=np.uint8)) == renderer.coloring()
        assert approx(1.0) == renderer.scaling()
        assert approx(np.array([0, 0, 0], dtype=np.float32)) == renderer.translation()

    def test_circle_renderer_translate(self) -> None:
        factory = RendererFactory()
        surface = Surface((100, 100))
        context = CircleRendererContext(surface)
        renderer = factory.create_circle(context)

        assert approx(np.array([255, 255, 255], dtype=np.uint8)) == renderer.coloring()
        assert approx(1.0) == renderer.scaling()
        assert approx(np.array([0, 0, 0], dtype=np.float32)) == renderer.translation()

        renderer.translate(np.array([50, 50, 0], dtype=np.float32))
        assert approx(np.array([255, 255, 255], dtype=np.uint8)) == renderer.coloring()
        assert approx(1.0 == renderer.scaling())
        assert approx(np.array([50, 50, 0], dtype=np.float32)) == renderer.translation()

    def test_circle_renderer_scale(self) -> None:
        factory = RendererFactory()
        surface = Surface((100, 100))
        context = CircleRendererContext(surface)
        renderer = factory.create_circle(context)

        assert approx(np.array([255, 255, 255], dtype=np.uint8)) == renderer.coloring()
        assert approx(1.0) == renderer.scaling()
        assert approx(np.array([0, 0, 0], dtype=np.float32)) == renderer.translation()

        renderer.scale(20.0)
        assert approx(np.array([255, 255, 255], dtype=np.uint8)) == renderer.coloring()
        assert approx(20.0) == renderer.scaling()
        assert approx(np.array([0, 0, 0], dtype=np.float32)) == renderer.translation()

    def test_circle_renderer_color(self) -> None:
        factory = RendererFactory()
        surface = Surface((100, 100))
        context = CircleRendererContext(surface)
        renderer = factory.create_circle(context)

        assert approx(np.array([255, 255, 255], dtype=np.uint8)) == renderer.coloring()
        assert approx(1.0) == renderer.scaling()
        assert approx(np.array([0, 0, 0], dtype=np.float32)) == renderer.translation()

        renderer.color(np.array([0, 0, 255], dtype=np.uint8))
        assert approx(np.array([0, 0, 255], dtype=np.uint8)) == renderer.coloring()
        assert approx(1.0) == renderer.scaling()
        assert approx(np.array([0, 0, 0], dtype=np.float32)) == renderer.translation()
