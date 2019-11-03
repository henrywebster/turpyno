"""
Unit test for recipes.
"""

from pytest import approx  # type: ignore
import numpy as np  # type: ignore
from turpyno.component import LocatorFactory, ColliderFactory
from turpyno.mover import MoverFactory
from turpyno.recipe import move


class TestRecipe:
    def test_move_default(self) -> None:
        mover_factory = MoverFactory()
        mover = mover_factory.create()
        locator_factory = LocatorFactory()
        locator = locator_factory.create()
        assert approx(np.array([0, 0, 0], dtype=np.float32)) == locator.translation()

        move(mover, locator, np.array([1, 0, 0]))
        assert approx(np.array([1, 0, 0], dtype=np.float32)) == locator.translation()

    def test_move_obsructed(self) -> None:
        collider_factory = ColliderFactory()
        collider = collider_factory.create()
        collider.update(np.array([1, 0, 0], dtype=np.float32), 10.0)
        mover_factory = MoverFactory()
        mover = mover_factory.create(obstructs=[collider])
        locator_factory = LocatorFactory()
        locator = locator_factory.create()
        assert approx(np.array([0, 0, 0], dtype=np.float32)) == locator.translation()

        move(mover, locator, np.array([1, 0, 0]))
        assert approx(np.array([0, 0, 0], dtype=np.float32)) == locator.translation()
