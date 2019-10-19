"""
Unit tests for the component class.
"""

from enum import Enum
from turpyno.generator import unique_id


class TypeId(Enum):
    NOOPER = 1,
    IDENTIFIER = 2


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


class Identifier(Component):
    """Component that identifies."""

    def __init__(self, eid: int, name: str) -> None:
        super().__init__(TypeId.IDENTIFIER)
        self._eid = eid
        self._name = name

    def eid(self) -> int:
        return self._eid

    def name(self) -> str:
        return self._name


class IdentifierFactory:

    def __init__(self) -> None:
        self._generator = unique_id()

    def create(self, name: str = "anon") -> Identifier:
        """Create a new named identifier."""
        return Identifier(next(self._generator), name)
