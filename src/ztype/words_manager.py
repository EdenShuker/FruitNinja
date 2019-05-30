import random
import pickle

from ztype.word import Word
from ztype.config import SCREEN_WIDTH, WORDS, FONT_SIZE


class WordsManager(object):
    """
    Words manager that holds all of the words per level.
    Responsible for choosing words randomly and also
    placing them on screen.
    """

    def __init__(self, level, words_group):
        """
        :param level: level configuration
        :param words_group: the group of words
        """
        self._level = level
        self._words_group = words_group
        self._generate_words(words_group)

    @staticmethod
    def _load_words_dict():
        """
        Loads the words dictionary
        :return: dict
        """
        with open(WORDS, "rb") as f:
            words_by_length = pickle.load(f)
        return words_by_length

    def _pick_random_words(self):
        """
        Chooses the words strings to be displayed this level.
        The choice itself is somewhat random (the higher the level, the longer the words)
        """
        words = self._load_words_dict()
        for _ in range(self._level.words_count):
            possible_words = words[random.randint(*self._level.word_length)]
            random_index = random.randint(0, len(possible_words) - 1)
            yield possible_words[random_index]

    def _generate_words(self, words_group):
        """
        Randomly generates the falling words of the current level.
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
        Returns the difference between the last y value to the next.
        Notice that its value depends on the level's difficulty
        :return: int
        """
        return random.randrange(FONT_SIZE, self._level.frequency)

    def get_displayed_words_starting_with_letter(self, letter):
        """
        Returns a list of the displayed words that starts with
        the given letter
        :param letter: string
        :return: list
        """
        return list(
            filter(lambda word: word.get_next_letter() == letter and word.rect.top > -1, self._words_group.sprites()))

    @staticmethod
    def get_lowest_y_axis_word(words):
        """
        Returns the word with the lowest y value
        (i.e the word closest to the bottom of the screen)
        :param words: list
        :return: Word
        """
        return sorted(words, key=lambda word: word.rect.bottom, reverse=True)[0]
