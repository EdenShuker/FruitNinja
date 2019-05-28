class Level(object):
    """
    Ztype level configurations
    """

    def __init__(self, words_count, falling_speed, frequency, word_length):
        """
        :param words_count: number of words
        :param falling_speed: the speed of the words falling down the screen
        :param frequency: range of starting positions to randomize from
        :param word_length: minimum length & maximum length of the words in this level
        """
        self.words_count = words_count
        self.falling_speed = falling_speed
        self.frequency = frequency
        self.word_length = word_length
