import pygame
import time
from random import *
from basic_Resources import *
from alien_classes import *
from player_class import *

pygame.init()

Background = Image('resources/sprite_Images/Game_Background.png', 480, 360)
current_Score_Display = Text("0", 30, 55, 25)
player = Player(480)
aliens = pygame.sprite.Group()
game_settings = Settings()
projectiles = pygame.sprite.Group()
alien_shots = pygame.sprite.Group()
columns = []
highscoresvar = Highscores()
highscoresvar.get_highscores()
lives_display = Text(str(player.lives), 30, 55, 700)
lives_image_display = pygame.sprite.Group()
lives_image_display.add(Image('resources/sprite_Images/ship/ship.png', 125, 700))
lives_image_display.add(Image('resources/sprite_Images/ship/ship.png', 85, 700))
mother_ship = pygame.sprite.Group()

#alien sounds
alien_move_sound = pygame.mixer.Sound('resources/audio/sound_effects/aliens_move.wav')
alien_die_sound = pygame.mixer.Sound('resources/audio/sound_effects/alien_death.wav')
alien_bolt_sound = pygame.mixer.Sound('resources/audio/sound_effects/alien_bolt.wav')
alien_arrow_sound = pygame.mixer.Sound('resources/audio/sound_effects/alien_arrow.wav')
mother_ship_sound = pygame.mixer.Sound('resources/audio/sound_effects/mother_ship_move.wav')
mother_ship_sound.set_volume(.3)

#player sound
player_shoot_sound = pygame.mixer.Sound('resources/audio/sound_effects/player_shoot.wav')
player_die_sound = pygame.mixer.Sound('resources/audio/sound_effects/player_death.wav')


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

        columns.append(aliensort)
    #columns = colstore


def draw_page():
    Background.display_Image()
    for shot in projectiles:
        shot.display_shot()

    for alshot in alien_shots:
        alshot.display_shot()

    player.display_player()
    current_Score_Display.display_text()
    #runs through the aliens group and displays all of the aliens
    for life in lives_image_display:
        life.display_Image()

    for alien in aliens:
        alien.display_alien()

    if len(mother_ship) > 0:
        for mother in mother_ship:
            mother.display_ship()

    lives_display.display_text()
    pygame.display.flip()

#runs through the aliens group and moves all the aliens in the correct direction
def move_aliens(xdist, ydist):
    for alien in aliens:
        alien.move(xdist, ydist)
    print(game_settings.soundeffects)
    if game_settings.soundeffects:
        alien_move_sound.play()
    #print(aliens.sprites())

#runs through the aliens group for if an alien is getting close the the edge
#and if an alien is it switches the movement direction
def check_change(moved_down):
    for alien in aliens:
        if alien.position[0] > 900 or alien.position[0] < 60:
            if moved_down == 0:
                moved_down = 1
    return moved_down

def end_game():
    time.sleep(0.3)
    print('Game Over')

