import pygame
import os
import time


pygame.init()

White = (255, 255, 255)
Black = (0, 0, 0)

#Settins Class
class Settings():
    def __init__(self):
        #variables store the state of the settings
        self.musicstate = True
        self.musictype =  1
        self.soundeffects = True
        self.graphics = False

    #procedure to get the settings from the settings file
    def get_settings(self):
        #checks the settings file exists
        if not os.path.isfile("settings.txt"):
            #if the file doesn't exist create the file
            print("file not there")
            self.write_file(False)
        else:
            #if it does exist open the file and split the string
            #by commas into an array
            settingsfile = open("settings.txt", "r")
            settings = settingsfile.read().split(",")
            settingsfile.close()
            print(settings)
            #run through the array of setting strings and
            #set the state variables to the appropriate conversions of the values
            #if the string is "True" the variabel will be set to true if not it will be set to false
            self.musicstate =  settings[0] == "True"
            self.musictype =  int(settings[1])
            self.soundeffects = settings[2] == "True"
            self.graphics = settings[3] == "True"

    def write_file(self, remove):
        #if the remove variable is true (will be the case if the file already exists)
        if remove:
            #delete the file
            os.remove("settings.txt")
        #create the file again
        settings = open("settings.txt", "w")
        #fill the file with string verisions of the settings variables
        #delimited by commas for later separation
        settings.write(str(self.musicstate) + ",")
        settings.write(str(self.musictype)+ ",")
        settings.write(str(self.soundeffects) + ",")
        settings.write(str(self.graphics))
        settings.close

#Image Class
class Image(pygame.sprite.Sprite):
    def __init__(self, path, xpos, ypos):
        pygame.sprite.Sprite.__init__(self)
        #allows the class to refer to the current window surface
        self.surface = pygame.display.get_surface()
        #loads the image from the path passed in
        self.image = pygame.image.load(path)
        print((self.image.get_height() * 2))
        print((self.image.get_height() * 2))
        #stores the given co-ords
        self.givenpos = (xpos, ypos)
        #creates an array to store the position for the image
        self.position = (xpos - (self.image.get_width() // 2), ypos - (self.image.get_height() // 2))

    #procedure to display the image
    def display_Image(self):
        self.surface.blit(self.image, self.position)

    #procedure to scale the image
    def resize_Image(self, scale):
        #changes the size of the image
        self.image = pygame.transform.scale(self.image, ((self.image.get_width() * scale), (self.image.get_height() * scale)))
        #moves the image to maintain the center
        self.position = (self.givenpos[0] - (self.image.get_width() // 2), self.givenpos[1] - (self.image.get_height() // 2))

#Text Class
class Text(pygame.sprite.Sprite):
    def __init__(self, content, font_size, xpos, ypos, colour = White):
        pygame.sprite.Sprite.__init__(self)
        #Initializes the font if needed
        if  not pygame.font.get_init:
            pygame.font.init()
        #allows the class to refer to the current window surface
        self.surface = pygame.display.get_surface()
        #creates the font that will be used for the text
        self.font = pygame.font.Font('resources/font/ca.ttf', font_size)
        #creastes the text
        self.text = self.font.render(content, False, colour)
        #saves colour for use when changing the text
        self.colour = colour
        #saves given for use when changing the text
        self.givenpos = (xpos, ypos)
        #creates array to store the position for the text
        self.position = (xpos - (self.text.get_width() // 2), ypos - (self.text.get_height() // 2))
        print((self.text.get_width(), self.text.get_height()))

    #procedure to display the text
    def display_text(self):
        self.surface.blit(self.text, self.position)

    #procedure to change the content of the text object
    def change_text(self, newtext, drawmethod):
        #changes the text
        self.text = self.font.render(newtext, False, self.colour)
        #move the text so the center is the same
        self.position = (self.givenpos[0] - (self.text.get_width() // 2), self.givenpos[1] - (self.text.get_height() // 2))
        #redraws the current page
        drawmethod()
