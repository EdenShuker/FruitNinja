from word import Word


class Board(object):

    def __init__(self, level, words_group):
        self.words = [Word("eden", level.falling_speed, words_group)]
