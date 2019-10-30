"""
Unit tests for the engine.
"""

from turpyno.engine import Engine, VideoMode
from turpyno.component import IdentifierContext


class TestEngine:
    def test_engine(self) -> None:

        engine = Engine(500, 500)
        engine.setup(VideoMode.NOOP)

        assert 0 == len(engine.entities())

        context = IdentifierContext("square")
        identifier = engine.create_identifier(context)
        entity = engine.create_entity([identifier])

        assert 1 == len(engine.entities())
        assert entity == engine.entities()[0]
