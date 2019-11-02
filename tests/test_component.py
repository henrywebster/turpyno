"""
Unit tests for components.
"""

import numpy as np  # type: ignore
from pytest import approx  # type: ignore
from pygame import Rect  # type: ignore
from turpyno.component import IdentifierFactory, LocatorFactory, ColliderFactory


class TestComponent:
    def test_identifier_named(self) -> None:
        factory = IdentifierFactory()
        identifier = factory.create("Component A")

        assert "Component A" == identifier.name()
        assert not identifier.alive()
        assert 0 == identifier.eid()

    def test_identifier_toggle(self) -> None:
        factory = IdentifierFactory()
        identifier = factory.create("Component A")
        assert "Component A" == identifier.name()
        assert not identifier.alive()
        assert 0 == identifier.eid()

        identifier.toggle()
        assert identifier.alive()
        identifier.toggle()
        assert not identifier.alive()

    def test_identifier_unqiue_id(self) -> None:
        factory = IdentifierFactory()
        identifier_a = factory.create("Component A")
        identifier_b = factory.create("Component B")

        assert "Component A" == identifier_a.name()
        assert not identifier_a.alive()
        assert 0 == identifier_a.eid()

        assert "Component B" == identifier_b.name()
        assert not identifier_b.alive()
        assert 1 == identifier_b.eid()

    def test_default_locator(self) -> None:
        factory = LocatorFactory()
        locator = factory.create()
        assert approx(np.array([0, 0, 0], dtype=np.float32)) == locator.translation()

    def test_offset_locator(self) -> None:
        factory = LocatorFactory()
        locator = factory.create(np.array([1, 1, 0]))
        assert approx(np.array([1, 1, 0], dtype=np.float32)) == locator.translation()

    def test_translate_locator(self) -> None:
        factory = LocatorFactory()
        locator = factory.create()
        assert approx(np.array([0, 0, 0], dtype=np.float32)) == locator.translation()

        locator.translate(np.array([4, 5, 0], dtype=np.float32))
        assert approx(np.array([4, 5, 0], dtype=np.float32)) == locator.translation()

        locator.translate(np.array([-4, 5, 0], dtype=np.float32))
        assert approx(np.array([-4, 5, 0], dtype=np.float32)) == locator.translation()

    def test_collider_default(self) -> None:
        factory = ColliderFactory()
        collider = factory.create()

        hitbox_a = collider.hitbox()
        assert 0 == hitbox_a.x
        assert 0 == hitbox_a.y
        assert 0 == hitbox_a.w
        assert 0 == hitbox_a.h

        hitbox_b = Rect(0, 0, 1, 1)
        assert not collider.query(hitbox_b)

    def test_collider_update(self) -> None:
        factory = ColliderFactory()
        collider = factory.create()
        collider.update(np.array([1, 1, 0], dtype=np.float32), 1.0)
        hitbox_a = collider.hitbox()
        assert 1 == hitbox_a.x
        assert 1 == hitbox_a.y
        assert 1 == hitbox_a.w
        assert 1 == hitbox_a.h

        hitbox_b = Rect(1, 1, 1, 1)
        assert collider.query(hitbox_b)
