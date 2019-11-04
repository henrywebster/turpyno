"""
App class for running windows.
"""
import pygame  # type: ignore


from turpyno.engine import Engine


class App:  # pylint: disable=too-few-public-methods
    """Main app class."""

    def __init__(self, engine: Engine) -> None:
        self._engine = engine

    def run(self) -> None:  # pylint: disable=no-self-use
        """Runs the program."""

        clock = pygame.time.Clock()

        while not self._engine.stopped():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._engine.stop()
                if event.type == pygame.KEYDOWN:
                    self._engine.act(event.key)
                else:
                    print(event)

            self._engine.render()
            clock.tick()

        pygame.quit()
        print("done")
