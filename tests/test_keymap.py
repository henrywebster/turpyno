"""
Unit test for keymap class.
"""

from typing import List
from pygame.locals import K_a  # type: ignore
import pytest  # type: ignore
from turpyno.keymap import Keymap


class TestKeymap:
    def test_keymap(self) -> None:
        keymap = Keymap()
        a: List[int] = []
        callback = lambda: a.append(1)  # noqa: E731
        keymap.bind(K_a, callback)
        assert 0 == len(a)

        keymap.action(K_a)
        assert 1 == len(a)
        assert 1 == a[0]

    def test_keymap_no_binding(self) -> None:
        keymap = Keymap()
        with pytest.raises(KeyError):
            keymap.action(K_a)

    def test_isolated_maps(self) -> None:
        keymap_a = Keymap()
        keymap_b = Keymap()
        a: List[int] = []
        b: List[int] = []
        callback_a = lambda: a.append(1)  # noqa: E731
        callback_b = lambda: b.append(2)  # noqa: E731
        assert 0 == len(a)
        assert 0 == len(b)

        keymap_a.bind(K_a, callback_a)
        keymap_b.bind(K_a, callback_b)

        keymap_a.action(K_a)
        assert 1 == len(a)
        assert 1 == a[0]
        assert 0 == len(b)

        keymap_b.action(K_a)
        assert 1 == len(a)
        assert 1 == a[0]
        assert 1 == len(b)
        assert 2 == b[0]
