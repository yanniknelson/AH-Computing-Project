import pygame
from button_class import *
from basic_Resources import *
import home_Page as hp
from basic_Resources import *

pygame.init()

Background = Image('resources/sprite_Images/Background.png', 480, 360)
back_button = Button("Back", 80, 40)
Title = Text("SETTINGS", 72, 480, 106)
music_Text = Text("Music:", 32, 200, 225)
music_button = Button("", 372, 225, 160)
musictype_Text = Text("Music Type:", 32, 365, 285)
musictype_button = Button("", 600, 285, 160)
effects_Text = Text("Sound Effects:", 32, 296, 375)
effects_button = Button("", 564, 375, 160)
graphics_Text = Text("Graphics:", 32, 236, 465)
graphics_button = Button("", 444, 465, 160)
settingsvar = Settings()

def musicstate_text():
    if settingsvar.musicstate:
        music_button.text.change_text("On", draw_page)
    else:
        music_button.text.change_text("Off", draw_page)

def musictype_text():
    if settingsvar.musictype == 1:
        musictype_button.text.change_text("SciFi", draw_page)
    else:
        musictype_button.text.change_text("popDance", draw_page)

def effects_text():
    if settingsvar.soundeffects:
        effects_button.text.change_text("On", draw_page)
    else:
        effects_button.text.change_text("Off", draw_page)

def graphics_text():
    if settingsvar.graphics:
        graphics_button.text.change_text("Classic", draw_page)
    else:
        graphics_button.text.change_text("Modern", draw_page)

def switch_music():
    settingsvar.musicstate = not settingsvar.musicstate
    print(settingsvar.musicstate)
    musicstate_text()

def change_music():
    settingsvar.musictype = (settingsvar.musictype + 1) % 2
    print(str(settingsvar.musictype))
    musictype_text()

def switch_effects():
    settingsvar.soundeffects = not settingsvar.soundeffects
    print(settingsvar.soundeffects)
    effects_text()

def switch_graphics():
    settingsvar.graphics = not settingsvar.graphics
    print(settingsvar.graphics)
    graphics_text()

def draw_page():
    print("drawn")
    Background.display_Image()
    Title.display_text()
    back_button.display_Button()
    music_Text.display_text()
    music_button.display_Button()
    musictype_Text.display_text()
    musictype_button.display_Button()
    effects_Text.display_text()
    effects_button.display_Button()
    graphics_Text.display_text()
    graphics_button.display_Button()
    pygame.display.flip()

def exit_page():
    settingsvar.write_file(True)
    hp.run_page()


def run_page():
    settingsvar.get_settings()
    musicstate_text()
    musictype_text()
    effects_text()
    graphics_text()
    draw_page()
    while True:
            back_button.hover_Check(draw_page, exit_page)
            music_button.hover_Check(draw_page, switch_music)
            musictype_button.hover_Check(draw_page, change_music)
            effects_button.hover_Check(draw_page, switch_effects)
            graphics_button.hover_Check(draw_page, switch_graphics)
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            settingsvar.write_file(True)
                            pygame.display.quit()
                            pygame.quit()
                            sys.exit()


#########################                                          GO TO sqlzoo.net
