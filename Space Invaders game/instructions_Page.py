import pygame
from button_class import *
from basic_Resources import *
import home_Page as hp
from basic_Resources import *

pygame.init()
#image object for background image
Background = Image('resources/sprite_Images/Background.png', 480, 360)
#back button
back_button = Button("Back", 80, 40)

#text objects containing instructions
Title = Text("INSTRUCTIONS", 72, 480, 106)

C_SubTitle = Text("CONTROLS:", 32, 144, 186)
C_text_one = Text("to move your character left and right use the a and d buttons", 16, 402, 226)
C_text_two = Text("or the left and right arrow keys. to shoot press spacebar.", 16, 384, 246)


WW_SubTitle = Text("WHAT'S WHAT:", 32, 180, 306)
WW_text_one = Text("The creatures at the top of the screen are ALIENS, there is also", 16, 420, 346)
WW_text_two = Text("a MOTHERSHIP that occasionally travels across the top of the screen.", 16, 444, 366)
WW_text_three = Text("The green arches are your BUNKERS. YOU are the GREEN PUCK that", 16, 408, 386)
WW_text_four = Text("moves side to side near the bottom of the screen.", 16, 330, 406)

WD_SubTitle = Text("WHAT TO DO:", 32, 168, 466)
WD_text_one = Text("The aim of the game is to KILL all of the ALIENS before they reach", 16, 432, 506)
WD_text_two = Text("your BUNKERS. There are 3 types of ALIENS, KILLING each one will reward", 16, 462, 526)
WD_text_three = Text("a different amount of points. You KILL the ALIENS by SHOOTING them ", 16, 438, 546)
WD_text_four = Text("BUT they can SHOOT YOU too. If YOU get HIT you DIE and lose a LIFE,", 16, 438, 566)
WD_text_five = Text("YOU have 3 LIVES in total, when you run out of LIVES where the game ENDS.", 16, 474, 586)
WD_text_six = Text("As the ALIENS get closer to your BUNKERS they will SPEED UP.", 16, 396, 606)
WD_text_seven = Text("Once you’ve KILLED all the ALIENS a new WAVE will begin", 16, 364, 626)
WD_text_eight = Text("the ALIENS’ STARTING SPEED is FASTER, this repeats until the game ends.", 16, 460, 646)

#array of all the text objects for easier access later
Instructions = (C_SubTitle, C_text_one, C_text_two,
                WW_SubTitle, WW_text_one, WW_text_two, WW_text_three, WW_text_four,
                WD_SubTitle, WD_text_one, WD_text_two, WD_text_three, WD_text_four, WD_text_five,
                WD_text_six, WD_text_seven, WD_text_eight)

def draw_page():
    #display the background image
    Background.display_Image()
    #display the back button
    back_button.display_Button()
    #display the title
    Title.display_text()
    #runs throught the array of text calling display on every element
    for text in Instructions:
        text.display_text()
    #update the display
    pygame.display.flip()

def run_page():
    #draw the page
    draw_page()
    #loop the keep the page open and run checks
    while True:
            #check if the mouse is over the  back button
            #if clicked run the home page
            back_button.hover_Check(draw_page, hp.run_page)

            #if the quit button is clicked quit the game
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            pygame.display.quit()
                            pygame.quit()
                            sys.exit()