def run_page():
    #makes the cursor invisible
    #pygame.mouse.set_visible(False)
    #variables to find the elapsed time
    game_settings.get_settings()
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

    max_wait_time = 3
    should_shoot = uniform(0.3, max_wait_time)
    alien_Shoot_Timer = time.time()
    alien_Shoot_Timer_Elapsed = time.time() - alien_Shoot_Timer

    mother_Ship_Time = uniform(5, 25)
    mother_Ship_Timer = time.time()
    mother_Ship_Timer_Elapsed = time.time() - mother_Ship_Timer

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
                #will decrease the speed only if it's higher than 0.1s
                if gamespeed > minspeed:
                    gamespeed -= 0.02
                movingspeed = -xmovespeed
                xmovespeed = movingspeed
                max_wait_time -= 0.2
                move_down = 0
            #move the aliens
            move_aliens(movingspeed, ymovespeed)
            #once the aliens have been moved restart the timer
            alien_Timer_Start = time.time()

        #runs through the aliens at the bottom of the columns

        if alien_Shoot_Timer_Elapsed >= should_shoot:
            column = randint(0,10)
            if len(columns[column]) > 0:
                for alien in columns[column]:
                    print(alien)
                    wich_shot = randint(0,3)
                    if wich_shot == 3:
                        new_alien_shot = Bolt(alien.position[0], alien.position[1])
                        if game_settings.soundeffects:
                            alien_bolt_sound.play()
                    else:
                        new_alien_shot = Arrow(alien.position[0], alien.position[1])
                        if game_settings.soundeffects:
                            alien_arrow_sound.play()
                    alien_shots.add(new_alien_shot)
                    print(alien_shots)
                    should_shoot = uniform(0.5, max_wait_time)
                    alien_Shoot_Timer = time.time()
                    break

        for column in columns:
            for alien in column:
                if alien.position[1] > 515:
                    end_game()

        for alshot in alien_shots:
            if alshot.moving:
                alshot.move()
                #print(pygame.display.get_surface().get_at((alshot.position[0], alshot.position[1])) )
                #print(pygame.display.get_surface().get_at(alshot.position[0], alshot.position[1]))
                if alshot.position[1] + 8 > 523:
                    if not alshot.colour_changed:
                        alshot.change_colour()
                    if alshot.position[1] + 8 < 590:
                        if (pygame.display.get_surface().get_at((alshot.position[0] + 8, alshot.position[1] + 8))[1] == 255):
                            alshot.blow_up()
                            print(pygame.display.get_surface().get_at((alshot.position[0], alshot.position[1])))
                    elif alshot.position[1] >= 675:
                        alshot.kill()
                    else:
                        if alshot.rect.colliderect(player.rect):
                            print('player die')
                            alshot.blow()
                            if game_settings.soundeffects:
                                player_die_sound.play()
                            player.kill_player(draw_page)
                            lives_display.change_text(str(player.lives), draw_page)
                            for img in lives_image_display:
                                img.kill()
                                break
                            #remove one from lives_image_display

                for shot in projectiles:
                    if alshot.rect.colliderect(shot.rect):
                        if shot.moving:
                            shot.kill()
                            alshot.kill()

        if len(mother_ship) > 0:
            for mother in mother_ship:
                mother.move()
                if game_settings.soundeffects:
                    mother_ship_sound.play()
                if mother.position[0] < -20:
                    mother.kill()

        if mother_Ship_Timer_Elapsed >= mother_Ship_Time:
            new_mother = Mother_Ship()
            mother_ship.add(new_mother)
            mother_Ship_Time = uniform(10, 25)
            mother_Ship_Timer = time.time()


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
                if game_settings.soundeffects:
                    player_shoot_sound.play()
                print(len(projectiles))

        for shot in projectiles:
            if shot.moving:
                if shot.position[1] - 8 > 0:
                    #if the show is above the bottom of the bunkers and touches green, it should blow up
                    if shot.position[1] - 8 < 590:
                        if (pygame.display.get_surface().get_at(((shot.position[0] - 8), shot.position[1] - 2))[1] == 225 or
                            pygame.display.get_surface().get_at(((shot.position[0] - 8), shot.position[1] + 2)))[1] == 255:
                            shot.blowup()

                    #checks if the shot is touching an alien

                    for mother in mother_ship:
                        if shot.rect.colliderect(mother.rect):
                            points_added = randint(0,3)
                            if points_added == 0:
                                points_added = 50
                            elif points_added == 1:
                                points_added = 100
                            elif points_added == 2:
                                points_added = 150
                            else:
                                points_added = 300
                            highscoresvar.current_score += points_added
                            current_Score_Display.change_text(str(highscoresvar.current_score), draw_page)
                            mother.blow()
                            shot.blow()

                    for alien in aliens:
                        if shot.rect.colliderect(alien.rect):
                            #if touching kill the alien and remove the shot
                            print('hit')
                            if game_settings.soundeffects:
                                alien_die_sound.play()
                            highscoresvar.current_score += alien.kill_alien()
                            current_Score_Display.change_text(str(highscoresvar.current_score), draw_page)
                            shot.blow()
                            print(highscoresvar.current_score)

                    shot.move()
                else:
                    shot.blow()

        if player.dead:
            end_game()

        #exits if the x button or escape button is pressed
        if pygame.key.get_pressed()[pygame.K_ESCAPE] == 1:
            #highscoresvar.write_file(True, True)
            pygame.display.quit()
            pygame.quit()
            sys.exit()

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()
        #update the elpased time
        alien_Timer_Elapsed = time.time() - alien_Timer_Start
        alien_Shoot_Timer_Elapsed = time.time() - alien_Shoot_Timer
        mother_Ship_Timer_Elapsed = time.time() - mother_Ship_Timer
