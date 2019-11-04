"""
Unit tests for menus.
"""

from typing import Generator, List
from pytest import fixture  # type: ignore
from pygame import Surface  # type: ignore
from pygame.font import Font, get_default_font, init, quit  # type: ignore
import numpy as np  # type: ignore
from turpyno.menu import Menu, MenuItem
from turpyno.renderer import RendererFactory
from turpyno.component import LocatorFactory


@fixture(scope="module", autouse=True)
def init_fonts() -> Generator:
    init()
    yield None
    quit()


class TestMenu:
    def test_menu_item(self) -> None:
        font = Font(get_default_font(), 12)
        surface = Surface((1, 1))
        renderer_factory = RendererFactory(surface)
        renderer = renderer_factory.create_text("test", font)
        locator_factory = LocatorFactory()
        locator = locator_factory.create()
        l: List[int] = []
        action = lambda: l.append(1)  # noqa: E731
        item = MenuItem(locator, renderer, action)
        assert 0 == len(l)

        item.action()
        assert 1 == len(l)

    def test_menu_focus(self) -> None:
        font = Font(get_default_font(), 12)
        surface = Surface((1, 1))
        renderer_factory = RendererFactory(surface)
        renderer = renderer_factory.create_text("test", font)
        locator_factory = LocatorFactory()
        locator = locator_factory.create()
        l: List[int] = []
        action = lambda: l.append(1)  # noqa: E731
        item = MenuItem(locator, renderer, action)
        menu = Menu([item], np.array([0, 0, 0], dtype=np.float32), 100)
        assert [] == l

        menu.action()
        assert [1] == l

    def test_menu_next(self) -> None:
        font = Font(get_default_font(), 12)
        surface = Surface((1, 1))
        renderer_factory = RendererFactory(surface)
        renderer_a = renderer_factory.create_text("a", font)
        renderer_b = renderer_factory.create_text("b", font)
        locator_factory = LocatorFactory()
        locator_a = locator_factory.create()
        locator_b = locator_factory.create()
        l: List[int] = []
        action_a = lambda: l.append(1)  # noqa: E731
        action_b = lambda: l.append(2)  # noqa: E731
        item_a = MenuItem(locator_a, renderer_a, action_a)
        item_b = MenuItem(locator_b, renderer_b, action_b)
        menu = Menu([item_a, item_b], np.array([0, 0, 0], dtype=np.float32), 100)
        assert [] == l

        menu.action()
        assert [1] == l

        menu.next()
        menu.action()
        assert [1, 2] == l

    def test_menu_previous(self) -> None:
        font = Font(get_default_font(), 12)
        surface = Surface((1, 1))
        renderer_factory = RendererFactory(surface)
        renderer_a = renderer_factory.create_text("a", font)
        renderer_b = renderer_factory.create_text("b", font)
        locator_factory = LocatorFactory()
        locator_a = locator_factory.create()
        locator_b = locator_factory.create()
        l: List[int] = []
        action_a = lambda: l.append(1)  # noqa: E731
        action_b = lambda: l.append(2)  # noqa: E731
        item_a = MenuItem(locator_a, renderer_a, action_a)
        item_b = MenuItem(locator_b, renderer_b, action_b)
        menu = Menu([item_a, item_b], np.array([0, 0, 0], dtype=np.float32), 100)
        assert [] == l

        menu.action()
        assert [1] == l

        menu.next()
        menu.action()
        assert [1, 2] == l

        menu.previous()
        menu.action()
        assert [1, 2, 1] == l

    def test_menu_next_wrap(self) -> None:
        font = Font(get_default_font(), 12)
        surface = Surface((1, 1))
        renderer_factory = RendererFactory(surface)
        renderer_a = renderer_factory.create_text("a", font)
        renderer_b = renderer_factory.create_text("b", font)
        locator_factory = LocatorFactory()
        locator_a = locator_factory.create()
        locator_b = locator_factory.create()
        l: List[int] = []
        action_a = lambda: l.append(1)  # noqa: E731
        action_b = lambda: l.append(2)  # noqa: E731
        item_a = MenuItem(locator_a, renderer_a, action_a)
        item_b = MenuItem(locator_b, renderer_b, action_b)
        menu = Menu([item_a, item_b], np.array([0, 0, 0], dtype=np.float32), 100)
        assert [] == l

        menu.action()
        assert [1] == l

        menu.next()
        menu.action()
        assert [1, 2] == l

        menu.next()
        menu.action()
        assert [1, 2, 1] == l

    def test_menu_previous_wrap(self) -> None:
        font = Font(get_default_font(), 12)
        surface = Surface((1, 1))
        renderer_factory = RendererFactory(surface)
        renderer_a = renderer_factory.create_text("a", font)
        renderer_b = renderer_factory.create_text("b", font)
        locator_factory = LocatorFactory()
        locator_a = locator_factory.create()
        locator_b = locator_factory.create()
        l: List[int] = []
        action_a = lambda: l.append(1)  # noqa: E731
        action_b = lambda: l.append(2)  # noqa: E731
        item_a = MenuItem(locator_a, renderer_a, action_a)
        item_b = MenuItem(locator_b, renderer_b, action_b)
        menu = Menu([item_a, item_b], np.array([0, 0, 0], dtype=np.float32), 100)
        assert [] == l

        menu.action()
        assert [1] == l

        menu.previous()
        menu.action()
        assert [1, 2] == l

        menu.previous()
        menu.action()
        assert [1, 2, 1] == l
