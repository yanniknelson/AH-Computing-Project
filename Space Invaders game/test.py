import pygame
import os
from basic_Resources import *
pygame.init()

screen = pygame.display.set_mode((960, 720))
pygame.display.set_caption("SPACE INADERS")
highscore = ScoreBoard()
highscore.get_highscores()
highscore.current_score = 0
import highscore_input_Page as hp

hp.run_page(highscore)
