import pygame
from basic_Resources import *

pygame.init()

#Alien Class
class Player(pygame.sprite.Sprite):
    def __init__(self, xpos):
        pygame.sprite.Sprite.__init__(self)
        self.position = [xpos, 633]
        self.dead = False
        self.lives = 3
        self.image = Image('resources/sprite_Images/ship/ship.png', xpos, 633)
        self.image.resize_Image(2)

    def kill_player(self, drawmethod):
        self.lives -= 1
        for count in range(0, 5):
            self.image = Image('resources/sprite_Images/ship/ship_explode_one.png', self.position[0], self.position[1] - 4)
            #print(self.image.image.get_height())
            self.display_player()
            drawmethod()
            time.sleep(0.05)
            self.image = Image('resources/sprite_Images/ship/ship_explode_two.png', self.position[0], self.position[1] + 3)
            self.image.resize_Image(2)
            self.display_player()
            drawmethod()
            time.sleep(0.05)
        time.sleep(0.3)
        self.position = [480, 633]
        self.image = Image('resources/sprite_Images/ship/ship.png', self.position[0], self.position[1])
        self.image.resize_Image(2)
        self.display_player()
        drawmethod()
        time.sleep(0.5)

    def move(self, xdist):
        if not self.dead:
            self.position[0] += xdist
            self.image = Image('resources/sprite_Images/ship/ship.png', self.position[0], self.position[1])
            self.image.resize_Image(2)
            print(self.image.image.get_height())


    def display_player(self):
        self.image.display_Image()
        if self.lives == 0:
            self.dead = TRUE


class Shot(pygame.sprite.Sprite):
    def __init__(self, xpos):
        pygame.sprite.Sprite.__init__(self)
        self.position = [xpos, 633]
        self.image = Image('resources/sprite_Images/shot/player_Shot_Green.png', self.position[0], self.position[1])
        self.image.resize_Image(2)
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
                self.image = Image('resources/sprite_Images/shot/player_Shot_Green.png', self.position[0], self.position[1])
            else:
                self.image = Image('resources/sprite_Images/shot/player_Shot.png', self.position[0], self.position[1])
            self.image.resize_Image(2)
            self.rect = self.image.image.get_rect()
            self.rect.center = self.position

    def blowup(self):
        self.image = Image('resources/sprite_Images/shot/player_Shot_Black_Mask.png', self.position[0], self.position[1])
        self.moving = False

    def display_shot(self):
        self.image.display_Image()
