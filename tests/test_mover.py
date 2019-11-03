"""
Unit tests for mover component.
"""

from pytest import approx  # type: ignore
import numpy as np  # type: ignore
from turpyno.mover import MoverFactory
from turpyno.component import ColliderFactory


class TestMover:
    def test_default_factory(self) -> None:
        factory = MoverFactory()
        mover = factory.create()
        assert approx(np.array([0, 0, 0], dtype=np.float32)) == mover.move()

    def test_offset_factory(self) -> None:
        factory = MoverFactory()
        mover = factory.create(np.array([1, 1, 0], dtype=np.float32))
        assert approx(np.array([1, 1, 0], dtype=np.float32)) == mover.move()

    def test_target(self) -> None:
        factory = MoverFactory()
        mover = factory.create()
        assert approx(np.array([0, 0, 0], dtype=np.float32)) == mover.move()

        mover.target(np.array([1, 0, 0], dtype=np.float32))
        assert approx(np.array([1, 0, 0], dtype=np.float32)) == mover.move()

    def test_velocitize(self) -> None:
        factory = MoverFactory()
        mover = factory.create()
        assert approx(np.array([0, 0, 0], dtype=np.float32)) == mover.move()

        mover.target(np.array([0, 1, 0], dtype=np.float32))
        mover.velocitize(0)
        assert approx(np.array([0, 0, 0], dtype=np.float32)) == mover.move()

        mover.velocitize(2.0)
        assert approx(np.array([0, 2, 0], dtype=np.float32)) == mover.move()

    def test_obstructs(self) -> None:
        collider_factory = ColliderFactory()
        collider = collider_factory.create()
        mover_factory = MoverFactory()
        obstructs = [collider]
        mover = mover_factory.create(obstructs=obstructs)

        assert mover
