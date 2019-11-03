"""
Classes for menus.
"""

from typing import List, Callable
from pygame import Surface  # type: ignore
from pygame.font import Font  # type: ignore


class MenuItem:  # pylint: disable=too-few-public-methods
    """Represents a menu item."""

    def __init__(
        self, text: str, font: Font, surface: Surface, action: Callable[[], None]
    ) -> None:
        self._focus_color = (0, 255, 0)
        self._color = (255, 255, 255)
        self._font = font
        self._text = text
        self._surface = surface
        self._focused = False
        self._action = action

    def focus(self) -> None:
        """Focus the menu item."""
        self._focused = True

    def action(self) -> None:
        """Perform an action."""
        self._action()

    def render(self) -> None:
        """Render the menu item."""
        if self._focused:
            color = self._focus_color
        else:
            color = self._color
        self._surface.blit(self._font.render(self._text, True, color), (0, 0))


class MenuItemFactory:  # pylint: disable=too-few-public-methods
    """Class to make menu items."""

    def __init__(self, surface: Surface, font: Font) -> None:
        self._surface = surface
        self._font = font

    def create(self, text: str, action: Callable[[], None]) -> MenuItem:
        """Create a new menu item on same surface with same font."""
        return MenuItem(text, self._font, self._surface, action)


class Menu:
    """Represents a collection of menu items."""

    def __init__(self, items: List[MenuItem]) -> None:
        assert len(items) != 0
        self._items = items
        self._focus = 0
        self._count = len(items)

    def action(self) -> None:
        """Act on the currently focused item."""
        self._items[self._focus].action()

    def next(self) -> None:
        """Move focus to the next menu item."""
        if self._focus + 1 < self._count:
            self._focus += 1
        else:
            self._focus = 0
        self._items[self._focus].focus()

    def previous(self) -> None:
        """Move focus to the previous menu item."""
        if self._focus > 0:
            self._focus -= 1
        else:
            self._focus = self._count - 1
        self._items[self._focus].focus()
