"""
Unit tests for the component class.
"""

from enum import Enum
from typing import NamedTuple
from turpyno.generator import unique_id


class TypeId(Enum):
    """Types enum for components."""

    IDENTIFIER = 1


IdentifierContext = NamedTuple("IdentifierContext", [("name", str)])


class Component:  # pylint: disable=too-few-public-methods
    """Super class for all components."""

    def __init__(self, type_id: TypeId):
        self.type = type_id

    def cid(self) -> TypeId:
        """Return the unique identifier for this component type."""
        return self.type


class Identifier(Component):
    """Component that identifies."""

    def __init__(self, eid: int, name: str) -> None:
        super().__init__(TypeId.IDENTIFIER)
        self._eid = eid
        self._name = name

    def eid(self) -> int:
        """Return the entity id field."""
        return self._eid

    def name(self) -> str:
        """Return the name field."""
        return self._name


class IdentifierFactory:  # pylint: disable=too-few-public-methods
    """Factory method for identifier components."""

    def __init__(self) -> None:
        self._generator = unique_id()

    def create(self, context: IdentifierContext) -> Identifier:
        """Create a new named identifier."""
        return Identifier(next(self._generator), context.name)
