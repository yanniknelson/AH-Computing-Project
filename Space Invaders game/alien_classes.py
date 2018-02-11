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

class Mother_Ship(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.position = [1000, 40]
        self.image = Image('resources/sprite_Images/aliens/mother_Ship.png', self.position[0], self.position[1])
        self.image.resize_Image(2)
        self.rect = self.image.image.get_rect()
        self.rect.center = self.position

    def move(self):
        self.position[0] -= 4
        self.image = Image('resources/sprite_Images/aliens/mother_Ship.png', self.position[0], self.position[1])
        self.image.resize_Image(2)
        self.rect = self.image.image.get_rect()
        self.rect.center = self.position

    def blow(self):
        self.kill()

    def display_ship(self):
        self.image.display_Image()


class Alien_Shot(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, left, right, mask, speed):
        pygame.sprite.Sprite.__init__(self)
        self.position = [xpos, ypos]
        self.distance_moved = 0
        self.moving = True
        self.blownUp = False
        self.left_image = left
        self.right_image = right
        self.colour_changed = False
        self.mask = mask
        self.movement_speed = speed
        self.image = Image(self.left_image, self.position[0], self.position[1])
        self.rect = self.image.image.get_rect()
        self.rect.center = self.position

    def move(self):
        if self.moving:
            self.position[1] += self.movement_speed
            self.distance_moved += self.movement_speed
            if self.distance_moved % 2 == 1:
                self.image = Image(self.right_image, self.position[0], self.position[1])
            else:
                self.image = Image(self.left_image, self.position[0], self.position[1])
                self.rect = self.image.image.get_rect()
                self.rect.center = self.position

    def change_colour(self):
        self.colour_changed = True
        index = self.right_image.find('.png')
        self.right_image = self.right_image[:index] + '_Green'+ self.right_image[index:]
        index = self.left_image.find('.png')
        self.left_image = self.left_image[:index] + '_Green'+ self.left_image[index:]
        print('colour_changed')

    def blow(self):
        self.kill()

    def blow_up(self):
        self.image = Image(self.mask, self.position[0], self.position[1])
        self.moving = False

    def display_shot(self):
        self.image.display_Image()

class Bolt(Alien_Shot):
    def __init__(self, xpos, ypos):
        Alien_Shot.__init__(self, xpos, ypos, 'resources/sprite_Images/bolt/bolt_Left.png', 'resources/sprite_Images/bolt/bolt_Right.png', 'resources/sprite_Images/bolt/bolt_Mask.png', 7)

class Arrow(Alien_Shot):
    def __init__(self, xpos, ypos):
        Alien_Shot.__init__(self, xpos, ypos, 'resources/sprite_Images/arrow/arrow.png', 'resources/sprite_Images/arrow/arrow_Second.png', 'resources/sprite_Images/arrow/arrow_Black_Mask.png', 5)
