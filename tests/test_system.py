"""
Unit tests for systems.
"""

from typing import Callable, Generator
from pygame import Surface  # type: ignore
from pygame.font import Font, get_default_font, init, quit  # type: ignore
from pytest import fixture  # type: ignore
from turpyno.component import IdentifierFactory, LocatorFactory
from turpyno.entity import EntityFactory
from turpyno.renderer import RendererFactory
from turpyno.system import RenderSystemFactory
from turpyno.menu import MenuItemFactory


@fixture(scope="module", autouse=True)
def init_fonts() -> Generator:
    init()
    yield None
    quit()


class TestSystem:
    def test_render_system(self) -> None:

        font = Font(get_default_font(), 12)
        system_factory = RenderSystemFactory()
        s: Callable[[Surface], RendererFactory] = lambda surface: RendererFactory(
            surface
        )
        m: Callable[[Surface], MenuItemFactory] = lambda surface: MenuItemFactory(
            surface, font
        )
        system = system_factory.create(Surface((1, 1)), s, m)

        identifier_factory = IdentifierFactory()
        identifier = identifier_factory.create("entity a")
        renderer_factory = system.renderer_factory()
        renderer = renderer_factory.create_rectangle()
        locator_factory = LocatorFactory()
        locator = locator_factory.create()
        entity_factory = EntityFactory()
        entity = entity_factory.create([identifier, renderer, locator])

        assert system.handles(entity)
        system.register(entity)
