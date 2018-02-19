import pygame
import game_Page as gp
import home_Page as hp
from basic_Resources import *
from button_class import *

#title text object
Title = Text("Score Table", 72, 480, 106)
#text objects for highscores
first = Text("", 25, 480, 206)
second = Text("", 25, 480, 246)
third = Text("", 25, 480, 286)
forth = Text("", 25, 480, 326)
fifth = Text("", 25, 480, 366)
sixth = Text("", 25, 480, 406)
seventh = Text("", 25, 480, 446)
eighth = Text("", 25, 480, 486)
nineth = Text("", 25, 480, 526)
thenth = Text("", 25, 480, 566)
#array of all highscore text objects
text = [first, second, third, forth, fifth, sixth, seventh, eighth, nineth, thenth]
#home and newgame buttons
home_button = Button("Home", 160, 650, 164, 62)
new_game_button = Button("New Game", 800, 650, 164, 62)
#ScoreBoard object
highscores = ScoreBoard()

#a procedure to pass into the change text mothods called on the text objects
#to avoid drawing the page too soon
def decoy_draw():
    pass

def draw_page():
    #fill the background with black
    pygame.display.get_surface().fill((0,0,0))
    #display the title
    Title.display_text()
    #run through the text array and diplay all the text objects in it
    for score in text:
        score.display_text()
    #display home and new game buttons
    home_button.display_Button()
    new_game_button.display_Button()

    #update the display
    pygame.display.flip()

def run_page():
    #get the highscores from the highscores file
    highscores.get_highscores()
    #for every index in the highscores scores array
    for count in range(len(highscores.scores)):
        #so long as the count doesn't go out of range
        if count < 10:
            #change the text object at the index count to display the highscore at the index count
            text[count].change_text(highscores.scores[count].name + " " + str(highscores.scores[count].value), decoy_draw)
            #change the x position of the text object to 415
            text[count].position[0] = 415
    #draw the page
    draw_page()
    #waite 0.1 seconds
    time.sleep(0.1)
    while True:
        #check if the mouse is hovering over the buttons
        home_button.hover_Check(draw_page, hp.run_page)
        new_game_button.hover_Check(draw_page, gp.run_page)

        #if the close button is clicked quit the game
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.display.quit()
                        pygame.quit()
                        sys.exit()
