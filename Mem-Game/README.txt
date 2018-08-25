# =============================================================================
#   Name:  Kenneth Perkins
#   Date:   Aug 8, 2013
#   Taken From: http://programmingnotes.freeweq.com/
#   File: README.txt
#   Description: This is the README file which describes any bugs and features 
#     along with a description of what was or was not completed in this 
#     assignment. This file describes the use of the program and if there are 
#     any external dependencies.
# =============================================================================

Ordered list:
    1. DESCRIPTION
    2. USAGE
    3. FEATURES
    4. EXTERNAL DEPENDENCIES
    5. BUGS        
    6. ADDITIONAL NOTES

==== 1. DESCRIPTION ====

Brainy Memory Game is a mind stimulating educational card game in which an 
assortment of cards are laid face down on a surface, and the player tries to
find and uncover two identical pairs. If the two cards match, they are removed 
from gameplay. If they do not match, the cards are turned back over. The object 
of the game is to find pairs of two matching cards in the fewest number of turns 
possible. This game can be played alone or with multiple players, and is 
especially challenging for children and adults alike.

==== 2. USAGE ====

This game utilizes the python "pygame" module (http://pygame.org). To play 
this game, it is assumed that the user already has python and pygame installed 
on their computer. If that is not the case, here are documents explaining how 
to obtain the necessary resources for play.

How to install Python: 
(1) http://python.org/getit/

How to install Pygame: 
(1) http://pygame.org/install.html
(2) http://pygame.org/download.shtml

After the required resources are obtained, to start the game, the easiest 
way to do this would be to extract the entire .zip file into the directory of
your choice, and to simply run the "memory.py" source file through the python
interpreter. Once the "memory.py" source file is run through the python 
interpreter, the game should automatically start.
 
==== 3. FEATURES ====

This game features various colorful images and sounds for a pleasant user 
experience. By default, there are 27 playing cards (image size: 80x80) for use 
located in the "img" folder, and more can be added by the player in the future
if they desire. 

==== 4. EXTERNAL DEPENDENCIES ====

Other than the pygame module, there are two other source files this program
depends on. They are named "gameBoard.py" and "gameMusic.py." 

"gameBoard.py" sets up the game board and playing cards for display. It also 
reads files (images/fonts) from the "img" & "fnt "directory for use within 
this program.

"gameMusic.py" sets up the game sounds and music. It also reads files 
(.ogg/.wav) from the "snd" directory for use within this program.

Both of these source files should be located in the same directory as
"memory.py"

==== 5. BUGS ====

NONE

==== 6. ADDITIONAL NOTES ====

• My game was influenced by another memory based game located here: http://www.pygame.org/project-Memory-1263-.html
  I used that game as my pygame tutorial as i've never used pygame before.

• Though some of the images from that game was borrowed and used in my game, 
  NONE OF THE SOURCE CODE WAS COPIED. THIS GAME WAS CREATED USING MY OWN SOURCE CODE 
  
• The fonts were found online (http://1001freefonts.com) aswell as the in game music.

----------
Visit My Programming Notes for more personal notes and actual homework exercises demonstrating simple examples on various programming concepts.

http://programmingnotes.freeweq.com/