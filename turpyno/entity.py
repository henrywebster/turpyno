"""
Class for entities.
"""

from typing import Collection, NamedTuple, List
from turpyno.component import Component

Entity = NamedTuple("Entity", [("components", Collection[Component])])


class EntityFactory:  # pylint: disable=too-few-public-methods
    """Factory for creating entities."""

    def create(  # pylint: disable=no-self-use
        self, components: List[Component]  # pylint: disable=bad-continuation
    ) -> Entity:
        """Build an entity with just an identifier component."""
        return Entity(components)
