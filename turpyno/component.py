"""
Unit tests for the component class.
"""

from enum import Enum
from turpyno.generator import unique_id


class TypeId(Enum):
    IDENTIFIER = 1


class Component:
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
        return self._eid

    def name(self) -> str:
        return self._name


class ComponentContext:
    def __init__(self, type_id: TypeId) -> None:
        self._type_id = type_id


class IdentifierContext(ComponentContext):
    def __init__(self, name: str = "anon") -> None:
        super().__init__(TypeId.IDENTIFIER)
        self._name = name

    def name(self) -> str:
        return self._name


class IdentifierFactory:
    def __init__(self) -> None:
        self._generator = unique_id()

    def create(self, context: IdentifierContext) -> Identifier:
        """Create a new named identifier."""
        return Identifier(next(self._generator), context.name())
