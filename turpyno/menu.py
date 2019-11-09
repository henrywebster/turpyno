"""
Classes for menus.
"""

from typing import List, Callable
import numpy as np  # type: ignore
from turpyno.renderer import TextRenderer
from turpyno.component import Locator


class MenuItem:
    """Represents a menu item."""

    def __init__(
        self, locator: Locator, renderer: TextRenderer, action: Callable[[], None]
    ) -> None:
        self._focus_color = np.array([255, 255, 0], np.uint8)
        self._color = np.array([255, 255, 255], np.uint8)
        self._focused = False
        self._action = action
        self._renderer = renderer
        self._locator = locator

    def focus(self) -> None:
        """Focus the menu item."""
        self._focused = True
        self._renderer.color(self._focus_color)

    def unfocus(self) -> None:
        """Unfocus the menu item."""
        self._focused = False
        self._renderer.color(self._color)

    def action(self) -> None:
        """Perform an action."""
        self._action()

    def translate(self, translation: np.array) -> None:
        """Translate the menu item."""
        self._locator.translate(translation)


class Menu:
    """Represents a collection of menu items."""

    def __init__(self, items: List[MenuItem], offset: np.array, spacing: int) -> None:
        assert len(items) != 0  # nosec
        self._items = items
        self._focus = 0
        self._count = len(items)
        self._items[0].focus()
        delta = 0
        for item in items:
            item.translate(np.add(offset, np.array([0, delta, 0], dtype=np.float32)))
            delta += spacing

    def action(self) -> None:
        """Act on the currently focused item."""
        self._items[self._focus].action()

    def next(self) -> None:
        """Move focus to the next menu item."""
        self._items[self._focus].unfocus()
        if self._focus + 1 < self._count:
            self._focus += 1
        else:
            self._focus = 0
        self._items[self._focus].focus()

    def previous(self) -> None:
        """Move focus to the previous menu item."""
        self._items[self._focus].unfocus()
        if self._focus > 0:
            self._focus -= 1
        else:
            self._focus = self._count - 1
        self._items[self._focus].focus()
