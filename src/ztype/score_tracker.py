import time


class ScoreTracker(object):
    """
    Tracks after game's score.
    """

    def __init__(self, time_between_levels=0):
        self._total_letters_typed = 0
        self._total_letters_typed_correctly = 0
        self._is_last_letter_typed_correctly = True
        self._total_typed_words = 0
        self._level = 1
        self._start_time = time.time()
        self._end_time = 0
        self._time_between_levels = time_between_levels

    def correct_letter_typed(self):
        """
        Called When expected letter got typed.
        If this letter typed correctly in the first try, update counter of letters typed correctly.
        """
        if self._is_last_letter_typed_correctly:
            self._total_letters_typed_correctly += 1
        self._total_letters_typed += 1
        self._is_last_letter_typed_correctly = True

    def incorrect_letter_typed(self):
        """
        Called when typed letter different from the one expected.
        """
        self._is_last_letter_typed_correctly = False

    def get_accuracy(self):
        """
        :return: Game's accuracy.
        """
        if self._total_letters_typed == 0:
            return 0
        return round(float(self._total_letters_typed_correctly) / self._total_letters_typed * 100, 2)

    def word_fully_typed(self):
        self._total_typed_words += 1

    def get_real_time_in_minutes(self):
        """
        Returns the minutes passed since the start of the game,
        without counting the breaks between levels
        :return: int
        """
        end_time = time.time() - (self._time_between_levels * self._level)
        return (end_time - self._start_time) / 60

    def get_wpm(self):
        """
        Returns the speed using the word-per-minute measure
        :return: float
        """
        return round(self._total_typed_words / self.get_real_time_in_minutes())

    def get_score(self):
        return self.get_accuracy(), self.get_wpm()
