"""
Unit tests for the engine.
"""

from turpyno.engine import EngineFactory
from turpyno.component import IdentifierFactory
from turpyno.keymap import Keymap


class TestEngine:
    def test_engine(self) -> None:

        engine_factory = EngineFactory(True)
        engine_factory.initialize()
        engine = engine_factory.create(500, 500, Keymap())

        assert 0 == len(engine.entities())

        identifier_factory = IdentifierFactory()
        identifier = identifier_factory.create("square")
        entity = engine.create_entity([identifier])

        assert 1 == len(engine.entities())
        assert entity == engine.entities()[0]
