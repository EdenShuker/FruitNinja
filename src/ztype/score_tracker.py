class ScoreTracker(object):
    """
    Tracks after game's score.
    """

    def __init__(self):
        """
        Constructor.
        """
        self._total_letters_typed = 0
        self._total_letters_typed_correctly = 0
        self._is_last_letter_typed_correctly = True

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
        return float(self._total_letters_typed_correctly) / self._total_letters_typed
