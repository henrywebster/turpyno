"""
Unit tests for components.
"""

from turpyno.component import IdentifierFactory, Nooper, TypeId


class TestComponent:

    def test_nooper(self) -> None:
        nooper = Nooper()
        assert TypeId.NOOPER == nooper.cid()

    def test_identifier_anonymous(self) -> None:
        identifier = IdentifierFactory.create()
        assert "anon" == identifier.name()
        assert 0 == identifier.eid()
        assert TypeId.IDENTIFIER == identifier.cid()

    def test_identifier_named(self) -> None:
        identifier = IdentifierFactory.create("Component A")
        assert "Component A" == identifier.name()
        assert 0 == identifier.eid()
        assert TypeId.IDENTIFIER == identifier.cid()

    def test_identifier_unqiue_id(self) -> None:
        identifier_a = IdentifierFactory.create("Component A")
        identifier_b = IdentifierFactory.create("Component B")

        assert "Component A" == identifier_a.name()
        assert 0 == identifier_a.eid()
        assert TypeId.IDENTIFIER == identifier_a.cid()

        assert "Component B" == identifier_b.name()
        assert 1 == identifier_b.eid()
        assert TypeId.IDENTIFIER == identifier_b.cid()
