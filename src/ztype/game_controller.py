import pygame
from pygame.locals import QUIT
from level import Level
from board import Board
from config import FPS, SCREEN_SIZE, WHITE, LEVEL_WORD_COUNT, \
    LEVEL_FREQUENCY, LEVEL_SPEED, SCREEN_BACKGROUND, SCREEN_HEIGHT


class GameController(object):
    """
    Responsible on running the game - displaying frames and handling events
    """

    def __init__(self):
        """
        Constructor.
        """
        pygame.init()
        pygame.font.init()
        self.words_group = pygame.sprite.RenderPlain()
        self.level = Level(LEVEL_WORD_COUNT, LEVEL_SPEED, LEVEL_FREQUENCY)
        self.board = Board(self.level, self.words_group)
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.clock = pygame.time.Clock()

    def remove_words_exceed_screen(self):
        map(lambda word: word.remove(self.words_group),
            filter(lambda word: word.rect.bottom > SCREEN_HEIGHT, self.words_group.sprites()))

    def run_one_frame(self):
        """
        Drop words down the screen.
        """
        self.words_group.update()
        self.remove_words_exceed_screen()

    def run(self):
        """
        Run main loop. Every tick update screen display.
        """
        while True:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == QUIT:
                    return

            self.run_one_frame()
            self.screen.fill(SCREEN_BACKGROUND)
            self.words_group.draw(self.screen)
            pygame.display.update()


def main():
    """
    Run game.
    """
    game_controller = GameController()
    game_controller.run()


if __name__ == '__main__':
    main()
