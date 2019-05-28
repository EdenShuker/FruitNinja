import random
import pickle

from word import Word
from config import SCREEN_WIDTH, WORDS_FILE, DISPLAY_WIDTH, FONT_SIZE


class WordsManager(object):
    """
    Words manager game holding all words.
    Responsible for choosing words randomly and also
    placing them on screen.
    """

    def __init__(self, level, words_group):
        """
        Constructor.
        :param level: Level configuration.
        :param words_group: The group of words.
        """
        self.level = level
        self.words_group = words_group
        self.words = self.generate_words()
        self.determine_words_grid()

    @staticmethod
    def load_words_dict():
        """
        Loads the words dictionary
        :return: dict
        """
        with open(WORDS_FILE, "rb") as f:
            words_by_length = pickle.load(f)
        return words_by_length

    def pick_random_words(self):
        """
        Chooses words to be displayed this level.
        The choice itself is somewhat random (the higher the level
        of the game, the longer the words)
        :return:
        """
        words = self.load_words_dict()
        for _ in range(self.level.words_count):
            possible_words = words[random.randint(*self.level.word_length)]
            random_index = random.randint(0, len(possible_words) - 1)
            yield possible_words[random_index]

    def generate_words(self):
        """
        Randomly generates a list of falling words
        for the current level.
        """
        return [Word(word, self.level.falling_speed, self.words_group) for word in self.pick_random_words()]

    def determine_words_grid(self):
        """
        Changes the x, y values of each word.
        :return:
        """
        y = 0
        for word in self.words:
            word.update_grid(random.randint(0, DISPLAY_WIDTH), y)
            y = y - self.range_between_y()

    def range_between_y(self):
        """
        Return the diff between last y value to the next.
        Notice that it changes according to the level's difficulty
        :return: int
        """
        return random.randrange(FONT_SIZE, self.level.frequency)
