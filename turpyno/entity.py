"""
Class for entities.
"""

from typing import cast, List, TypeVar, Type
from turpyno.component import Component

T = TypeVar("T", bound=Component)


class EntityError(Exception):
    """Raised when there is an issue with entities."""


class Entity:  # pylint: disable=too-few-public-methods
    """An entity is a collection of components."""

    def __init__(self, components: List[Component]) -> None:
        self._components = components

    def get(self, component_type: Type[T]) -> T:
        """Get the component from its type."""
        for component in self._components:
            if isinstance(component, component_type):
                return cast(T, component)
        raise EntityError("Entity does not have {} component.".format(component_type))

    def has(self, component_type: Type[T]) -> bool:
        """Get if the entity has a certain component."""
        for component in self._components:
            if isinstance(component, component_type):
                return True
        return False


class EntityFactory:  # pylint: disable=too-few-public-methods
    """Factory for creating entities."""

    def create(  # pylint: disable=no-self-use
        self, components: List[Component]
    ) -> Entity:
        """Build an entity with just an identifier component."""
        return Entity(components)
