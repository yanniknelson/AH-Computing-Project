import pygame
from button_class import *
from basic_Resources import *
import settings_Page as sp
import instructions_Page as ip
import game_Page as gp
import time

pygame.init()

#Image object for the background image
Background = Image('resources/sprite_Images/Background.png', 480, 360)
#instructions, game and settigns buttons
I_button = Button("Instructions", 156, 645, 164, 62)
G_button = Button("New Game", 480, 645, 164, 62)
S_button = Button("Settings", 821, 645, 164, 62)
#text objects
Title = Text("SPACE INVADERS", 72, 480, 106)
Sub_Title = Text("These are the aliens you'll encounter:", 32, 480, 228)
mother_text = Text("This can be worth 50, 100, 150 or 300 points", 16, 560, 318)
thirty_text = Text("This alien is worth 30 points", 16, 472, 368)
twenty_text = Text("This alien is worth 20 points", 16, 472, 418)
ten_text = Text("This alien is worth 10 points", 16, 472, 468)
#image objects
mother_ship_img = Image('resources/sprite_Images/aliens/mother_Ship.png', 250, 318)
thirty_img = Image('resources/sprite_Images/aliens/30pts_Open.png', 250, 368)
twenty_img = Image('resources/sprite_Images/aliens/20pts_Open.png', 250, 418)
ten_img = Image('resources/sprite_Images/aliens/10pts_Open.png', 250, 468)
mother_ship_img.resize_Image(2)
thirty_img.resize_Image(2)
twenty_img.resize_Image(2)
ten_img.resize_Image(2)

def draw_page():
    print("drawn")
    #display backround image
    Background.display_Image()
    #display text objects
    Title.display_text()
    Sub_Title.display_text()
    mother_text.display_text()
    thirty_text.display_text()
    twenty_text.display_text()
    ten_text.display_text()
    #display buttons
    I_button.display_Button()
    G_button.display_Button()
    S_button.display_Button()
    #display image objects
    mother_ship_img.display_Image()
    thirty_img.display_Image()
    twenty_img.display_Image()
    ten_img.display_Image()
    #update display
    pygame.display.flip()

def run_page():
    #draw the page
    draw_page()
    #wait 0.1 seconds
    time.sleep(0.1)
    #loop the keep the page open and run the checks
    while True:
            #check if the mouse is over any of the buttons
            #if clicked run the instructions page
            I_button.hover_Check(draw_page, ip.run_page)
            #if clicked run the game page
            G_button.hover_Check(draw_page, gp.run_page)
            #if clicked run the settings page
            S_button.hover_Check(draw_page, sp.run_page)

            #if the quit button is clicked quit the game
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            pygame.display.quit()
                            pygame.quit()
                            sys.exit()
