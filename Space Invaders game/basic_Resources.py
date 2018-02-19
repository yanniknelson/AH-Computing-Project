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
        self.musictype =  True
        self.soundeffects = True

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
            self.musictype =  settings[1] == "True"
            self.soundeffects = settings[2] == "True"

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
        settings.write(str(self.soundeffects))
        settings.close

#class for each highscore holds the score
#and the initials for the highscore
class Highscore():
    def __init__(self, name, value):
        #stores the initials
        self.name = name
        #stores the score
        self.value = value

#Class for the scoreboard
class ScoreBoard():
    def __init__(self):
        #list of scores
        self.scores = []
        #score of current game
        self.current_score = 0

    #procedure to determine if the current_score is a new highscore
    def check_score(self):
        #if there are less than 10 highscores
        if len(self.scores) < 10:
            #return true
            return True
        #otherwise
        else:
            #if the current score is greater than the value of any of the current scores
            for score in self.scores:
                if self.current_score > score.value:
                    #return true
                    return True

    #procedure to get the scoreboard from the highscores file
    def get_highscores(self):
        #make sure the highscores list is empty
        self.scores.clear()
        #checks the highscores file exists
        if not os.path.isfile("highscores.txt"):
            #if the file doesn't exist create the file
            print("file not there")
            self.write_file(False, False)
        else:
            #if it does exist open the file and split the string
            #by commas into an array
            highscoresfile = open("highscores.txt", "r")
            highscores = highscoresfile.read().split(",")
            highscoresfile.close()
            print(highscores)

            #then if the array has any elements in it
            count = 0
            if len(highscores) > 0:
                #run through the array and split in into score objects and store in the
                #list of scores
                while count < len(highscores) - 1:
                    new = Highscore(str(highscores[count]), int(highscores[count + 1]))
                    self.scores.append(new)
                    count += 2
            print(len(self.scores))

    #procedure to sort the scores
    def bubble_sort_scores(self):
        #if there is more than one highscore
        if len(self.scores) > 1:
            #for every index in self.scores
            for outer in range(len(self.scores)):
                #for every index from 0 to the current value of outer - 1
                for inner in range(0, len(self.scores) - outer - 1):
                    #if the value of the highscore at the index inner is less than that at the index of inner + 1
                    if self.scores[inner].value < self.scores[inner + 1].value:
                        #switch the values of those two index
                        temp = self.scores[inner]
                        self.scores[inner] = self.scores[inner + 1]
                        self.scores[inner + 1] = temp

    def write_file(self, remove, fill):
        #if the remove parameter is true (will be the case if the file already exists)
        if remove:
            #delete the file
            os.remove("highscores.txt")
        #create the file again
        highscoresfile = open("highscores.txt", "w")
        #if the fill parameter is true (will be the case if a new highscore needs to be added)
        if fill:
            #add each score from the scores list to the file deliited by a comma
            count = 0
            if len(self.scores) > 0:
                for score in self.scores:
                    highscoresfile.write(score.name + ",")
                    #if the current element is the last in the list
                    if count == len(self.scores) - 1:
                        #add the element but don't add a comma after it
                        highscoresfile.write(str(score.value))
                    else:
                        #otherwise add the element and add the comma delimit
                        highscoresfile.write(str(score.value) + ',')
                    count += 1
        highscoresfile.close()

#Image Class
class Image(pygame.sprite.Sprite):
    def __init__(self, path, xpos, ypos):
        pygame.sprite.Sprite.__init__(self)
        #allows the class to refer to the current window surface
        self.surface = pygame.display.get_surface()
        #loads the image from the path passed in
        self.image = pygame.image.load(path)
        #stores the given co-ords
        self.givenpos = (xpos, ypos)
        #creates an array to store the position for the image
        self.position = [xpos - (self.image.get_width() // 2), ypos - (self.image.get_height() // 2)]

    #procedure to display the image
    def display_Image(self):
        self.surface.blit(self.image, self.position)

    #procedure to scale the image
    def resize_Image(self, scalefactor):
        #changes the size of the image
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * scalefactor), int(self.image.get_height() * scalefactor)))
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
        self.position = [xpos - (self.text.get_width() // 2), ypos - (self.text.get_height() // 2)]
        print((self.text.get_width(), self.text.get_height()))

    #procedure to display the text
    def display_text(self):
        self.surface.blit(self.text, self.position)

    #procedure to change the content of the text object
    def change_text(self, newtext, drawmethod):
        #changes the text
        self.text = self.font.render(newtext, False, self.colour)
        #move the text so the center is the same
        self.position = [self.givenpos[0] - (self.text.get_width() // 2), self.givenpos[1] - (self.text.get_height() // 2)]
        #redraws the current page
        drawmethod()
