import pygame
from button_class import *
from basic_Resources import *
import home_Page as hp
from basic_Resources import *

pygame.init()

#image object for the background image
Background = Image('resources/sprite_Images/Background.png', 480, 360)
#text objects
Title = Text("SETTINGS", 72, 480, 106)
music_Text = Text("Music:", 32, 200, 225)
musictype_Text = Text("Music Type:", 32, 365, 285)
effects_Text = Text("Sound Effects:", 32, 296, 375)
#back and settings buttons
back_button = Button("Back", 80, 40)
music_button = Button("", 372, 225, 160)
musictype_button = Button("", 600, 285, 160)
effects_button = Button("", 564, 375, 160)
#settings variable
settingsvar = Settings()

#procedure to change the text on the musicstate button
def musicstate_text():
    #if the musicstate is true
    if settingsvar.musicstate:
        #make the text "ON"
        music_button.text.change_text("On", draw_page)
    #otherwise
    else:
        #make the text "OFF"
        music_button.text.change_text("Off", draw_page)

#procedure to change the text on the musictype button
def musictype_text():
    #if the musictype is true
    if settingsvar.musictype:
        #make the text "SciFi"
        musictype_button.text.change_text("SciFi", draw_page)
    #otherwise
    else:
        #make the text "popDance"
        musictype_button.text.change_text("popDance", draw_page)

#procedure to change the text on the soundeffects button
def effects_text():
    #if the soundeffects is true
    if settingsvar.soundeffects:
        #make the text "ON"
        effects_button.text.change_text("On", draw_page)
    #otherwise
    else:
        #make the text "OFF"
        effects_button.text.change_text("Off", draw_page)

#procedure to change the value of the musicstate setting
def switch_music():
    #set the music state setting to its opposite
    settingsvar.musicstate = not settingsvar.musicstate
    print(settingsvar.musicstate)
    #update the musicstate button
    musicstate_text()

#procedure to change the value of the musictype setting
def change_music():
    #set the music type to its opposite
    settingsvar.musictype = not settingsvar.musictype
    print(str(settingsvar.musictype))
    #update the musictype button
    musictype_text()

#procedure to change the value of the soundeffects setting
def switch_effects():
    #set the sound effects to its opposite
    settingsvar.soundeffects = not settingsvar.soundeffects
    print(settingsvar.soundeffects)
    #update the soundeffects button
    effects_text()


def draw_page():
    print("drawn")
    #display bakcroung image
    Background.display_Image()
    #display text objects
    Title.display_text()
    music_Text.display_text()
    musictype_Text.display_text()
    effects_Text.display_text()
    #diplay buttons
    back_button.display_Button()
    music_button.display_Button()
    musictype_button.display_Button()
    effects_button.display_Button()
    #update display
    pygame.display.flip()


def exit_page():
    #write the settings to the settings file
    settingsvar.write_file(True)
    #run the homepage
    hp.run_page()


def run_page():
    #get the settings
    settingsvar.get_settings()
    #change the button text to the appropriate values
    musicstate_text()
    musictype_text()
    effects_text()
    #draw the page
    draw_page()
    while True:
            #check if the mouse is over the buttons
            #if clicked run the exit method
            back_button.hover_Check(draw_page, exit_page)
            #if clicked run the switch music method
            music_button.hover_Check(draw_page, switch_music)
            #if clicked run the change music method
            musictype_button.hover_Check(draw_page, change_music)
            #if clicked run the switch effects method
            effects_button.hover_Check(draw_page, switch_effects)

            #if the quit button is clicked quit the game
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            settingsvar.write_file(True)
                            pygame.display.quit()
                            pygame.quit()
                            sys.exit()
