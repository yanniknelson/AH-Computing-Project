import pygame
import time
from basic_Resources import *
from alien_classes import *
from player_class import *

pygame.init()

Background = Image('resources/sprite_Images/Game_Background.png', 480, 360)
current_Score_Display = Text("0", 30, 55, 25)
player = Player(480)
aliens = pygame.sprite.Group()
projectiles = pygame.sprite.Group()
columns = []
highscoresvar = Highscores()
highscoresvar.get_highscores()

#populates the group with aliens
#also correctly positions the aliens
sep = 70

def setup_aliens():
    xpos = 60
    colstore = []
    for col in range(0, 11):
        aliensort = pygame.sprite.Group()
        alien101 = Alien10(xpos, 360)
        alien102 = Alien10(xpos, 290)
        alien201 = Alien20(xpos, 220)
        alien202 = Alien20(xpos, 150)
        alien30 = Alien30(xpos, 80)
        xpos += sep
        aliens.add(alien101)
        aliens.add(alien102)
        aliens.add(alien201)
        aliens.add(alien202)
        aliens.add(alien30)
        aliensort.add(alien101)
        aliensort.add(alien102)
        aliensort.add(alien201)
        aliensort.add(alien202)
        aliensort.add(alien30)

        colstore.append(aliensort)
    columns = colstore


def draw_page():
    Background.display_Image()
    for shot in projectiles:
        shot.display_shot()
    player.display_player()
    current_Score_Display.display_text()
    #runs through the aliens group and displays all of the aliens
    for alien in aliens:
        alien.display_alien()
    pygame.display.flip()

#runs through the aliens group and moves all the aliens in the correct direction
def move_aliens(xdist, ydist):
    for alien in aliens:
        alien.move(xdist, ydist)
    #print(aliens.sprites())

#runs through the aliens group for if an alien is getting close the the edge
#and if an alien is it switches the movement direction
def check_change(moved_down):
    for alien in aliens:
        if alien.position[0] > 900 or alien.position[0] < 60:
            if moved_down == 0:
                moved_down = 1
    return moved_down

def run_page():
    #makes the cursor invisible
    pygame.mouse.set_visible(False)
    #variables to find the elapsed time
    alien_Timer_Start = time.time()
    alien_Timer_Elapsed = time.time() - alien_Timer_Start
    #flag variable for moving down
    move_down = 0
    #stores the movement speed
    xmovespeed = 10
    movingspeed = xmovespeed
    ymovespeed = 0
    #stores the time increment between alien jumps
    starting_speed = 0.5
    gamespeed = starting_speed
    minspeed = 0.1
    #flag variable for if the player can
    can_shoot = True
    setup_aliens()
    while True:
        #resets the aliens once they've all been killed
        #with the starting and minimum speed slightly faster
        if len(aliens) == 0:
            draw_page()
            time.sleep(3)
            xmovespeed = 10
            movingspeed = xmovespeed
            ymovespeed = 0
            starting_speed -= 0.02
            gamespeed = starting_speed
            minspeed -= 0.02
            setup_aliens()
            print("all dead")
        #draws the page
        draw_page()
        #if the elapsed time is greater than or equal to the gamespeed
        #move the aliens
        if alien_Timer_Elapsed >= gamespeed:
            #checks if the aliens should change direction
            move_down = check_change(move_down)
            #if it needs to change direction it will move down
            if move_down == 1:
                ymovespeed = 10
                movingspeed = 0
                move_down = 2
                #then change direction
            elif move_down == 2:
                ymovespeed = 0
                #will decrease the speed only if its ahigher than 0.1s
                if gamespeed > minspeed:
                    gamespeed -= 0.02
                movingspeed = -xmovespeed
                xmovespeed = movingspeed
                move_down = 0
            #move the aliens
            move_aliens(movingspeed, ymovespeed)
            #once the aliens have been moved restart the timer
            alien_Timer_Start = time.time()


        #checks for key presses and moves the player in the appropriate check_direction
        #but only betweeen a specific range
        if (pygame.key.get_pressed()[pygame.K_a] == 1 or pygame.key.get_pressed()[pygame.K_LEFT] == 1) and player.position[0] > 40:
            player.move(-2)
        elif (pygame.key.get_pressed()[pygame.K_d] == 1  or pygame.key.get_pressed()[pygame.K_RIGHT] == 1) and player.position[0] < 920:
            player.move(2)

        #when the space bar is pressed
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            #so long as there is no shot currently moving in the game
            if len(projectiles) == 0:
                can_shoot = True
            for shot in projectiles:
                if shot.moving:
                    can_shoot = False
                else:
                    can_shoot = True
            #create a shot at the players position if there is no currently
            #moving shot
            if can_shoot:
                newshot = Shot(player.position[0])
                projectiles.add(newshot)
                print(len(projectiles))

        if pygame.mouse.get_pressed()[0]:
            print(pygame.mouse.get_pos())
            print(pygame.display.get_surface().get_at(pygame.mouse.get_pos()))
            time.sleep(0.1)

        for shot in projectiles:
            if shot.moving:
                if shot.position[1] - 8 > 0:
                    #if the show is above the bottom of the bunkers and touches green, it should blow up
                    if shot.position[1] - 8 < 590:
                        if (pygame.display.get_surface().get_at(((shot.position[0] - 8), shot.position[1] - 2))[1] == 225 or
                            pygame.display.get_surface().get_at(((shot.position[0] - 8), shot.position[1] + 2)))[1] == 255:
                            shot.blowup()

                    #checks if the shot is touching an alien
                    for alien in aliens:
                        if shot.rect.colliderect(alien.rect):
                            #if touching kill the alien and remove the shot
                            print('hit')
                            highscoresvar.current_score += alien.kill_alien()
                            current_Score_Display.change_text(str(highscoresvar.current_score ), draw_page)
                            shot.blow()
                            print(highscoresvar.current_score )

                    shot.move()
                else:
                    shot.blow()

        #exits if the x button or escape button is pressed
        if pygame.key.get_pressed()[pygame.K_ESCAPE] == 1:
            player.kill_player(draw_page)
            #highscoresvar.write_file(True, True)
            #pygame.display.quit()
            #pygame.quit()
            #sys.exit()

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()
        #update the elpased time
        alien_Timer_Elapsed = time.time() - alien_Timer_Start
