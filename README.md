# AH-Computing-Project
Advanced Higher Computing Project.

This is the Advanced Higher project of Yannik Nelson.
The project is a game, in this case space invaders.

Mechanics:
  Aliens:
    There will be 5 layers of aliens.
    3 Types of aliens:
      10pts:
        These constitute the lower 2 layers.
      20pts:
        These constitute the 2 layers above the 10pts aliens.
      30pts:
        These constitute the top layer.
    There will be 11 aliens on each row.
    There will also be a bonus point 'mother ship' that will occationaly 
    travel accross the top of the screen, above all the aliens this will be worth 100pts.
      Bombs:
        There will be 2 types of projectile, shot (fast) and bomb (slow).
				
  Player:
    The player will only be able to move right and left.
    Shots will only come from the center of the player character, this makes the game harder.
    The player will have 3 'lives' in total, each time the player 'dies' there will be a short explosion animation.
	
  Barracade:
    There will be 4 barricades in total, each time a shot hits a barricade a 'chunk' will be taken out of it.
  
  Projectiles:
    There will be 3 types of projecties in total:
		The 2 bomb types of the Aliens, mentioned earlier.
		The last type is the type the player will be able to 'shoot'.
  
  Score:
    Throughout the game the score will be kept track of and shown at the very top of the 'canvas'.
    Once the game is over the user will be asked to input 3 letters to be their player name and once they
    submit the name the score will be compared to a file containing the top 5 scores, if it is higher than any
    of the scores it will replace them/slot in and shift down the list, removing the new 11th hihgest score.
    Any reppetitions of the scores will cause the names to be added together in a list style, e.g. YAN, BEN.
    This will not occur if the name is the same, if so no change will be made.
