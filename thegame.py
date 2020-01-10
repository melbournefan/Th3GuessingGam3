from random import seed
from asciimatics.screen import Screen

def mainscreen(screen):
    screen.print_at('Th3GuessingGam3', 0, 0)
    screen.refresh()

Screen.wrapper(mainscreen)