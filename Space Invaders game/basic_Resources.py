import pygame
import os
import time


pygame.init()

White = (255, 255, 255)
Black = (0, 0, 0)

#Image Class
class Image(pygame.sprite.Sprite):
    def __init__(self, path, xpos, ypos):
        pygame.sprite.Sprite.__init__(self)
        #allows the class to refer to the current window surface
        self.surface = pygame.display.get_surface()
        #loads the image from the path passed in
        self.image = pygame.image.load(path)
        #resizes the image approreately
        print((self.image.get_height() * 2))
        print((self.image.get_height() * 2))
        self.image = pygame.transform.scale(self.image, ((self.image.get_width() * 2), (self.image.get_height() * 2)))
        #creates an array to store the position for the image
        self.position = (xpos - (self.image.get_width() // 2), ypos - (self.image.get_height() // 2))

    #procedure to display the image
    def display_Image(self):
        self.surface.blit(self.image, self.position)

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
        #creates array to store the position for the text
        self.position = (xpos - (self.text.get_width() // 2), ypos - (self.text.get_height() // 2))
        print((self.text.get_width(), self.text.get_height()))

    #procedure to display the text
    def display_text(self):
        self.surface.blit(self.text, self.position)
