"""
Class for managing key bindings.
"""

from typing import Callable, Dict


class Keymap:
    """Class for keybindings."""

    def __init__(self) -> None:
        self._map: Dict[int, Callable[[], None]] = {}

    def bind(self, key: int, action: Callable[[], None]) -> None:
        """Bind a key to an action."""
        self._map[key] = action

    def action(self, key: int) -> None:
        """Perform the action associated with the key."""
        self._map[key]()
