from word import Word


class Board(object):
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
