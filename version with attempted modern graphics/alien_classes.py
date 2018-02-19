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

#Alien Class
class Alien(pygame.sprite.Sprite):
    def __init__(self, openpath, closepath, xpos, ypos):
        pygame.sprite.Sprite.__init__(self)
        global resource
        self.img_resource = resource
        #array to hold the center position of the button
        self.position = [xpos, ypos]
        #holds the path to the open image
        self.open_image = openpath
        #holds the path to the close image
        self.close_image = closepath
        #indicates the current image in use
        self.which_image = True
        #determines weather or not the alien is dead
        self.dead = False
        #the image object to be displayed
        self.image = Image(self.open_image, xpos, ypos)
        self.scaler = 1
        if resource == 'resources/sprite_Images':
            self.scaler = 2
        else:
            print('smaller')
            self.scaler = 0.08
        self.image.resize_Image(self.scaler)
        #the number of points the alien rewards
        self.points = 0

        #gets and stores the rectangle of the image
        self.rect = self.image.image.get_rect()
        self.rect.center = self.position

    #procedure to kill the aien
    def kill_alien(self):
        #set the dead variable to true
        self.dead = True
        #change the image
        self.switch_image()
        #return the number of points the alien rewards
        return self.points

    #prodecure to change the alien's image if appropriate
    def switch_image(self):
        #the the dead variable is true
        if self.dead:
            #change the image to the blast image
            self.image = Image('resources/sprite_Images/aliens/alien_Blast.png', self.position[0], self.position[1])
            self.image.resize_Image(2)
        #other wise if the which_image is true
        elif self.which_image:
            #change the image to the closed alien image
            self.image = Image(self.close_image, self.position[0], self.position[1])
            self.image.resize_Image(self.scaler)
            #make which_image false
            self.which_image = False
        else:
            #change the image to the open alien image
            self.image = Image(self.open_image, self.position[0], self.position[1])
            self.image.resize_Image(self.scaler)
            #make which_image false
            self.which_image = True

        #get and store the new rectangle of the image
        self.rect = self.image.image.get_rect()
        self.rect.center = self.position

    #prodecure to move the current alien
    def move(self, xdist, ydist):
        #if it's not dead then move and switch image
        if not self.dead:
            #change the x and y positions by the respective changes
            self.position[0] += xdist
            self.position[1] += ydist
            #call the switch_image procedure
            self.switch_image()
        #otherwise
        else:
            #remove alien sprite from all sprite groups
            print('dead')
            self.kill()

    #procedure to display the alien
    def display_alien(self):
        self.image.display_Image()

#Subclass of Alien with the 10pt alien image paths and point set to 10
class Alien10(Alien):
    def __init__(self, xpos, ypos):
        global resource
        Alien.__init__(self, resource + '/aliens/10pts_Open.png', resource + '/aliens/10pts_Closed.png', xpos, ypos)
        self.points = 10

#Subclass of Alien with the 20pt alien image paths and point set to 20
class Alien20(Alien):
    def __init__(self, xpos, ypos):
        global resource
        Alien.__init__(self, resource + '/aliens/20pts_Open.png', resource + '/aliens/20pts_Closed.png', xpos, ypos)
        self.points = 20

#Subclass of Alien with the 30pt alien image paths and point set to 30
class Alien30(Alien):
    def __init__(self, xpos, ypos):
        global resource
        Alien.__init__(self, resource + '/aliens/30pts_Open.png', resource + '/aliens/30pts_Closed.png', xpos, ypos)
        self.points = 30

