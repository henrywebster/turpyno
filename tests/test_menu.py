"""
Unit tests for menus.
"""

from typing import Generator, List
from pytest import fixture  # type: ignore
from pygame import Surface  # type: ignore
from pygame.font import Font, get_default_font, init, quit  # type: ignore
from turpyno.menu import Menu, MenuItem


@fixture(scope="module", autouse=True)
def init_fonts() -> Generator:
    init()
    yield None
    quit()


class TestMenu:
    def test_menu_item(self) -> None:
        font = Font(get_default_font(), 12)
        surface = Surface((1, 1))
        l: List[int] = []
        action = lambda: l.append(1)  # noqa: E731
        item = MenuItem("test", font, surface, action)
        assert 0 == len(l)

        item.action()
        assert 1 == len(l)

    def test_menu_focus(self) -> None:
        font = Font(get_default_font(), 12)
        surface = Surface((1, 1))
        l: List[int] = []
        action = lambda: l.append(1)  # noqa: E731
        item = MenuItem("test", font, surface, action)
        menu = Menu([item])
        assert [] == l

        menu.action()
        assert [1] == l

    def test_menu_next(self) -> None:
        font = Font(get_default_font(), 12)
        surface = Surface((1, 1))
        l: List[int] = []
        action_a = lambda: l.append(1)  # noqa: E731
        action_b = lambda: l.append(2)  # noqa: E731
        item_a = MenuItem("a", font, surface, action_a)
        item_b = MenuItem("b", font, surface, action_b)
        menu = Menu([item_a, item_b])
        assert [] == l

        menu.action()
        assert [1] == l

        menu.next()
        menu.action()
        assert [1, 2] == l

    def test_menu_previous(self) -> None:
        font = Font(get_default_font(), 12)
        surface = Surface((1, 1))
        l: List[int] = []
        action_a = lambda: l.append(1)  # noqa: E731
        action_b = lambda: l.append(2)  # noqa: E731
        item_a = MenuItem("a", font, surface, action_a)
        item_b = MenuItem("b", font, surface, action_b)
        menu = Menu([item_a, item_b])
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
        l: List[int] = []
        action_a = lambda: l.append(1)  # noqa: E731
        action_b = lambda: l.append(2)  # noqa: E731
        item_a = MenuItem("a", font, surface, action_a)
        item_b = MenuItem("b", font, surface, action_b)
        menu = Menu([item_a, item_b])
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
        l: List[int] = []
        action_a = lambda: l.append(1)  # noqa: E731
        action_b = lambda: l.append(2)  # noqa: E731
        item_a = MenuItem("a", font, surface, action_a)
        item_b = MenuItem("b", font, surface, action_b)
        menu = Menu([item_a, item_b])
        assert [] == l

        menu.action()
        assert [1] == l

        menu.previous()
        menu.action()
        assert [1, 2] == l

        menu.previous()
        menu.action()
        assert [1, 2, 1] == l
