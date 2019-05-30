# display
FPS = 60
ZTYPE_CAPTION = 'Ztype'

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# screen
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 500, 640
SCREEN_BACKGROUND = BLACK
MIDDLE = CENTER_WIDTH, CENTER_HEIGHT = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
LINE_SPACING = 30

# word
BASIC_FONT = 'Consolas'
FONT_SIZE = 18
FONT_COLOR = WHITE
FONT_HIGHLIGHT_COLOR = (36, 201, 47)
WORD_BACKGROUND_COLOR = (200, 10, 10)
WORD_SPEED = [0, 1]

# levels
LEVEL_SPEED = [[0, 1], [0, 1], [0, 1], [0, 1], [0, 1]]
LEVEL_WORD_COUNT = [5, 8, 13, 18, 22]
LEVEL_FREQUENCY = [120, 140, 160, 180, 200]
LEVEL_WORDS_LENGTH = [[2, 5], [3, 6], [4, 7], [5, 8], [6, 9]]
TIME_BETWEEN_LEVELS = 1000

# files
WORDS = 'resources/words.txt'
ICON_PATH = 'resources/images/favicon.png'

# messages
START = 'Press any key to start'
GAME_OVER = 'Game Over'
YOU_WIN = 'You Win!'
RESTART = 'Press insert to restart or esc to quit'
SCORE = 'Accuracy: {}%, WPM: {}'
LEVEL = 'Level {}'
