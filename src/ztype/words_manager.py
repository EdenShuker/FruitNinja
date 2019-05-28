import random
import pickle

from word import Word
from config import SCREEN_WIDTH, WORDS_FILE, FONT_SIZE


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
        self._level = level
        self._generate_words(words_group)

    @staticmethod
    def _load_words_dict():
        """
        Loads the words dictionary
        :return: dict
        """
        with open(WORDS_FILE, "rb") as f:
            words_by_length = pickle.load(f)
        return words_by_length

    def _pick_random_words(self):
        """
        Chooses words to be displayed this level.
        The choice itself is somewhat random (the higher the level
        of the game, the longer the words)
        :return:
        """
        words = self._load_words_dict()
        for _ in range(self._level.words_count):
            possible_words = words[random.randint(*self._level.word_length)]
            random_index = random.randint(0, len(possible_words) - 1)
            yield possible_words[random_index]

    def _generate_words(self, words_group):
        """
        Randomly generates a list of falling words
        for the current level.
        """
        y = 0
        for word_string in self._pick_random_words():
            word = Word(word_string, self._level.falling_speed, words_group)
            self._place_word(word, y)
            y = y - self._range_between_y()

    @staticmethod
    def _place_word(word, y):
        """
        Changes the x, y values of the given word.
        """
        word.update_grid(random.randint(0, SCREEN_WIDTH - word.rect.width), y)

    def _range_between_y(self):
        """
        Return the diff between last y value to the next.
        Notice that it changes according to the level's difficulty
        :return: int
        """
        return random.randrange(FONT_SIZE, self._level.frequency)
