import pygame
import time
from random import *
from basic_Resources import *
from alien_classes import *
from player_class import *
import home_Page as hp
import highscore_input_Page as hip
import highscore_display_Page as hdp

pygame.init()

#image object for the background image (with the green bunkers)
Background = Image('resources/sprite_Images/Game_Background.png', 480, 360)
#text object that displays the current score
current_Score_Display = Text("0", 30, 55, 25)
#text object that displays the highest score
highest_Score_Display = Text("", 30, 905 ,25)
#player object
player = Player(480)
#group that holds the aliens
aliens = pygame.sprite.Group()
#array that will hold groups that hold the columns of the aliens
columns = []
#settings object
game_settings = Settings()
#group that holds the players shots
projectiles = pygame.sprite.Group()
#group that holds the aliens shots
alien_shots = pygame.sprite.Group()
#scoreboard object
highscoresvar = ScoreBoard()
#text object that displays the number of lives the player has left
lives_display = Text(str(player.lives), 30, 55, 700)
#group that holds the player images that represent the lives left
lives_image_display = pygame.sprite.Group()
#group that holds the mother ships
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
def setup_aliens():
    #xposition of the first column
    xpos = 60
    #make sure the columns array is empty
    columns.clear()
    #do 11 times
    for col in range(0, 11):
        #group to temporarily hold the column being created
        aliensort = pygame.sprite.Group()
        #alien objects in the column with appropriate y positions
        alien101 = Alien10(xpos, 360)
        alien102 = Alien10(xpos, 290)
        alien201 = Alien20(xpos, 220)
        alien202 = Alien20(xpos, 150)
        alien30 = Alien30(xpos, 80)
        #increase the xposition by 70 for the next column
        xpos += 70
        #add the aliens to the group of aliens
        aliens.add(alien101)
        aliens.add(alien102)
        aliens.add(alien201)
        aliens.add(alien202)
        aliens.add(alien30)
        #add the aliens to the temp group that holds the column
        aliensort.add(alien101)
        aliensort.add(alien102)
        aliensort.add(alien201)
        aliensort.add(alien202)
        aliensort.add(alien30)

        #add the column to the array of columns
        columns.append(aliensort)


def draw_page():
    #display the background
    Background.display_Image()

    #run through the alien shots group and display each object
    for alshot in alien_shots:
        alshot.display_shot()

    #run through the player shots group and display each object
    for shot in projectiles:
        shot.display_shot()

    #display the player object
    player.display_player()
    #display the current and highscore text objects and the number of lives left
    current_Score_Display.display_text()
    highest_Score_Display.display_text()
    lives_display.display_text()

    #run through the lives group and display each object
    for life in lives_image_display:
        life.display_Image()

    #run through the aliens group and display each object
    for alien in aliens:
        alien.display_alien()

    #if there is a mother ship in the mothership group
    if len(mother_ship) > 0:
        #run through the mothership group and display each object
        for mother in mother_ship:
            mother.display_ship()

    #update the display
    pygame.display.flip()


def move_aliens(xdist, ydist):
    #run through the alien group and move each one
    for alien in aliens:
        alien.move(xdist, ydist)
    print(game_settings.soundeffects)
    #if the sound effects setting is on play the move sound effect
    if game_settings.soundeffects:
        alien_move_sound.play()
    #print(aliens.sprites())

#checks if the aliens should moved down
def check_change(moved_down):
    #run through the alien display
    for alien in aliens:
        #if any alien is near the edge of the screen
        if alien.position[0] > 900 or alien.position[0] < 60:
            #if the aliens haven't moved down
            if moved_down == 0:
                #change the moved down idicator
                moved_down = 1
    #return the moved down indicator
    return moved_down

def end_game():
    global highscoresvar
    #make the mouse visible
    pygame.mouse.set_visible(True)
    #stop the background music
    pygame.mixer.music.stop()
    print(highscoresvar.current_score)
    #if a new highscore has been achieved
    if highscoresvar.check_score():
        #switch to the highscore input page
        hip.run_page(highscoresvar)
    #otherwise
    else:
        #switch to the highscore display page
        hdp.run_page()
    print('Game Over')

