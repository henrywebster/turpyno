"""
Unit tests for the component class.
"""

from enum import Enum


class TypeId(Enum):
    NOOPER = 1


class Component:
    """Super class for all components."""

    def __init__(self, type_id: TypeId):
        self.type = type_id

    def cid(self) -> TypeId:
        """Return the unique identifier for this component type."""
        return self.type


class Nooper(Component):
    """A component that does nothing"""

    def __init__(self) -> None:
        super().__init__(TypeId.NOOPER)
