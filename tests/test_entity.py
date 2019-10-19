"""
Unit tests for entities.
"""

from turpyno.component import IdentifierContext
from turpyno.entity import EntityFactory


class TestEntity:
    def test_create_entity(self) -> None:
        entity_factory = EntityFactory()
        identifier_context = IdentifierContext("Entity a")
        entity = entity_factory.build(identifier_context)
        assert entity is not None
