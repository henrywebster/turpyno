"""
Unit test for scripts.
"""

from pytest import approx  # type: ignore
import numpy as np  # type: ignore
from turpyno.component import LocatorFactory, ColliderFactory
from turpyno.mover import MoverFactory
from turpyno.script import move_right, move_left, move_up, move_down


class TestScript:
    def test_move_right_default(self) -> None:
        mover_factory = MoverFactory()
        mover = mover_factory.create()
        locator_factory = LocatorFactory()
        locator = locator_factory.create()
        assert approx(np.array([0, 0, 0], dtype=np.float32)) == locator.translation()
        move = move_right(mover, locator)
        move()
        assert approx(np.array([1, 0, 0], dtype=np.float32)) == locator.translation()

    def test_move_right_obsructed(self) -> None:
        collider_factory = ColliderFactory()
        collider = collider_factory.create()
        collider.update(np.array([1, 0, 0], dtype=np.float32), 10.0)
        mover_factory = MoverFactory()
        mover = mover_factory.create(obstructs=[collider])
        locator_factory = LocatorFactory()
        locator = locator_factory.create()
        assert approx(np.array([0, 0, 0], dtype=np.float32)) == locator.translation()
        move = move_right(mover, locator)
        move()
        assert approx(np.array([0, 0, 0], dtype=np.float32)) == locator.translation()

    def test_move_left_default(self) -> None:
        mover_factory = MoverFactory()
        mover = mover_factory.create()
        locator_factory = LocatorFactory()
        locator = locator_factory.create()
        assert approx(np.array([0, 0, 0], dtype=np.float32)) == locator.translation()
        move = move_left(mover, locator)
        move()
        assert approx(np.array([-1, 0, 0], dtype=np.float32)) == locator.translation()

    def test_move_left_obsructed(self) -> None:
        collider_factory = ColliderFactory()
        collider = collider_factory.create()
        collider.update(np.array([-1, 0, 0], dtype=np.float32), 10.0)
        mover_factory = MoverFactory()
        mover = mover_factory.create(obstructs=[collider])
        locator_factory = LocatorFactory()
        locator = locator_factory.create()
        assert approx(np.array([0, 0, 0], dtype=np.float32)) == locator.translation()
        move = move_left(mover, locator)
        move()
        assert approx(np.array([0, 0, 0], dtype=np.float32)) == locator.translation()

    def test_move_up_default(self) -> None:
        mover_factory = MoverFactory()
        mover = mover_factory.create()
        locator_factory = LocatorFactory()
        locator = locator_factory.create()
        assert approx(np.array([0, 0, 0], dtype=np.float32)) == locator.translation()
        move = move_up(mover, locator)
        move()
        assert approx(np.array([0, -1, 0], dtype=np.float32)) == locator.translation()

    def test_move_up_obsructed(self) -> None:
        collider_factory = ColliderFactory()
        collider = collider_factory.create()
        collider.update(np.array([0, -1, 0], dtype=np.float32), 10.0)
        mover_factory = MoverFactory()
        mover = mover_factory.create(obstructs=[collider])
        locator_factory = LocatorFactory()
        locator = locator_factory.create()
        assert approx(np.array([0, 0, 0], dtype=np.float32)) == locator.translation()
        move = move_up(mover, locator)
        move()
        assert approx(np.array([0, 0, 0], dtype=np.float32)) == locator.translation()

    def test_move_down_default(self) -> None:
        mover_factory = MoverFactory()
        mover = mover_factory.create()
        locator_factory = LocatorFactory()
        locator = locator_factory.create()
        assert approx(np.array([0, 0, 0], dtype=np.float32)) == locator.translation()
        move = move_down(mover, locator)
        move()
        assert approx(np.array([0, 1, 0], dtype=np.float32)) == locator.translation()

    def test_move_down_obsructed(self) -> None:
        collider_factory = ColliderFactory()
        collider = collider_factory.create()
        collider.update(np.array([0, 1, 0], dtype=np.float32), 10.0)
        mover_factory = MoverFactory()
        mover = mover_factory.create(obstructs=[collider])
        locator_factory = LocatorFactory()
        locator = locator_factory.create()
        assert approx(np.array([0, 0, 0], dtype=np.float32)) == locator.translation()
        move = move_down(mover, locator)
        move()
        assert approx(np.array([0, 0, 0], dtype=np.float32)) == locator.translation()
