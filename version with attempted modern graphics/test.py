import pygame
import os
pygame.init()

screen = pygame.display.set_mode((960, 720))
pygame.display.set_caption("SPACE INADERS")
import highscore_display_Page as hp

hp.run_page()
