import pygame
import os
import time


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
    def hover_Check(self):
        if self.face.collidepoint(pygame.mouse.get_pos()) and not self.large:
            self.large = True
            self.face = self.face.inflate(20, 16)
            print(self.caption + " is large")
            draw_page()
        elif not self.face.collidepoint(pygame.mouse.get_pos()) and self.large:
            self.large = False
            self.face = self.face.inflate((-20, -16))
            print(self.caption + " is small")
            draw_page()

    #procedure to display the button
    def display_Button(self):
        #draws the rectangle
        pygame.draw.rect(self.surface, White, self.face)
        #draws the text
        self.text.display_text()

#homepage_Button class
class homepage_Button(Button):
    def __init__(self, caption, xpos, ypos):
        #sets up the button
        Button.__init__(self, caption, xpos, ypos, 164, 62)

    #procedure to detect being clicked
    def click_Check(self):
        #the self.large variable is only true if the mouse is over the buttons
        #checks if self.large is true and the mouse button 1 is pressed
        if self.large and pygame.mouse.get_pressed()[0]:
            print (self.caption + " has been clicked")
            #sleeps to ensure it doesn't detect more than one click at a time
            time.sleep(.1)


pygame.init()

screen = pygame.display.set_mode((960, 720))
pygame.display.set_caption("SPACE INADERS")

done = False
clock = pygame.time.Clock()
I_button = homepage_Button("Instructions", 156, 645)
G_button = homepage_Button("New Game", 480, 645)
S_button = homepage_Button("Settings", 821, 645)
Title = Text("SPACE INVADERS", 72, 480, 106)
Sub_Title = Text("These are the aliens you'll encounter:", 32, 480, 228)
mother_ship_img = Image('resources/sprite_Images/aliens/mother_Ship.png', 250, 318)
mother_text = Text("This can be worth 50, 100, 150 or 300 points", 16, 560, 318)
thirty_img = Image('resources/sprite_Images/aliens/30pts_Open.png', 250, 368)
thirty_text = Text("This alien is worth 30 points", 16, 472, 368)
twenty_img = Image('resources/sprite_Images/aliens/20pts_Open.png', 250, 418)
twenty_text = Text("This alien is worth 20 points", 16, 472, 418)
ten_img = Image('resources/sprite_Images/aliens/10pts_Open.png', 250, 468)
ten_text = Text("This alien is worth 10 points", 16, 472, 468)



def draw_page():
    pygame.display.get_surface().fill(Black)
    print("drawn")
    Title.display_text()
    Sub_Title.display_text()
    I_button.display_Button()
    G_button.display_Button()
    S_button.display_Button()
    mother_ship_img.display_Image()
    mother_text.display_text()
    thirty_img.display_Image()
    thirty_text.display_text()
    twenty_img.display_Image()
    twenty_text.display_text()
    ten_img.display_Image()
    ten_text.display_text()
    pygame.display.flip()

draw_page()

clock.tick(60)

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        I_button.hover_Check()
        I_button.click_Check()
        G_button.hover_Check()
        S_button.hover_Check()
