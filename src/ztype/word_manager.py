from word import Word


class WordManager(object):
    """
    Board game holding all words.
    """

    def __init__(self, level, words_group):
        """
        Constructor.
        :param level: Level configuration.
        :param words_group: The group of words.
        """
        self.words = [Word("eden", level.falling_speed, words_group)]

    def get_all_words_starting_with_letter(self, letter):
        return filter(lambda word: word.get_next_letter() == letter, self.words)

    def get_lowest_y_axis_word(self, words):
        return sorted(words, key=lambda word: word.rect.bottom, reverse=True)[0]
