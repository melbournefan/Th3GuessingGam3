from asciimatics.screen import Screen
from random import seed
from time import sleep

def mainscreen(screen):
    screen.print_at('Th3GuessingGam3', 0, 0,)
    screen.refresh()
    sleep(10)

Screen.wrapper(mainscreen)