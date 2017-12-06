import pygame
import os
import time
from basic_Resources import *

pygame.init()

White = (255, 255, 255)
Black = (0, 0, 0)

#Button Class
class Button(pygame.sprite.Sprite):
    def __init__(self, caption, xpos, ypos, width = 113, height = 41):
        pygame.sprite.Sprite.__init__(self)
        #array hold the center position of the button
        self.position = [xpos, ypos]
        #allows the class to refer to the current window surface
        self.surface = pygame.display.get_surface()
        #creates rectangle that is the base of the button
        self.face = pygame.Rect(self.position, (width, height))
        #moves the rectangle to the desired location
        self.face.center = self.position
        #stores the state of the size
        self.large = False
        #creates a text variable of the text class
        self.text = Text(caption, 16, xpos, ypos, Black)
        self.caption = caption

    #checks if the cursor is over the button and changes the size accordingly
    def hover_Check(self, drawmethod):
        if self.face.collidepoint(pygame.mouse.get_pos()) and not self.large:
            self.large = True
            self.face = self.face.inflate(20, 16)
            print(self.caption + " is large")
            drawmethod()
        elif not self.face.collidepoint(pygame.mouse.get_pos()) and self.large:
            self.large = False
            self.face = self.face.inflate((-20, -16))
            print(self.caption + " is small")
            drawmethod()

    #procedure to display the button
    def display_Button(self):
        #draws the rectangle
        pygame.draw.rect(self.surface, White, self.face)
        #draws the text
        self.text.display_text()

#Homepage_Button class
class Homepage_Button(Button):
    def __init__(self, caption, xpos, ypos, page):
        #sets up the button
        Button.__init__(self, caption, xpos, ypos, 164, 62)
        self.page = page

    #procedure to detect being clicked
    def click_Check(self):
        #the self.large variable is only true if the mouse is over the buttons
        #checks if self.large is true and the mouse button 1 is pressed
        if self.large and pygame.mouse.get_pressed()[0]:
            print (self.caption + " has been clicked")
            #if instruction button
            if self.page == "I":
                print("start instruction page")
            #if game button
            elif self.page == "G":
                print("start game page")
            #if settings button
            elif self.page == "S":
                print("start settings page")
            #sleeps to ensure it doesn't detect more than one click at a time
            time.sleep(.1)
