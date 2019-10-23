"""
Unit tests for entities.
"""

from turpyno.component import IdentifierContext, IdentifierFactory
from turpyno.entity import EntityFactory


class TestEntity:
    def test_create_entity(self) -> None:
        entity_factory = EntityFactory()
        identifier_factory = IdentifierFactory()
        context = IdentifierContext("Entity a")
        identifier = identifier_factory.create(context)
        entity = entity_factory.create([identifier])
        assert entity is not None
