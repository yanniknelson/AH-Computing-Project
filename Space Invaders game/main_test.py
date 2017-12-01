import pygame
import os


White = (255, 255, 255)
Black = (0, 0, 0)

pygame.font.init()
ca = pygame.font.Font('resources/font/ca.ttf', 16)

#required for pygame sprite
class Button(pygame.sprite.Sprite):
    def __init__(self, caption, xpos, ypos):
        #required for pygame sprite
        pygame.sprite.Sprite.__init__(self)
        #array holds the small size of the button
        self.size = [164, 62]
        #array hold the center position of the button
        self.position = [xpos, ypos]
        #allows the class to refer to the current window surface
        self.surface = pygame.display.get_surface()
        #creates rectangle that is the base of the button
        self.face = pygame.Rect(self.position, self.size)
        #moves the rectangle to the desired location
        self.face.center = self.position
        #creates text that is displayed on the button
        #this relies on the font being called ca
        #if not this will crash the program
        #(there is not catch all for this, bar passing it as a parameter in everything)
        #font created like this:
        #pygame.font.init()
        #ca = pygame.font.Font('resources/font/ca.ttf', 16)s
        self.text = ca.render(caption, False, Black)

    def display_Button(self):
        #draws the rectangle
        pygame.draw.rect(self.surface, White, self.face)
        #draws the text
        self.surface.blit(self.text, self.position)

pygame.init()

screen = pygame.display.set_mode((960, 720))
pygame.display.set_caption("SPACE INADERS")

done = False
clock = pygame.time.Clock()
test_button = Button("test", 224, 600)

screen.fill(Black)

test_button.display_Button()

pygame.display.flip()

clock.tick(60)

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
