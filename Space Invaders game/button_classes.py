import pygame
#import the pages to refer to them(for homepage buttons and back buttons)

pygame.init()

#variables used to quickly refer to colours
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
        self.position = [xpos - (self.text.get_width() //2), ypos - (self.text.get_height() //2)]

    #procedure to display the text
    def display_text(self):
        self.surface.blit(self.text, self.position)


#required for pygame sprite
class Button(pygame.sprite.Sprite):
    def __init__(self, caption, xpos, ypos, width = 113, height = 41s):
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
            #stand in for the fucntion that will draw the whole page
            #draw_page() //////////////////////////////////////////////////////////////////////////////
        elif not self.face.collidepoint(pygame.mouse.get_pos()) and self.large:
            self.large = False
            self.face = self.face.inflate((-20, -16))
            print(self.caption + " is small")
            #stand in for the fucntion that will draw the whole page
            #draw_page() /////////////////////////////////////////////////////////////////////////////

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
