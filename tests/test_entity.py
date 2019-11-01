"""
Unit tests for entities.
"""

import pytest  # type: ignore

from turpyno.component import IdentifierFactory, Identifier
from turpyno.entity import EntityFactory, EntityError
from turpyno.renderer import Renderer


class TestEntity:
    def test_create_entity(self) -> None:
        entity_factory = EntityFactory()
        identifier_factory = IdentifierFactory()
        identifier = identifier_factory.create("Entity a")
        entity = entity_factory.create([identifier])
        assert entity.has(Identifier)
        assert not entity.has(Renderer)
        assert identifier == entity.get(Identifier)

    def test_entity_no_type(self) -> None:
        entity_factory = EntityFactory()
        identifier_factory = IdentifierFactory()
        identifier = identifier_factory.create("Entity a")
        entity = entity_factory.create([identifier])
        assert entity.has(Identifier)
        assert not entity.has(Renderer)
        with pytest.raises(EntityError):
            entity.get(Renderer)
