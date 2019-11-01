"""
Unit tests for the component class.
"""

from enum import Enum
from turpyno.generator import unique_id


class TypeId(Enum):
    """Types enum for components."""

    IDENTIFIER = (1,)
    RENDERER = 2


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
        self._alive = False

    def eid(self) -> int:
        """Return the entity id field."""
        return self._eid

    def name(self) -> str:
        """Return the name field."""
        return self._name

    def alive(self) -> bool:
        """Return if the entity is alive."""
        return self._alive

    def toggle(self) -> bool:
        """Switch to opposite state and return the new value."""
        self._alive = not self._alive
        return self._alive


class IdentifierFactory:  # pylint: disable=too-few-public-methods
    """Factory method for identifier components."""

    def __init__(self) -> None:
        self._generator = unique_id()

    def create(self, name: str) -> Identifier:
        """Create a new named identifier."""
        return Identifier(next(self._generator), name)
