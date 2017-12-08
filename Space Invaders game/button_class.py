import pygame
import os
import time
from basic_Resources import *
import home_Page as hp

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

    #procedure to detect the mouse hovering over the button
    def hover_Check(self, drawmethod, clickmethod):
        #if the mouse is over the button
        if self.face.collidepoint(pygame.mouse.get_pos()):
            #and the button is not large
            if not self.large:
                #make the button larger
                self.large = True
                self.face = self.face.inflate(20, 16)
                print(self.caption + " is large")
                drawmethod()
            #if already large
            else:
                #run the click check
                self.click_Check(clickmethod)
        #if the mouse is not over the button and the button is large
        elif not self.face.collidepoint(pygame.mouse.get_pos()) and self.large:
            #make the button small
            self.large = False
            self.face = self.face.inflate((-20, -16))
            print(self.caption + " is small")
            drawmethod()

    #procedure to detect being clicked
    def click_Check(self, clickmethod):
        #checks if mouse button 1 is pressed
        if pygame.mouse.get_pressed()[0]:
            #runs the passed in method
            clickmethod()
            #sleeps to ensure it doesn't detect more than one click at a time
            time.sleep(.1)

    #procedure to display the button
    def display_Button(self):
        #draws the rectangle
        pygame.draw.rect(self.surface, White, self.face)
        #draws the text
        self.text.display_text()

class Back_Button(Button):
    def __init__(self, xpos, ypos):
        Button.__init__(self, "Back", xpos, ypos)

    def hover_Check(self, drawmethod):
        #if the mouse is over the button
        if self.face.collidepoint(pygame.mouse.get_pos()):
            #and the button is not large
            if not self.large:
                #make the button larger
                self.large = True
                self.face = self.face.inflate(20, 16)
                print(self.caption + " is large")
                drawmethod()
            #if already large
            else:
                #run the click check
                return self.click_Check()
        #if the mouse is not over the button and the button is large
        elif not self.face.collidepoint(pygame.mouse.get_pos()) and self.large:
            #make the button small
            self.large = False
            self.face = self.face.inflate((-20, -16))
            print(self.caption + " is small")
            drawmethod()

    #procedure to detect being clicked
    def click_Check(self):
        #checks if mouse button 1 is pressed
        if pygame.mouse.get_pressed()[0] == 1:
            #runs the passed in method
            print("back clicked")
            time.sleep(.1)
            hp.draw_page()
            hp.run_page()
            return True
