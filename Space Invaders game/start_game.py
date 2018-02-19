import pygame
import os
pygame.init()

#create the display
screen = pygame.display.set_mode((960, 720))
#set the caption at the top of the display to "SPACE INVADERS"
pygame.display.set_caption("SPACE INADERS")
import home_Page as hp

#run the home page
hp.run_page()
