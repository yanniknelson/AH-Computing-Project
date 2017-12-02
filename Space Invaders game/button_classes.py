import pygame
pygame.init()

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
        self.text = Text(caption, 16, xpos, ypos)

        #checks if the cursor is over the button and changes the size accordingly
        def hover_Check(self):
            if self.face.collidepoint(pygame.mouse.get_pos()) and not self.large:
                self.large = True
                #size changes don't work yet
                self.face = self.face.inflate(20, 16)
                print(self.caption + " is large")
                #stand in for the fucntion that will draw the whole page
                #draw_page()
            elif not self.face.collidepoint(pygame.mouse.get_pos()) and self.large:
                self.large = False
                #size changes don't work yet
                self.face = self.face.inflate((-20, -16))
                print(self.caption + " is small")
                #stand in for the fucntion that will draw the whole page
                #draw_page()

    def display_Button(self):
        #draws the rectangle
        pygame.draw.rect(self.surface, White, self.face)
        #draws the text
        self.text.display_text()
