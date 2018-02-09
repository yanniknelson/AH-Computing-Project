import pygame
from basic_Resources import *

pygame.init()

#Alien Class
class Alien(pygame.sprite.Sprite):
    def __init__(self, openpath, closepath, xpos, ypos):
        pygame.sprite.Sprite.__init__(self)
        #array hold the center position of the button
        self.position = [xpos, ypos]
        self.open_image = openpath
        self.close_image = closepath
        self.which_image = True
        self.dead = False
        self.image = Image(self.open_image, xpos, ypos)
        self.image.resize_Image(2)
        self.points = 0

        self.rect = self.image.image.get_rect()
        self.rect.center = self.position

    #procedure to kill the aien
    def kill_alien(self):
        self.dead = True
        self.switch_image()
        return self.points

    #prodecure to change the alien's image if appropriate
    def switch_image(self):
        if self.dead:
            self.image = Image('resources/sprite_Images/aliens/alien_Blast.png', self.position[0], self.position[1])
            self.image.resize_Image(2)
        elif self.which_image:
            self.image = Image(self.close_image, self.position[0], self.position[1])
            self.image.resize_Image(2)
            self.rect = self.image.image.get_rect()
            self.rect.center = self.position
            self.which_image = False
        else:
            self.image = Image(self.open_image, self.position[0], self.position[1])
            self.image.resize_Image(2)
            self.rect = self.image.image.get_rect()
            self.rect.center = self.position
            self.which_image = True

    #prodecure to move the current alien
    def move(self, xdist, ydist):
        #if it's not dead then move and switch image
        if not self.dead:
            self.position[0] += xdist
            self.position[1] += ydist
            self.switch_image()
        else:
            #if dead kill the sprite
            print('dead')
            self.kill()

    #procedure to display the alien
    def display_alien(self):
        self.image.display_Image()


class Alien10(Alien):
    def __init__(self, xpos, ypos):
        Alien.__init__(self, 'resources/sprite_Images/aliens/10pts_Open.png', 'resources/sprite_Images/aliens/10pts_Closed.png', xpos, ypos)
        self.points = 10

class Alien20(Alien):
    def __init__(self, xpos, ypos):
        Alien.__init__(self, 'resources/sprite_Images/aliens/20pts_Open.png', 'resources/sprite_Images/aliens/20pts_Closed.png', xpos, ypos)
        self.points = 20

class Alien30(Alien):
    def __init__(self, xpos, ypos):
        Alien.__init__(self, 'resources/sprite_Images/aliens/30pts_Open.png', 'resources/sprite_Images/aliens/30pts_Closed.png', xpos, ypos)
        self.points = 30

class Bolt(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos):
        pygame.sprite.Sprite.__init__(self)
        self.position = [xpos, ypos]
        self.distance_moved = 0
        self.moving = True
        self.blownUp = False
        self.left_image = 'resources/sprite_Images/bolt/bolt_Left.png'
        self.right_image = 'resources/sprite_Images/bolt/bolt_Right.png'
        self.image = Image(self.left_image, self.position[0], self.position[1])
        self.rect = self.image.image.get_rect()
        self.rect.center = self.position

    def move(self):
        if self.moving:
            self.position[1] += 7
            self.distance_moved += 7
            if self.distance_moved % 2 == 1:
                self.image = Image(self.right_image, self.position[0], self.position[1])
            else:
                self.image = Image(self.left_image, self.position[0], self.position[1])
                self.rect = self.image.image.get_rect()
                self.rect.center = self.position

    def blow(self):
        self.kill()

    def blow_up(self):
        self.image = Image('resources/sprite_Images/bolt/bolt_Mask.png', self.position[0], self.position[1])
        self.moving = False

    def display_shot(self):
        self.image.display_Image()
