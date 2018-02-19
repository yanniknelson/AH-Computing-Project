import pygame
from basic_Resources import *

pygame.init()
settings = Settings()
settings.get_settings()
resource = ""
if settings.graphics:
    resource = 'resources/modern_sprite_Images'
else:
    resource = 'resources/sprite_Images'

#Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self, xpos):
        pygame.sprite.Sprite.__init__(self)
        global resource
        self.img_resource = resource
        #array to hold the position of the player
        self.position = [xpos, 633]
        #indicates if the player is dead or not
        self.dead = False
        #holds the number of lives the player has left
        self.lives = 3
        #image obejct
        self.image = Image(self.img_resource + '/ship/ship.png', xpos, 633)
        self.scaler = 1
        if resource == 'resources/sprite_Images':
            self.scaler = 2
        else:
            print('smaller')
            self.scaler = 2

        self.image.resize_Image(self.scaler)
        #gets and stores the rectangel of the image
        self.rect = self.image.image.get_rect()
        self.rect.center = self.position

    #procedure to kill the player
    def kill_player(self, drawmethod):
        #decrease the number of lives the player has by one
        self.lives -= 1
        #do five times
        for count in range(0, 5):
            #change the image to ship_explode_one
            self.image = Image(self.img_resource + '/ship/ship_explode_one.png', self.position[0], self.position[1] - 4)
            #draw the display
            drawmethod()
            #wait 0.05 seconds
            time.sleep(0.05)
            #change the image to ship_explode_two
            self.image = Image(self.img_resource + '/ship/ship_explode_two.png', self.position[0], self.position[1] + 3)
            self.image.resize_Image(self.scaler)
            #draw the display
            drawmethod()
            #wait 0.05 seconds
            time.sleep(0.05)
        #wait 0.3 seconds
        time.sleep(0.3)
        #set the position to  480, 633
        self.position = [480, 633]
        #change the image back to normal
        self.image = Image(self.img_resource + '/ship/ship.png', self.position[0], self.position[1])
        self.image.resize_Image(self.scaler)
        #draw the display
        drawmethod()
        #wait 0.5 seconds
        time.sleep(0.5)

    #procedure to move the player
    def move(self, xdist):
        if not self.dead:
            #chang the x position by xdist
            self.position[0] += xdist
            #change the image to an image in the new position
            self.image = Image(self.img_resource + '/ship/ship.png', self.position[0], self.position[1])
            self.image.resize_Image(self.scaler)
            #get and store the new rectangle
            self.rect = self.image.image.get_rect()
            self.rect.center = self.position


    #procedure to display the player
    def display_player(self):
        #display the image
        self.image.display_Image()
        #if the player has 0 lives left
        if self.lives == 0:
            #set the dead indicator to true
            self.dead = True

#Shot Class
class Shot(pygame.sprite.Sprite):
    def __init__(self, xpos):
        pygame.sprite.Sprite.__init__(self)
        global resource
        self.img_resource = resource
        #array to hold the position of the shot
        self.position = [xpos, 633]
        self.image = Image(self.img_resource + '/shot/player_Shot_Green.png', self.position[0], self.position[1])
        self.scaler = 1
        if resource == 'resources/sprite_Images':
            self.scaler = 2
        else:
            print('smaller')
            self.scaler = 2
        self.image.resize_Image(self.scaler)
        self.moving = True
        self.rect = self.image.image.get_rect()
        self.rect.center = self.position

    def blow(self):
        self.moving = False
        self.kill()

    def move(self):
        if self.moving:
            self.position[1] -= 10
            if self.position[1] > 525:
                self.image = Image(self.img_resource + '/shot/player_Shot_Green.png', self.position[0], self.position[1])
            else:
                self.image = Image(self.img_resource + '/shot/player_Shot.png', self.position[0], self.position[1])
            self.image.resize_Image(self.scaler)
            self.rect = self.image.image.get_rect()
            self.rect.center = self.position

    def blowup(self):
        self.image = Image(self.img_resource + '/shot/player_Shot_Black_Mask.png', self.position[0], self.position[1])
        self.moving = False

    def display_shot(self):
        self.image.display_Image()
