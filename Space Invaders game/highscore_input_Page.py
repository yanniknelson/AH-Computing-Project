import pygame
from basic_Resources import *
from button_class import *
import highscore_display_Page as hdp
import time

#text object for title
Title = Text("HIGHSCORE!", 72, 480, 106)
#text object for left initial
left_initial = Text("", 250, 270, 400)
#rectangle for left initial
left_underline = pygame.Rect(180, 520, 150, 5)
#text object for middle initial
middle_initial = Text("", 250, 495, 400)
#recatngle for middle initial
middle_underline = pygame.Rect(405, 520, 150, 5)
#text object for right initial
right_initial = Text("", 250, 720, 400)
#rectangle for right initial
right_underline = pygame.Rect(630, 520, 150, 5)
#text object to display enter intructions
enter_Text = Text("press enter to submit", 16, 480, 560)
#skip button
skip_button = Button("skip", 830, 640)
#surface variable for easier access
surface = pygame.display.get_surface()
#colour variable for easier access
White = (255,255,255)
#variable to identify the currently selected initial place
currently_selected = 0
#variable to identify the visible state of the currently currently_selected
#place's underline
flash_on = True

def draw_page():
    global flash_on
    global currently_selected
    #fill the background in black
    pygame.display.get_surface().fill((0,0,0))
    #display all the text objects
    Title.display_text()
    left_initial.display_text()
    middle_initial.display_text()
    right_initial.display_text()
    enter_Text.display_text()

    #chooses the underline that will flash
    if currently_selected == 0:
        #when flash on is true display the currently selected left_underline
        #when not, don't
        if flash_on:
            pygame.draw.rect(surface, White, left_underline)
        pygame.draw.rect(surface, White, middle_underline)
        pygame.draw.rect(surface, White, right_underline)
    elif currently_selected == 1:
        pygame.draw.rect(surface, White, left_underline)
        if flash_on:
            pygame.draw.rect(surface, White, middle_underline)
        pygame.draw.rect(surface, White, right_underline)
    elif currently_selected == 2:
        pygame.draw.rect(surface, White, left_underline)
        pygame.draw.rect(surface, White, middle_underline)
        if flash_on:
            pygame.draw.rect(surface, White, right_underline)
    #when all characters have been input display all underlines
    else:
        pygame.draw.rect(surface, White, left_underline)
        pygame.draw.rect(surface, White, middle_underline)
        pygame.draw.rect(surface, White, right_underline)

    #display skip button
    skip_button.display_Button()
    #update display
    pygame.display.flip()

def run_page(highscores):
    #draw the page
    draw_page()
    #stores the input initials
    initials = ""
    left_initial.change_text("", draw_page)
    middle_initial.change_text("", draw_page)
    right_initial.change_text("", draw_page)
    #variables used to keep track of time between flashes
    flash_start = time.time()
    flash_elapsed = time.time() - flash_start
    global currently_selected
    #ensures the currently selected is the first initial when the page loads
    currently_selected = 0
    global flash_on
    while True:

        #check if the mouse is over the skip button
        skip_button.hover_Check(draw_page, hdp.run_page)

        #if the time since the last flash is greater than or equal to 0.4s
        if flash_elapsed >= 0.4:
            #switch the state of the flash on variable
            flash_on = not flash_on
            print(flash_on)
            #redraw the page
            draw_page()
            #restart flash timer
            flash_start = time.time()

        #get every current event
        for event in pygame.event.get():
            #if the event is the quit button being clicked
            if event.type == pygame.QUIT:
                #quit the game
                pygame.display.quit()
                pygame.quit()
                sys.exit()

            #if the event is a key being pressed
            if event.type == pygame.KEYDOWN:
                print("pressed")
                print(event.key)
                #chagne the text under the underlines to "press enter to submit"
                enter_Text.change_text("press enter to submit", draw_page)
                #if the key pressed is an alpha character
                if event.unicode.isalpha():
                    #display the pressed character in the currently selected
                    #initial place
                    if currently_selected == 0:
                        left_initial.change_text(event.unicode, draw_page)
                    elif currently_selected == 1:
                        middle_initial.change_text(event.unicode, draw_page)
                    elif currently_selected == 2:
                        right_initial.change_text(event.unicode, draw_page)

                    #if the inital place indicator is refering to a place
                    if currently_selected < 3:
                        #move it up one place
                        currently_selected = currently_selected + 1
                        #add the pressed key the the initials store
                        initials += event.unicode

                    print(initials)

                #if the key isn't an alpha characters
                #if the key is back space
                elif event.key == 8:
                    #stop displaying the initial in the place last added to
                    if currently_selected == 1:
                        left_initial.change_text("", draw_page)
                    elif currently_selected == 2:
                        middle_initial.change_text("", draw_page)
                    elif currently_selected == 3:
                        right_initial.change_text("", draw_page)

                    #if the place indicator isn't refering to the first inital
                    if currently_selected > 0:
                        #move it down one place
                        currently_selected -= 1
                        #remove the last initial in the initial store
                        initials = initials[:-1]

                #if the key isn't alpha or backspace
                #if the key is enter
                elif event.key == 13:
                    #if less than 3 initials have been input
                    if len(initials) < 3:
                        #change the text under the underlines to "Please input 3 Characters"
                        enter_Text.change_text("Please input 3 Characters", draw_page)
                    #otherwise
                    else:
                        #instanciate a new highscore object with the name value of the initials (upper case)
                        #and the value of the current score stored in the highscores obect passed into the procedure
                        new_score = Highscore(initials.upper(), highscores.current_score)
                        #if there are less than 10 highscores
                        if len(highscores.scores) < 10:
                            #add new_score to the scores array of the highscores object passed in
                            highscores.scores.append(new_score)
                        #otherwise
                        else:
                            #replace the 10th object in the scores array of the highscores object passed in
                            #with new_score
                            highscores.scores[9] = new_score
                        #sort the list of highscores
                        highscores.bubble_sort_scores()
                        #write the highscores to the highscores file
                        highscores.write_file(True, True)
                        hdp.run_page()

                    #print(initials)
        #update time elapsed over the loop
        flash_elapsed = time.time() - flash_start
