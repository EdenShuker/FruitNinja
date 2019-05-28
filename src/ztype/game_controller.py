import pygame
from pygame.locals import QUIT, KEYDOWN
from level import Level
from words_manager import WordsManager
from config import FPS, SCREEN_SIZE, LEVEL_WORD_COUNT, \
    LEVEL_FREQUENCY, LEVEL_SPEED, SCREEN_BACKGROUND, SCREEN_HEIGHT, \
    WORD_LENGTH


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
        self.level = Level(LEVEL_WORD_COUNT, LEVEL_SPEED, LEVEL_FREQUENCY, WORD_LENGTH)
        self.words_manager = WordsManager(self.level, self.words_group)
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.clock = pygame.time.Clock()
        self.current_typed_word = None

    def remove_words_exceed_screen(self):
        map(lambda word: word.remove(self.words_group),
            filter(lambda word: word.rect.bottom > SCREEN_HEIGHT, self.words_group.sprites()))

    def run_one_frame(self):
        """
        Drop words down the screen.
        """
        self.words_group.update()
        self.remove_words_exceed_screen()

    def handle_key_down_events(self, key_letter):
        if not self.current_typed_word:
            self.set_next_current_typed_word(key_letter)

        if self.current_typed_word:
            if self.current_typed_word.is_typed_letter_is_next(key_letter):
                self.current_typed_word.on_letter_typed(key_letter)

            if self.current_typed_word.is_fully_typed():
                self.current_typed_word.remove(self.words_group)
                self.current_typed_word = None

    def set_next_current_typed_word(self, key_letter):
        words_starts_with_letter = self.words_manager.get_all_words_starting_with_letter(key_letter)
        if words_starts_with_letter:
            self.current_typed_word = self.words_manager.get_lowest_y_axis_word(words_starts_with_letter)

    def run(self):
        """
        Run main loop. Every tick update screen display.
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
    """
    Run game.
    """
    game_controller = GameController()
    game_controller.run()


if __name__ == '__main__':
    main()
