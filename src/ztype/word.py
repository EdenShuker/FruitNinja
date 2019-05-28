import pygame

from ztype.config import BASIC_FONT, FONT_SIZE, FONT_COLOR, FONT_HIGHLIGHT_COLOR


class Word(pygame.sprite.Sprite):
    """
    Word rectangle in game
    """

    def __init__(self, word_str, speed, *groups):
        """
        :param word_str: word string
        :param speed: speed of falling down the screen
        :param groups: groups to add this word to
        """
        super(Word, self).__init__(*groups)
        self.letters = [letter for letter in word_str]
        self.length = len(word_str)
        self.speed = speed
        self.font = pygame.font.SysFont(BASIC_FONT, FONT_SIZE)
        # Attributes required to group.draw()
        self.image = self.font.render(word_str, True, FONT_COLOR)
        self.rect = self.image.get_rect()

    def update_grid(self, x, y):
        """
        Change the x, y values of the word
        :param x: int
        :param y: int
        """
        self.rect.topleft = (x, y)

    def update(self, *args):
        """
        Move word's rectangle
        :param args: None
        """
        self.rect.move_ip(self.speed)

    def get_next_letter(self):
        """
        Returns the next letter of the word
        :return: string
        """
        return self.letters[0]

    def on_letter_typed(self, letter):
        """
        Removes the typed letter from the letters list,
        and updates the view
        :param letter: string
        """
        if self.letters[0] == letter:
            self.letters.pop(0)
            self.update_word_view()

    def update_word_view(self):
        """
        Updates the image of the word by both
        highlighting it and removing already typed letters
        """
        self.image = self.font.render(''.join(self.letters).rjust(self.length), True, FONT_HIGHLIGHT_COLOR)

    def is_typed_letter_is_next(self, letter):
        """
        Checks whether the typed letter is the next letter
        of this word
        :param letter: string
        :return: boolean
        """
        return self.letters[0] == letter

    def is_fully_typed(self):
        """
        Checks whether the word is fully typed
        :return: boolean
        """
        return len(self.letters) == 0
