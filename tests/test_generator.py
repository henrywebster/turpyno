"""
Unit tests for Turpyno generators.
"""

from turpyno.generator import unique_id


class TestGenerator:

    def test_unique_id(self) -> None:
        generator = unique_id()
        assert 0 == next(generator)
        assert 1 == next(generator)
        assert 2 == next(generator)

    def test_instance_unique_id(self) -> None:
        generator_a = unique_id()
        generator_b = unique_id()

        assert 0 == next(generator_a)
        assert 0 == next(generator_b)
