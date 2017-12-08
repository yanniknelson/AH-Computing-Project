import pygame
import os
import time
from button_class import *
from basic_Resources import *


pygame.init()

#screen = pygame.display.set_mode((960, 720))
#pygame.display.set_caption("SPACE INADERS")


clock = pygame.time.Clock()
I_button = Button("Instructions", 156, 645, 164, 62)
G_button = Button("New Game", 480, 645, 164, 62)
S_button = Button("Settings", 821, 645, 164, 62)
test_button = Back_Button(300, 600)
Title = Text("SPACE INVADERS", 72, 480, 106)
Sub_Title = Text("These are the aliens you'll encounter:", 32, 480, 228)
mother_ship_img = Image('resources/sprite_Images/aliens/mother_Ship.png', 250, 318)
mother_text = Text("This can be worth 50, 100, 150 or 300 points", 16, 560, 318)
thirty_img = Image('resources/sprite_Images/aliens/30pts_Open.png', 250, 368)
thirty_text = Text("This alien is worth 30 points", 16, 472, 368)
twenty_img = Image('resources/sprite_Images/aliens/20pts_Open.png', 250, 418)
twenty_text = Text("This alien is worth 20 points", 16, 472, 418)
ten_img = Image('resources/sprite_Images/aliens/10pts_Open.png', 250, 468)
ten_text = Text("This alien is worth 10 points", 16, 472, 468)

def draw_page():
    pygame.display.get_surface().fill(Black)
    print("drawn")
    Title.display_text()
    Sub_Title.display_text()
    I_button.display_Button()
    G_button.display_Button()
    S_button.display_Button()
    mother_ship_img.display_Image()
    mother_text.display_text()
    thirty_img.display_Image()
    thirty_text.display_text()
    twenty_img.display_Image()
    twenty_text.display_text()
    ten_img.display_Image()
    ten_text.display_text()
    test_button.display_Button()
    pygame.display.flip()


def test():
    print("worked")



def run_page():
    done = False
    while not done:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            done = True

            I_button.hover_Check(draw_page, test)
            G_button.hover_Check(draw_page, test)
            S_button.hover_Check(draw_page, test)
            #done = test_button.hover_Check(draw_page)
    print("closing homepage")
