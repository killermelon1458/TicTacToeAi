# TicTacToeAi
Hello! 
My name is KillerMelon and this is my passion project tictactoe game with AI. The base 
game was a school assignment but the AI I came up with on my own. I have no background 
in AI and did no research for how they are made. I also included 3 “bots.” I call them this 
because they just have rules to follow when picking moves. The “easy” bot picks 
random moves. The “medium”  bot  ranks moves in order of middle, corners, edges. The 
“hard” bot scans the board for chances to win, then chances to loose or random if neither 
of the other two criteria are met. All bots can be beat. The AI in contrast statistically chooses a move based on 
its training data to try to win the game. Properly trained it can always win or force a cat game.

In order to run TicTacToe.py the graphics.py module needs to be in the same directory. 
Once run, the game will create a sub-directory called tttData. All game logs  gameData.ttt 
and the .json files will be stored there. The ai will function, but have no data to pull from 
and therefore will pick random moves. 
      
      General Commands: in ipython or bottom of script

Main() starts the game. Main has 2 optional arguments. The first one is a pause time before 
any of the bots make a move. Default is set to .3 seconds. Set to 0 for no delay.
The second argument is games to run without asking the player to play again. Default is 1.

      Example Usage: 

* main() #for regular delay and to play regular
* main(0) #for no playing delay
* main(0,100) #to play with no delay and design for training the AI. Recommended to use 
      #with bot vs bot. Not for human play unless you want to play games really fast



To make the ai work with the data included:

 	Option 0:
*run the TTTsetup.exe. This is only for playing, not for modifying code. Windows will tell you 
its dangerous, its not but if you don’t trust me don’t run it.

      Option 1: 
* Before running the script create a sub directory to where the TicTacToe.py file is located 
named tttData
* Move the cat.json , win.json , and loose.json  files into the tttData directory. 
* Run the script.

	Option 2:
* Run the script but play no games then close
* Move the cat.json , win.json , and loose.json  files into the tttData directory. 

	Option 3:
* Run the script and play at least one game then close it.
* Move the cat.json , win.json , and loose.json  files into the tttData directory. When 
prompted replace files



To train the Ai yourself ignore all previous steps.

* Run the scrypt in ipython and play games. 
	*all games are logged and train the ai

* To automate: 
      * In the ipython terminal type main(0,numOfRuns)
      	*recommended at least 25,000 easy(random) vs easy(random)
		*It is recommended at least one of the players be easy when training to 
get proper coverage
		*if you want the ai to play while training it is recommended to go to function 
“scoresAvailableAi”  go to line:
catScore = (LoLoScores[2][j][0]/numOfCats)/100 #and change it to 
catScore = (LoLoScores[2][j][0]/numOfCats)*0 
This make it not use cat games to make decisions when training. Otherwise it can quickly 
get stuck doing cat games instead of winning

	Other stuff:
Also included is the script I used to train on gameData######.ttt files that already exist 
without playing the game, named training_scirpt.py Change the for loop range numbers 
based of the number of .ttt files you have. You can also get this number from the tttData.ttt 
file while the game is not running. 

The game creates 4 gameData.ttt files for every game played. Each one is rotated 90 from 
the last. This is to reduce training coverage requirements.


	

      	

