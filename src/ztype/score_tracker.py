class ScoreTracker(object):

    def __init__(self):
        self._total_letters_typed = 0
        self._total_letters_typed_correctly = 0
        self._is_last_letter_typed_correctly = True

    def correct_letter_typed(self):
        if self._is_last_letter_typed_correctly:
            self._total_letters_typed_correctly += 1
        self._total_letters_typed += 1
        self._is_last_letter_typed_correctly = True

    def incorrect_letter_typed(self):
        self._is_last_letter_typed_correctly = False

    def get_accuracy(self):
        return float(self._total_letters_typed_correctly) / self._total_letters_typed
