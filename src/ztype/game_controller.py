import pygame
from pygame.locals import QUIT, KEYDOWN
import sys

from ztype.level import Level
from ztype.words_manager import WordsManager
from ztype.config import *
from ztype.score_tracker import ScoreTracker


class GameController(object):
    """
    Responsible for running the game -
    displaying frames and handling events
    """

    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.font = pygame.font.SysFont(BASIC_FONT, FONT_SIZE)
        self.screen = self.initialize_display()
        self.words_group = pygame.sprite.RenderPlain()
        self.level = Level(LEVEL_WORD_COUNT, LEVEL_SPEED, LEVEL_FREQUENCY, WORD_LENGTH)
        self.words_manager = WordsManager(self.level, self.words_group)
        self.score_tracker = ScoreTracker()
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
        icon_surface = pygame.image.load(ICON_PATH).convert_alpha()
        pygame.display.set_icon(icon_surface)
        return screen

    def write_message(self, messages, width, height):
        """
        Writes a list of messages to screen (each message in a new line)
        :param messages: list<strings>
        :param width: int
        :param height: int
        """
        self.screen.fill(BLACK)
        for msg in messages:
            text_surface = self.font.render(msg, True, WHITE)
            text_rect = text_surface.get_rect()
            text_rect.center = (width, height)
            height = height + LINE_SPACING
            self.screen.blit(text_surface, text_rect)
        pygame.display.update()

    def remove_words_exceed_screen(self):
        """
        Removes words from the words group if their y value
        is bigger than the screen height
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
                self.score_tracker.correct_letter_typed()
                self.current_typed_word.on_letter_typed(key_letter)
            else:
                self.score_tracker.incorrect_letter_typed()
            if self.current_typed_word.is_fully_typed():
                self.current_typed_word.remove(self.words_group)
                self.current_typed_word = None
        else:
            self.score_tracker.incorrect_letter_typed()

    def set_next_current_typed_word(self, key_letter):
        """
        Determines which of the possible words is currently being
        typed by the user
        :param key_letter: string
        """
        words_starts_with_letter = self.words_manager.get_displayed_words_starting_with_letter(key_letter)
        if words_starts_with_letter:
            self.current_typed_word = self.words_manager.get_lowest_y_axis_word(words_starts_with_letter)

    @staticmethod
    def restart():
        """
        Restarts the game by calling another instance of the controller
        :return:
        """
        GameController().run()

    @staticmethod
    def terminate():
        """
        Terminates the game and exits the program
        """
        pygame.quit()
        sys.exit()

    def run(self):
        """
        Runs the main loop.
        Updates the screen display every tick.
        """
        while True:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                self.handle_main_menu_events(event)
                if event.type == KEYDOWN:
                    self.handle_key_down_events(event.unicode)

            self.run_one_frame()
            self.screen.fill(SCREEN_BACKGROUND)
            self.words_group.draw(self.screen)
            if self.is_level_complete():
                self.on_level_complete()
            pygame.display.update()

    def is_level_complete(self):
        """
        Checks if the user has managed to type all of the words,
        and if so writes a simple message to screen
        """
        return not self.words_group
        # if not self.words_group:
        #     self.write_message([YOU_WIN, RESTART], *MIDDLE)
        #     self.write_message([str(self.score_tracker.get_accuracy())], CENTER_WIDTH, CENTER_HEIGHT + 100)

    def on_level_complete(self):
        pass

    def on_game_over(self):
        """
        Display final score.
        """
        accuracy = self.score_tracker.get_accuracy()
        while True:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                self.handle_main_menu_events(event)
            self.display_score(accuracy)

    def display_score(self, accuracy):
        """
        Display final score.
        :param accuracy: Game accuracy score.
        """
        self.write_message([str(accuracy)], CENTER_WIDTH, CENTER_HEIGHT + 100)

    def handle_main_menu_events(self, event):
        """
        Event handler for events such as quit or restart.
        :param event: pygame event.
        """
        if event.type == QUIT or (event.type == KEYDOWN and event.key == pygame.K_ESCAPE):
            self.terminate()
        elif event.type == KEYDOWN:
            if event.key == pygame.K_INSERT:
                self.restart()


def main():
    game_controller = GameController()
    game_controller.run()


if __name__ == '__main__':
    main()
