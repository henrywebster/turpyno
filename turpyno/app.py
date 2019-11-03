"""
App class for running windows.
"""
import pygame  # type: ignore

from pygame.locals import K_ESCAPE  # type: ignore

from turpyno.engine import Engine


class App:  # pylint: disable=too-few-public-methods
    """Main app class."""

    def __init__(self, engine: Engine) -> None:
        self._engine = engine

    def run(self) -> None:  # pylint: disable=no-self-use
        """Runs the program."""

        clock = pygame.time.Clock()
        closed = False

        while not closed:
            for event in pygame.event.get():
                if (
                    event.type == pygame.KEYDOWN and event.key == K_ESCAPE
                ) or event.type == pygame.QUIT:
                    closed = True
                if event.type == pygame.KEYDOWN:
                    self._engine.act(event.key)
                else:
                    print(event)

            self._engine.render()
            clock.tick()

        pygame.quit()
        print("done")
