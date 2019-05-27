import pygame
from pygame.locals import QUIT
from level import Level
from board import Board
from config import FPS, SCREEN_SIZE, WHITE


class GameController(object):

    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.words_group = pygame.sprite.RenderPlain()
        self.level = Level(1, [0, 1], 1)
        self.board = Board(self.level, self.words_group)
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.clock = pygame.time.Clock()

    def run_one_frame(self):
        self.words_group.update()

    def run(self):
        while True:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == QUIT:
                    return

            self.run_one_frame()
            self.screen.fill(WHITE)
            self.words_group.draw(self.screen)
            pygame.display.update()


def main():
    game_controller = GameController()
    game_controller.run()


if __name__ == '__main__':
    main()
