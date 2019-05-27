class Level(object):
    """
    Ztype level configurations.
    """

    def __init__(self, words_count, falling_speed, frequency):
        """
        Constructor.
        :param words_count: Number of words.
        :param falling_speed: The speed of the words falling down the screen.
        :param frequency: Range of starting positions to randomize from.
        """
        self.words_count = words_count
        self.falling_speed = falling_speed
        self.frequency = frequency
