"""
Unit tests for components.
"""

from turpyno.component import Nooper, TypeId


class TestComponent:

    def test_nooper(self) -> None:
        nooper = Nooper()
        assert TypeId.NOOPER == nooper.cid()