def run_page():
    global highscoresvar
    #makes the cursor invisible
    pygame.mouse.set_visible(False)
    #variables to find the elapsed time
    columns.clear()
    alien_shots.empty()
    projectiles.empty()
    aliens.empty()
    #get the current highscores
    highscoresvar.get_highscores()

    #ensure the current score is 0 when the game starts
    highscoresvar.current_score = 0
    #ensure the player has 3 lives when the game starts
    player.lives = 3
    #ensure the dead indicator is false when the game starts
    player.dead = False
    #ensures the player starts in the middle of the page
    player.position[0] = 480
    player.move(0)
    #ensure all of the text is displaying the correct values
    lives_display.change_text(str(player.lives), draw_page)
    current_Score_Display.change_text(str(highscoresvar.current_score), draw_page)
    highest_Score_Display.change_text(str(highscoresvar.scores[0].value), draw_page)

    #ensures the lives_display has only two images when the game starts
    lives_image_display.empty()
    lives_image_display.add(Image('resources/sprite_Images/ship/ship.png', 125, 700))
    lives_image_display.add(Image('resources/sprite_Images/ship/ship.png', 85, 700))

    #gets the most recent settings
    game_settings.get_settings()
    #if the musictype setting is true
    if game_settings.musictype:
        #get the scifi music
        pygame.mixer.music.load('resources/audio/background_music/scifi.mp3')
    #otherwise
    else:
        #get the popdance music
        pygame.mixer.music.load('resources/audio/background_music/popdance.mp3')
    #if the musicstate setting is true
    if game_settings.musicstate:
        #play the music on a loop
        pygame.mixer.music.play(-1)

    #timer to tell if the aliens shoul move
    #start time
    alien_Timer_Start = time.time()
    #time elapsed
    alien_Timer_Elapsed = time.time() - alien_Timer_Start
    #flag variable for moving down
    move_down = 0
    #stores the movement speed
    xmovespeed = 10
    movingspeed = xmovespeed
    ymovespeed = 0
    #stores the starting time increment between alien jumps
    starting_speed = 0.5
    #stores the teim increment currently being used
    gamespeed = starting_speed
    #the smallest allowable time increment
    minspeed = 0.1
    #flag variable for if the player can
    can_shoot = True
    #create the groups of aliens
    setup_aliens()

    #stores the maximum time between alien shots
    max_wait_time = 3
    #stores the minimum time between alien shots
    min_wait_time = 0.3
    #stores the current time between alien alien_shots
    #chooses a random number between the minimum and maximum time
    should_shoot = uniform(min_wait_time, max_wait_time)
    #timer for the alien shots
    #starts timer
    alien_Shoot_Timer = time.time()
    #time elapsed
    alien_Shoot_Timer_Elapsed = time.time() - alien_Shoot_Timer

    #stores the current time between the appearances of the mother ship
    #chooses a random number between 5 and 25
    mother_Ship_Time = uniform(5, 25)
    #timer for mother ship appearences
    #starts timer
    mother_Ship_Timer = time.time()
    #time elapsed
    mother_Ship_Timer_Elapsed = time.time() - mother_Ship_Timer

    #loop to run the game
    while True:
        #draws the page
        draw_page()
        #if there are no aliens left
        if len(aliens) == 0:
            #wait 3 seconds
            time.sleep(3)
            #set xmovespeed store to 10 to ensure the aliens move to the right
            xmovespeed = 10
            #set the movement speed to the xmovement speed store
            movingspeed = xmovespeed
            #set the y movement speed to 0
            ymovespeed = 0
            #increase the starting speed (deacrease the time interval)
            starting_speed -= 0.02
            #set the current time interval (alien movement) to the starting speed
            gamespeed = starting_speed
            #increase the maximum speed (minimum time interval)
            minspeed -= 0.02
            #re-setup the aliens
            setup_aliens()

            #reset the max and min time intervals for the mother ships' appearances
            max_wait_time = 3
            min_wait_time = 0.3
            #pick a new random time
            should_shoot = uniform(min_wait_time, max_wait_time)
            #reset the timer for the alien shots
            alien_Shoot_Timer = time.time()
            alien_Shoot_Timer_Elapsed = time.time() - alien_Shoot_Timer

            print("all dead")
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
                #will increase the speed only if it's higher than 0.1s
                if gamespeed > minspeed:
                    gamespeed -= 0.02
                movingspeed = -xmovespeed
                xmovespeed = movingspeed
                #if the differnece between the max and minimumn time intervals for the
                #aliens movement is greater than 0.2 seconds
                if max_wait_time - min_wait_time > 0.2:
                    #deacrease the maximum time interval by 0.2
                    #and increse the minimum time interval by 0.2
                    max_wait_time -= 0.2
                    min_wait_time += 0.2
                #set the move down indicator to 0
                move_down = 0
            #move the aliens
            move_aliens(movingspeed, ymovespeed)
            #once the aliens have been moved restart the timer
            alien_Timer_Start = time.time()

        #if the elasped time is greater than or equal to the current aliens
        #shoot time interval
        if alien_Shoot_Timer_Elapsed >= should_shoot:
            print("shoot")
            #pick a random column of aliens
            column = randint(0,10)
            print(len(columns[column]))
            #if that column is not empty
            #(if it is this will be done again next loop until a non empty column is found)
            if len(columns[column]) > 0:
                #run through the aliens in the column
                #(will only use the bottom alien using the break to stop the loop after one go round)
                for alien in columns[column]:
                    print(alien)
                    #pick a random number between 0 and 3
                    wich_shot = randint(0,3)
                    #if the number is 3
                    if wich_shot == 3:
                        #create a bolt in the position of the lowest alien in the selected column
                        new_alien_shot = Bolt(alien.position[0], alien.position[1])
                        #if the sound effects setting is true play the bolt sound
                        if game_settings.soundeffects:
                            alien_bolt_sound.play()
                    #otherwise
                    else:
                        #create an arrow in the position of the lowest alien in the selected column
                        new_alien_shot = Arrow(alien.position[0], alien.position[1])
                        #if the sound effects setting is true play the arrow sound
                        if game_settings.soundeffects:
                            alien_arrow_sound.play()
                    #add the new alien shot to the group of alien shots
                    alien_shots.add(new_alien_shot)
                    print(alien_shots)
                    #reset the timer
                    should_shoot = uniform(min_wait_time, max_wait_time)
                    alien_Shoot_Timer = time.time()
                    #break the loop to ensure this is only donw for the lowest alien in the column
                    break

        #run through all the columns of aliens
        for column in columns:
            #run through the aliens in the column
            for alien in column:
            #if the lowest alien has reached the bunkers
                if alien.position[1] > 490:
                    #call the end game method
                    end_game()
                break

        #for every shot in the alien shot group
        for alshot in alien_shots:
            #if the moving indicator of the shot is true
            if alshot.moving:
                #call the shot's move method
                alshot.move()
                #if the shot is bellow the top of the bunkers
                if alshot.position[1] + 8 > 523:
                    #and the colour has not changed to green yet
                    if not alshot.colour_changed:
                        #change the colour of the shot
                        alshot.change_colour()
                    #if the shot is also above the bottom of the bunkers
                    if alshot.position[1] + 8 < 590:
                        #and the shot is touching a green pixel
                        if (pygame.display.get_surface().get_at((alshot.position[0] + 8, alshot.position[1] + 8))[1] == 255):
                            #blow up the shot
                            alshot.blow_up()
                            print(pygame.display.get_surface().get_at((alshot.position[0], alshot.position[1])))
                    #otherwise if the shot it at the bottom of the play area
                    elif alshot.position[1] >= 675:
                        #kill the shot sprite (remove it from all groups)
                        alshot.kill()
                    #otherwise
                    else:
                        #if the rectangle of the shot collides with the rectangle of the player
                        if alshot.rect.colliderect(player.rect):
                            print('player die')
                            #kill the shot
                            alshot.kill()
                            #if the sound effects setting is true
                            if game_settings.soundeffects:
                                #play the player death sound effect
                                player_die_sound.play()
                            #call the player kill method
                            player.kill_player(draw_page)
                            #update the lives text
                            lives_display.change_text(str(player.lives), draw_page)
                            #remove the rightmost lives image
                            for img in lives_image_display:
                                img.kill()
                                break

                #for every player shot
                for shot in projectiles:
                    #if the rectangle of the shot collides with the rectangle of the alien shot
                    if alshot.rect.colliderect(shot.rect):
                        #if the player shot is moving
                        if shot.moving:
                            #kill both shots
                            shot.kill()
                            alshot.kill()

        #if there is a mother ship
        if len(mother_ship) > 0:
            #for every mother ship
            for mother in mother_ship:
                #move the mother ship
                mother.move()
                #if the sound effects setting is true play the mothership soundeffect
                if game_settings.soundeffects:
                    mother_ship_sound.play()

                #if the mother ship is off the left side of the page
                if mother.position[0] < -20:
                    #kill the mother ship
                    mother.kill()

        #if the mother ship timer is greater than or equal to the current mother ship time interval
        if mother_Ship_Timer_Elapsed >= mother_Ship_Time:
            #create a new mother ship and add it to the group
            new_mother = Mother_Ship()
            mother_ship.add(new_mother)
            #reset the timer
            mother_Ship_Time = uniform(10, 25)
            mother_Ship_Timer = time.time()


        #if the a OR left arrow key is pressed AND the player is not at the left side of the screen
        if (pygame.key.get_pressed()[pygame.K_a] == 1 or pygame.key.get_pressed()[pygame.K_LEFT] == 1) and player.position[0] > 40:
            #move the player left
            player.move(-2)
        #otherwise if the d OR right arrow key is pressed AND the player is not at the right side of the screen
        elif (pygame.key.get_pressed()[pygame.K_d] == 1  or pygame.key.get_pressed()[pygame.K_RIGHT] == 1) and player.position[0] < 920:
            #move the player right
            player.move(2)

        #when the space bar is pressed
        if pygame.key.get_pressed()[pygame.K_SPACE]:

            #if there are no shots in the projectiles group
            if len(projectiles) == 0:
                #set can_shoot to true
                can_shoot = True

            #for every shot in th projectiles group
            for shot in projectiles:
                #if the moving indictor of the shot is true
                if shot.moving:
                    #set can_shoot to false
                    can_shoot = False
                    #leave the loop
                    break
                #otherwise
                else:
                    #set can_shoot to true
                    can_shoot = True

            #if can_shoot is true
            if can_shoot:
                #create a new shot and add it to the projectiles group
                newshot = Shot(player.position[0])
                projectiles.add(newshot)
                #if the soundeffects setting is true play the player shot soundeffect
                if game_settings.soundeffects:
                    player_shoot_sound.play()
                print(len(projectiles))

        #for every shot in the projectiles group
        for shot in projectiles:
            #if the moving indictor shot is true
            if shot.moving:
                #if the shot is bellow to top of the page
                if shot.position[1] - 8 > 0:
                    #if the shot is above the bottom of the bunkers
                    if shot.position[1] - 8 < 590:
                        #if the shot touches green
                        if (pygame.display.get_surface().get_at(((shot.position[0] - 8), shot.position[1] - 2))[1] == 225 or
                            pygame.display.get_surface().get_at(((shot.position[0] - 8), shot.position[1] + 2)))[1] == 255:
                            #blow up the shot
                            shot.blowup()

                    #for every mothership in the mother ship group
                    for mother in mother_ship:
                        #if the shot recangle collides with the mother ship rectangel
                        if shot.rect.colliderect(mother.rect):
                            #picka a random number between 0 and 3
                            points_added = randint(0,3)
                            #0 set points_added to 50 points
                            if points_added == 0:
                                points_added = 50
                            #otherwise if 1 set points_added to 100 points
                            elif points_added == 1:
                                points_added = 100
                            #othewise if 2 set points_added to 150 points
                            elif points_added == 2:
                                points_added = 150
                            #othewise set points_added to 300 points
                            else:
                                points_added = 300
                            #add points_added to the current score
                            highscoresvar.current_score += points_added
                            #update the current score display
                            current_Score_Display.change_text(str(highscoresvar.current_score), draw_page)
                            #kill the mother ship and the shot
                            mother.kill()
                            shot.kill()

                    #for every alien
                    for alien in aliens:
                        #if the shot rectangel collides with the alien rectangle
                        if shot.rect.colliderect(alien.rect):
                            #if the sound effects setting is true play the alien death sound effect
                            if game_settings.soundeffects:
                                alien_die_sound.play()
                            #kill the alien and add its points to the current score
                            highscoresvar.current_score += alien.kill_alien()
                            #update the score display
                            current_Score_Display.change_text(str(highscoresvar.current_score), draw_page)
                            #kill the shot
                            shot.kill()
                            print(highscoresvar.current_score)

                    #if the shot has not been killed by this point
                    #move the shot
                    shot.move()
                #otherwise
                else:
                    #kill the shot
                    shot.kill()

        #if the player dead indicator is true call the end game method
        if player.dead:
            end_game()

        #exits if the escape button is pressed
        if pygame.key.get_pressed()[pygame.K_ESCAPE] == 1:
            #make the mouse visible
            pygame.mouse.set_visible(True)
            #stop the background music
            pygame.mixer.music.stop()
            #run the home page
            hp.run_page()

        #if the quit button is pressed quit the game
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()


        #update the elpased time for all timers
        alien_Timer_Elapsed = time.time() - alien_Timer_Start
        alien_Shoot_Timer_Elapsed = time.time() - alien_Shoot_Timer
        mother_Ship_Timer_Elapsed = time.time() - mother_Ship_Timer
