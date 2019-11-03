"""
Unit tests for the engine.
"""

from turpyno.engine import EngineFactory


class TestEngine:
    def test_engine(self) -> None:

        engine_factory = EngineFactory(True)
        engine_factory.initialize()
        engine = engine_factory.create(500, 500)

        assert engine
