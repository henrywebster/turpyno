"""
Class for entities.
"""

from typing import Collection
from turpyno.component import Component, IdentifierContext, IdentifierFactory


class Entity:
    def __init__(self, components: Collection[Component]) -> None:
        self.components = components


class EntityFactory:

    identifier_factory = IdentifierFactory()

    def build(self, context: IdentifierContext) -> Entity:
        identifier = EntityFactory.identifier_factory.create(context)
        return Entity([identifier])