#Mother Ship Class
class Mother_Ship(pygame.sprite.Sprite):
    def __init__(self):
        global resource
        self.img_resource = resource
        pygame.sprite.Sprite.__init__(self)
        #array to hold the center position of the button
        self.position = [1000, 40]
        #the image object to be displayed
        self.image = Image(self.img_resource + '/aliens/mother_Ship.png', self.position[0], self.position[1])
        self.image.resize_Image(2)
        #gets and stores the rectangle of the image
        self.rect = self.image.image.get_rect()
        self.rect.center = self.position

    #procedure to move the mother ship
    def move(self):
        #change the x position by -4
        self.position[0] -= 4
        #redefine the image with the new position
        self.image = Image(self.img_resource + '/aliens/mother_Ship.png', self.position[0], self.position[1])
        self.image.resize_Image(2)
        #get and store the new rectangle
        self.rect = self.image.image.get_rect()
        self.rect.center = self.position

    #procedure to kill the mother ship
    def blow(self):
        #remove motehr ship sprite from all sprite groups
        self.kill()

    #procedure to display mother ship
    def display_ship(self):
        #display the image of the ship
        self.image.display_Image()

#Alien Shot Class
class Alien_Shot(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, left, right, mask, speed):
        pygame.sprite.Sprite.__init__(self)
        #array to hold the center position of the button
        self.position = [xpos, ypos]
        #array to hold the distance moved from starting place
        self.distance_moved = 0
        #indicates if the shot is moving or not
        self.moving = True
        #stores the path for the left image
        self.left_image = left
        #stores the path for the right image
        self.right_image = right
        #indicates whether or not the colour has been changed
        self.colour_changed = False
        #stoers teh path for the mask image
        self.mask = mask
        #stores the movement speed
        self.movement_speed = speed
        #the image object to be displayed
        self.image = Image(self.left_image, self.position[0], self.position[1])
        #gets and stores the rectangle of the image
        self.rect = self.image.image.get_rect()
        self.rect.center = self.position

    #procedure to move the shot
    def move(self):
        #if the moving variabel is true
        if self.moving:
            #change the y position by the movement speed
            self.position[1] += self.movement_speed
            #change the distance moved by the movement speed
            self.distance_moved += self.movement_speed
            #if the distanced moved is odd (every second move)
            if self.distance_moved % 2 == 1:
                #change the image to the right_image
                self.image = Image(self.right_image, self.position[0], self.position[1])
            #otherwise
            else:
                #change the image to the left_image
                self.image = Image(self.left_image, self.position[0], self.position[1])
            #get and store the new rectangle
            self.rect = self.image.image.get_rect()
            self.rect.center = self.position

    #procedure to change the colour of the shot
    def change_colour(self):
        #set the colour_changed indicator to true
        self.colour_changed = True
        #add '_Green' to then end of the path, just before .png for both images (left and right)
        index = self.right_image.find('.png')
        self.right_image = self.right_image[:index] + '_Green'+ self.right_image[index:]
        index = self.left_image.find('.png')
        self.left_image = self.left_image[:index] + '_Green'+ self.left_image[index:]
        print('colour_changed')

    #procedure to remove the shot
    def blow(self):
        #remove the shot sprite from all groups
        self.kill()

    #procedure to blow up the shot
    def blow_up(self):
        #chagne the image to the mask image
        self.image = Image(self.mask, self.position[0], self.position[1])
        #set the moving indicator to false
        self.moving = False

    #procedure to display the shot
    def display_shot(self):
        #display the image of the shot
        self.image.display_Image()

#Subclass of Alien Shot with the bolt image paths and speed of 7
class Bolt(Alien_Shot):
    def __init__(self, xpos, ypos):
        Alien_Shot.__init__(self, xpos, ypos, 'resources/sprite_Images/bolt/bolt_Left.png', 'resources/sprite_Images/bolt/bolt_Right.png', 'resources/sprite_Images/bolt/bolt_Mask.png', 7)

#Subclass of Alien Shot with the arrow image paths and speed of 5
class Arrow(Alien_Shot):
    def __init__(self, xpos, ypos):
        Alien_Shot.__init__(self, xpos, ypos, 'resources/sprite_Images/arrow/arrow.png', 'resources/sprite_Images/arrow/arrow_Second.png', 'resources/sprite_Images/arrow/arrow_Black_Mask.png', 5)
