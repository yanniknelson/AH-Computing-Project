import pygame
import os


White = (255, 255, 255)
Black = (0, 0, 0)

#Text Class
class Text(pygame.sprite.Sprite):
    def __init__(self, content, font_size, xpos, ypos):
        pygame.sprite.Sprite.__init__(self)
        #Initializes the font if needed
        if  not pygame.font.get_init:
            pygame.font.init()
        #allows the class to refer to the current window surface
        self.surface = pygame.display.get_surface()
        #creates the font that will be used for the text
        self.font = ca = pygame.font.Font('resources/font/ca.ttf', font_size)
        #creastes the text
        self.text = self.font.render(content, False, Black)
        #creates array to store the position for the text
        self.position = [xpos - (self.text.get_width() //2), ypos - (self.text.get_height() //2)]

    #procedure to display the text
    def display_text(self):
        self.surface.blit(self.text, self.position)

#Button Class
class Button(pygame.sprite.Sprite):
    def __init__(self, caption, xpos, ypos):
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
        #stores the state of the size
        self.large = False
        #creates a text variable of the text class
        self.text = Text(caption, 16, xpos, ypos)
        self.caption = caption

    #checks if the cursor is over the button and changes the size accordingly
    def hover_Check(self):
        if self.face.collidepoint(pygame.mouse.get_pos()) and not self.large:
            self.large = True
            #size changes don't work yet
            self.face = self.face.inflate(20, 16)
            print(self.caption + " is large")
            draw_page()
        elif not self.face.collidepoint(pygame.mouse.get_pos()) and self.large:
            self.large = False
            #size changes don't work yet
            self.face = self.face.inflate((-20, -16))
            print(self.caption + " is small")
            draw_page()

    #procedure to display the button
    def display_Button(self):
        #draws the rectangle
        pygame.draw.rect(self.surface, White, self.face)
        #draws the text
        self.text.display_text()


pygame.init()

screen = pygame.display.set_mode((960, 720))
pygame.display.set_caption("SPACE INADERS")

done = False
clock = pygame.time.Clock()
I_button = Button("Instructions", 156, 645)
G_button = Button("New Game", 480, 645)
S_button = Button("Settings", 821, 645)

def draw_page():
    pygame.display.get_surface().fill(Black)
    print("drawn")
    I_button.display_Button()
    G_button.display_Button()
    S_button.display_Button()
    pygame.display.flip()

draw_page()

clock.tick(60)

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        I_button.hover_Check()
        G_button.hover_Check()
        S_button.hover_Check()
