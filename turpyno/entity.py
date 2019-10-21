"""
Class for entities.
"""

from typing import Collection, NamedTuple
from turpyno.component import Component, IdentifierContext, IdentifierFactory

Entity = NamedTuple("Entity", [("components", Collection[Component])])


class EntityFactory:  # pylint: disable=too-few-public-methods
    """Factory for creating entities."""

    identifier_factory = IdentifierFactory()

    def build(  # pylint: disable=no-self-use
        self, context: IdentifierContext  # pylint: disable=bad-continuation
    ) -> Entity:
        """Build an entity with just an identifier component."""
        identifier = EntityFactory.identifier_factory.create(context)
        return Entity([identifier])
