import pygame
from pygame.locals import QUIT, KEYDOWN

from ztype.level import Level
from ztype.words_manager import WordsManager
from ztype.config import *


class GameController(object):
    """
    Responsible for running the game -
    displaying frames and handling events
    """

    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.screen = self.initialize_display()
        self.words_group = pygame.sprite.RenderPlain()
        self.level = Level(LEVEL_WORD_COUNT, LEVEL_SPEED, LEVEL_FREQUENCY, WORD_LENGTH)
        self.words_manager = WordsManager(self.level, self.words_group)
        self.clock = pygame.time.Clock()
        self.current_typed_word = None

    @staticmethod
    def initialize_display():
        """
        Initializes the display by updating its size, title and icon
        :return: Surface
        """
        screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption(ZTYPE_CAPTION)
        icon_surface = pygame.image.load(ICON_PATH)
        pygame.display.set_icon(icon_surface)
        return screen

    def remove_words_exceed_screen(self):
        """
        Removes words from the words group if their y value
        is bigger than the screen height
        :return:
        """
        map(lambda word: word.remove(self.words_group),
            filter(lambda word: word.rect.bottom > SCREEN_HEIGHT, self.words_group.sprites()))

    def run_one_frame(self):
        """
        Drop words down the screen
        """
        self.words_group.update()
        self.remove_words_exceed_screen()

    def handle_key_down_events(self, key_letter):
        """
        A simple key strokes listener that follows the user's typing
        :param key_letter: string
        """
        if (not self.current_typed_word) or (self.current_typed_word not in self.words_group.sprites()):
            self.set_next_current_typed_word(key_letter)

        if self.current_typed_word:
            if self.current_typed_word.is_typed_letter_is_next(key_letter):
                self.current_typed_word.on_letter_typed(key_letter)

            if self.current_typed_word.is_fully_typed():
                self.current_typed_word.remove(self.words_group)
                self.current_typed_word = None

    def set_next_current_typed_word(self, key_letter):
        """
        Determines which of the possible words is currently being
        typed by the user
        :param key_letter: string
        """
        words_starts_with_letter = self.words_manager.get_displayed_words_starting_with_letter(key_letter)
        if words_starts_with_letter:
            self.current_typed_word = self.words_manager.get_lowest_y_axis_word(words_starts_with_letter)

    def run(self):
        """
        Runs the main loop.
        Updates the screen display every tick.
        """
        while True:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                elif event.type == KEYDOWN:
                    self.handle_key_down_events(event.unicode)

            self.run_one_frame()
            self.screen.fill(SCREEN_BACKGROUND)
            self.words_group.draw(self.screen)
            pygame.display.update()


def main():
    game_controller = GameController()
    game_controller.run()


if __name__ == '__main__':
    main()
