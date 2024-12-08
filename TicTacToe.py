#
# hw9pr3.py
#
# Name:Malachi
#

# TTT-class
# game-play AND visualization!
from graphics import *
import random
from time import sleep
import os
#import threading
import traceback
import json
import sys

class TTT:
    
    
    def __init__(self,strData):
        """When creating a class TTT object include a string and this will create a TTT board"""
        self.data_string = ''
        N = len(strData)
        for k in range(9):
            if k >= N:
                break
            else:
                self.data_string = self.data_string + strData[k] #this constucts the initial string
        self.board = TTT.boardFromDataString(self.data_string) # this initializes the .board data member 

    def boardFromDataString(dataString):
        """This function takes in a sting and outs puts a LOL with 3 rows and 3 columns. functionaly 'making' a TTT Board"""
        tttBoard = [ [' ',' ',' '], [' ', ' ',' '], [' ',' ',' ']]
        N = len(dataString)
        for k in range(N):
            r = k // 3 #as k goes up this returns the same integer 3 times then goes up by one
            c = k % 3 #this returns 0-2 then resets
            # these allow for you to index through a 3x3 grid 
            tttBoard[r][c] = dataString[k]
        return tttBoard

    def __repr__(self):
        s = ''
        for k in range(30):
            r = k // 6
            c = k % 6
            if (r % 2 == 0) and (c % 2 == 1):#this checks if if the row is even and the column is odd
                if c < 5: #staying within the bound of a TTT board 
                    s = s + '|' #writing separating bars on the od columns
                else:
                    s = s + '\n' #after a row is complete going to the next line
            elif (r % 2 == 1) and (c % 2 == 1):#row odd and column odd check
                if c < 5: #staying within the bound of a TTT board
                    s = s + '+' #this adds the intersections of the board 
                else:
                    s = s + '\n' #after a row is complete going to the next line
            elif (r % 2 == 1) and (c % 2 == 0):#row odd and column even check
                s = s + '-' #this add the horizontal dividers in the board
            else:
                s = s + self.board[r//2][c//2]# this fills in all the X's and )'s
        return s
    def dataStringFromBoard(board):
        """This takes in a list of list and converst the contents to a string from left to right top to bottom"""
        boardStr = ''
        for row in range(3):
            for column in range(3):
                boardStr += board[row][column]
        return boardStr
    def  addMove(self, row, col, ox):
        """This adds a char to any place on the board. Takes integer Row and Column and a char arguments. Also updates data_string data member of intance of class."""
        self.board[row][col] = ox
        self.data_string = TTT.dataStringFromBoard(self.board)
    def checkMove (self, row, col):
        """This checks if any place on the board is ' ' And that the input is on the board. Takes integer Row and Column arguments. Returns Boulion."""
        if 0<= row <=2 and 0<= col <=2:
            if self.board[row][col] == ' ':
                return True
            else:
                return False
        else:
            return False
    def checkDelete (self, row, col):
        """This checks that the input is on the board. Takes integer Row and Column arguments. Returns Boulion."""
        if 0<= row <=2 and 0<= col <=2:
            return True
        else:
            return False
        
    def deleteMove(self, row, col):
        """Uses addMove to set any place on the board to ' ' . Takes integer Row and Column arguments"""
        if 0<= row <=2 and 0<= col <=2:
            TTT.addMove(self, row, col, ' ')
    def clearBoard(self):
        """Sets the whole board to ' ' ."""
        for row in range(3):
            for column in range(3):
                self.board[row][column] = ' '
    def winsFor(self, ox):
        winner = ' '
        
        for row in range(3):
            if self.board[row][0] == self.board[row][1] and self.board[row][0] == self.board[row][2] and self.board[row][0] != ' ':
                winner = str(self.board[row][0])
                
        for col in range(3):
            if self.board[0][col] == self.board[1][col] and self.board[0][col] == self.board[2][col] and self.board[0][col] != ' ':
                winner = str(self.board[0][col])
                
        if self.board[1][1] == self.board[0][0] and self.board[1][1] == self.board[2][2] and self.board[1][1] != ' ':
            winner = str(self.board[1][1])
            
        if self.board[1][1] == self.board[0][2] and self.board[1][1] == self.board[2][0] and self.board[1][1] != ' ':
            winner = str(self.board[1][1])
            
        
        if winner == ox:
            return True
        else:
            return False
        
        

    def movesAvailable(self):
        LoMoves = self.data_string
        outList=[]
        place = -1
        for e in LoMoves:
            place += 1
            if e == " ":
                outList += [place]
        return outList
    
    def scoresAvailableMed(self,Turn):
        """For an instance of a TTT board its take a sting argument of 'X' or 'O' and returns a list of lists with data paired as score then boardplace"""
        #this is a simple scoring system that rands the middle as best corners as second best and edges as worst. It picks random for first move.
        
        moves = self.movesAvailable()
        outlist=[]
        
        if moves == [0, 1, 2, 3, 4, 5, 6, 7, 8]:
            for e in moves:
                rand = random.randint(1,6)
                new = [rand, e]
                outlist += [new]
        
        else:
            for e in moves:
                if e%2 == 0 and e !=4:
                    new = [3,e]
                elif e%2 == 1:
                    new = [2,e]
                elif e == 4:
                    new = [4,e]
                outlist += [new]
        return outlist
    
    def scoreAvailableRand(self):
        """For an instance of a TTT board its takes no arguments and returns a list of lists with data paired as score then boardplace"""
        #this scores the moves randomly, no logic involved
        moves = self.movesAvailable()
        outlist=[]
        
        for e in moves:
            rand = random.randint(1,8)
            new = [rand, e]
            outlist += [new]
        
        return outlist
    
    def scoresAvailableWin(self,currentPlayer):
        """For an instance of a TTT board its take a sting argument of 'X' or 'O' and returns a list of lists with data paired as score then boardplace"""
        #This systematically goes thru every posible board state and wins if possible, stops the enemy from winning. And blocks attempts to get trapped
        #yes there are redundant parts of code, that could be combinded to make it shorter but copy pasta is easy and the little arrow that hides functions code, hides all wrongs

        board = self.board

        enemy = turnSwitch(currentPlayer)
        
        scoreList =[]
        
        #checking for if can win
        for row in range(3):
            moveCount = 0
            potentialMove =[]
            for col in range(3):
                if board[row][col]== currentPlayer:
                    moveCount +=1
                if board[row][col] == ' ':
                    potentialMove = [row,col]     
            if moveCount == 2 and potentialMove != []:
                pos = potentialMove[0]*3+potentialMove[1] #calulating linear position
                scoreList += [[8,pos]]
        potentialMove =[]
        for col in range(3):
            moveCount = 0
            potentialMove =[]
            for row in range(3):
                if board[row][col]== currentPlayer:
                    moveCount +=1
                if board[row][col] == ' ':
                    potentialMove = [row,col]     
            if moveCount == 2 and potentialMove != []:
                pos = potentialMove[0]*3+potentialMove[1] #calulating linear position
                scoreList += [[8,pos]]
        #checking diagonal wins left top to right bottom
        moveCount =0
        potentialMove =[]
        if board[0][0] == currentPlayer:
            moveCount +=1
        elif board[0][0] == ' ':
            potentialMove = [0,0]
        if board[1][1] == currentPlayer:
            moveCount +=1        
        elif board[1][1] == ' ':
            potentialMove = [1,1]
        if board[2][2] == currentPlayer:
            moveCount +=1        
        elif board[2][2] == ' ':
            potentialMove = [2,2]
        if moveCount == 2 and potentialMove != []:
            pos = potentialMove[0]*3+potentialMove[1] #calulating linear position
            scoreList += [[8,pos]]
        #checking diagonal wins left bottom to right top
        moveCount =0
        potentialMove =[]
        if board[2][0] == currentPlayer:
            moveCount +=1
        elif board[2][0] == ' ':
            potentialMove = [2,0]
        if board[1][1] == currentPlayer:
            moveCount +=1        
        elif board[1][1] == ' ':
            potentialMove = [1,1]
        if board[0][2] == currentPlayer:
            moveCount +=1        
        elif board[0][2] == ' ':
            potentialMove = [0,2]
        if moveCount == 2 and potentialMove != []:
            pos = potentialMove[0]*3+potentialMove[1] #calulating linear position
            scoreList += [[8,pos]]
        
        #checking for if will loose
        for row in range(3):
            moveCount = 0
            potentialMove =[]
            for col in range(3):
                if board[row][col]== enemy:
                    moveCount +=1
                if board[row][col] == ' ':
                    potentialMove = [row,col]     
            if moveCount == 2 and potentialMove != []:
                pos = potentialMove[0]*3+potentialMove[1] #calulating linear position
                scoreList += [[7,pos]]
        potentialMove =[]
        for col in range(3):
            moveCount = 0
            potentialMove =[]
            for row in range(3):
                if board[row][col]== enemy:
                    moveCount +=1
                if board[row][col] == ' ':
                    potentialMove = [row,col]     
            if moveCount == 2 and potentialMove != []:
                pos = potentialMove[0]*3+potentialMove[1] #calulating linear position
                scoreList += [[7,pos]]
        #checking diagonal wins left top to right bottom
        moveCount =0
        potentialMove =[]
        if board[0][0] == enemy:
            moveCount +=1
        elif board[0][0] == ' ':
            potentialMove = [0,0]
        if board[1][1] == enemy:
            moveCount +=1        
        elif board[1][1] == ' ':
            potentialMove = [1,1]
        if board[2][2] == enemy:
            moveCount +=1        
        elif board[2][2] == ' ':
            potentialMove = [2,2]
        if moveCount == 2 and potentialMove != []:
            pos = potentialMove[0]*3+potentialMove[1] #calulating linear position
            scoreList += [[7,pos]]
        #checking diagonal wins left bottom to right top
        moveCount =0
        potentialMove =[]
        if board[2][0] == enemy:
            moveCount +=1
        elif board[2][0] == ' ':
            potentialMove = [2,0]
        if board[1][1] == enemy:
            moveCount +=1        
        elif board[1][1] == ' ':
            potentialMove = [1,1]
        if board[0][2] == enemy:
            moveCount +=1        
        elif board[0][2] == ' ':
            potentialMove = [0,2]
        if moveCount == 2 and potentialMove != []:
            pos = potentialMove[0]*3+potentialMove[1] #calulating linear position
            scoreList += [[7,pos]]
        """
        #this prevents all corner traps and should not be commented out if this bot is supposed to be unbeatable
        potentialMove =[]
        if (board[0][0] == enemy and board[1][1] == currentPlayer and board[2][2] == enemy) or (board[2][0] == enemy and board[1][1] == currentPlayer and board[0][2] == enemy):
            if board[0][1] == ' ' and board[1][0] == ' ' and board[1][2] == ' ' and board[2][1] == ' ':
                potentialMoves = [[0,1],[1,0],[1,2],[2,1]]
                for e in potentialMoves:
                    pos = e[0]*3+e[1]
                    scoreList += [[5,pos]]  
        
        #this creates a random first move
        moves = self.movesAvailable()
        if moves == [0, 1, 2, 3, 4, 5, 6, 7, 8]:
            #scoreList += [[7,1]]
            for e in moves:
                rand = random.randint(4,6)
                new = [rand, e]
                scoreList += [new]
        #^this should be commented out to make this bot unbeatable


        #filling all available moves with a value for all cases other that win or loose
        #yes i know this creats duplicate possible moves but its ok because ones from this 
        # list will be scored lower than from the previous list
        

        moves = self.movesAvailable()
        for e in moves:
            if e%2 == 0 and e !=4:
                new = [3,e]
            elif e%2 == 1:
                new = [2,e]
            elif e == 4:
                new = [4,e]
            scoreList += [new]
        """
        moves = self.movesAvailable()
        for e in moves:
            scoreList += [[1,e]]
        return scoreList
    

    def scoresAvailableAi(self,LoDicts,Turn):
        """For an instance of a TTT board its take a list of 3 dictionaries and a string argument of 'X' or 'O' and returns a list of lists with data paired as score then boardplace"""
        

        LoLoScores =[[],[],[],[]]
        sumScores=[]
        numOfWin = LoDicts[0]['count']
        numOfloose=LoDicts[1]['count']
        numOfCats=LoDicts[2]['count']
        moves = self.movesAvailable()
        key = gameBoardToKey(self.data_string,Turn)
        for i in range(3):
            if key in LoDicts[i]:
                for e in moves:
                    LoLoScores[i] += [[LoDicts[i][key][e],e]]
            else:
                for e in moves:
                    LoLoScores[i] += [[1,e]]
        LoLoScores[3] = self.scoreAvailableRand()
        for e in moves:
            LoLoScores[3]+= [[random.choice(range(3)),e]]
        for j in range(len(moves)):

            winsScore = LoLoScores[0][j][0]/numOfWin
            looseScore = (LoLoScores[1][j][0]/numOfloose)*8
            catScore = (LoLoScores[2][j][0]/numOfCats)/100
            randScore = LoLoScores[3][j][0]/numOfWin
            overalScore = (winsScore+catScore+randScore)-(looseScore)
            
            sumScores+= [[overalScore,LoLoScores[0][j][1]]]
        return sumScores
    
    def bestMoves(self,Turn,player,LoDicts):
        #this sorts through the moves an returns the one with the highest score, it also handles sorting which bot will be used.
        if player == 'hard':
            scores =self.scoresAvailableWin(Turn)
        elif player == 'medium':
            scores = self.scoresAvailableMed(Turn)
        elif player == 'easy':
            scores = self.scoreAvailableRand()
        elif player == 'ai':
            scores = self.scoresAvailableAi(LoDicts,Turn)
        

        bestSc = scores[0][0]
        for e in scores:
            current = e[0]
            if current> bestSc:
                bestSc = current
        bestL = []
        for j in scores:
            if j[0] == bestSc:
                bestL += [j[1]]
        return bestL
    
    def aiMove(self,Turn, player,LoDicts):
        """"""
        bestMs= self.bestMoves(Turn,player,LoDicts)
        if len(bestMs)>=2:
            move = random.choice(bestMs)
        else:#This check existed to troubleshoot a bug and seems fine to leave in
            move = int(bestMs[0])
        row = move//3
        col = move%3
        return [row,col]


    

def indexOfString(gameline, winner):
    """This takes a sting of spaces and finds the first place where the specified character is"""
    #not used for my current ai
    firstPos = 0
    for i in gameline:
        if i == " ":
            firstPos +=1
        elif i == winner:
            return firstPos
        else:
            return -1 #a little c like i know, buts it usefull

def rotateBoard(filePath):
    """this take a log file and creates a exivelent log file with the board rotated 90 degress. it returns the file path of the created file and an updated file number for the file counter to use"""
    file = os.path.basename(filePath)
    filename = file[:-4]
    filenum=int(filename[8:])
    fileDir = os.path.dirname(filePath)
    newFilePath = os.path.join(fileDir,'gameData'+str(filenum+1).zfill(6)+'.ttt')

    log = open(filePath, 'r', encoding='utf-8')
    newFile = open(newFilePath, 'w', encoding='utf-8')

    line = log.readline()
    
   
    while line != '':
        newLine = ''
        newLine += line[6]
        newLine += line[3]
        newLine += line[0]

        newLine += line[7]
        newLine += line[4]
        newLine += line[1]

        newLine += line[8]
        newLine += line[5]
        newLine += line[2]

        newLine += line[9]
        newLine += line[10]
        if len(line) ==12:
            newLine += line[11]
            
        newFile.write(newLine)

        line = log.readline()
    log.close()
    newFile.close()
    return newFilePath,str(filenum+2).zfill(6)

    
def sortThroughOne(filePath):
    """takes a filepath and returns a list of list of strings. each internal 
    list contains moves in terms of self and enemy this allows all the data to work
    for both x and o. lists are in order of: winner = s, loser =s, firstplayer = s, secondplayer= s"""
    #yes this should have been two or three functions but i was in the scripting mood. 
    gameData = open(filePath, 'r', encoding= "utf-8")
    lineCount = -1
    line ='magnus_dingus'
    firstMove = ' '
    line = gameData.readline()
    if len(line)<9:
        return [[],[],[],[]]
    for i in range(9):
        if line[i] != ' ':
            firstMove = line[i] 
        

    gameData.seek(0)
    while line != '': #counts the number of lines
        line = gameData.readline()
        lineCount +=1
    
    winPos = (lineCount - 1)*13 + 10 #calculates where the the winning character is
    
    gameData.seek(winPos)
    gameWinner = gameData.read(1)
    
    listOfWinLines =[]
    listOfLooseLines =[]
    listofFirstMovers =[]
    listof2ndMovers =[]
    
    if gameWinner == 'X' or gameWinner == 'O':

        gameData.seek(0)
        if gameWinner == firstMove:
            listOfWinLines =['         ']
            listOfLooseLines =[]
        else:
            listOfWinLines =[]
            listOfLooseLines =['         ']

        for e in range(lineCount):
            line = gameData.readline()
            winLine = ''
            looseLine = ''
            for let in range(9):
                if line[let] == ' ':
                    winLine += ' '
                    looseLine += ' '
                elif line[let] == gameWinner:
                    winLine += 'S'
                    looseLine +='E'
                else:
                    winLine +="E"
                    looseLine +='S'
            listOfWinLines.append(winLine)
            listOfLooseLines.append(looseLine)
            
    if gameWinner == 'n' and lineCount == 9:
        
        
        secondMove = turnSwitch(firstMove)
        gameData.seek(0)
        listofFirstMovers =['         ']
        listof2ndMovers =[]
        for e in range(9):
            line = gameData.readline()
            firstMoveLine = ''
            secondmoveLine = ''
            for let in range(9):
                if line[let] == ' ':
                    firstMoveLine += ' '
                    secondmoveLine += ' '
                elif line[let] == firstMove:
                    firstMoveLine += 'S'
                    secondmoveLine += 'E'
                elif line[let] == secondMove:
                    firstMoveLine += 'E'
                    secondmoveLine += 'S'
            listofFirstMovers.append(firstMoveLine)
            listof2ndMovers.append(secondmoveLine)
            
    return [listOfWinLines,listOfLooseLines,listofFirstMovers,listof2ndMovers]

def pairingData(gameData):
    """takes a list of board states and returns list of pairs.  every other board state with where self went next  """
    count = 0
    
    listOfPairs = []
    for e in gameData:
        if count%2 == 0:
            pair=[e,0]
        
        elif (count+1)%2 ==0:
            strCount= 0
            for i in range(9):
                     
                if e[i] != pair[0][i]:
                    pair[1] = strCount
                strCount +=1
            listOfPairs += [pair]
        count +=1
            
    return listOfPairs

def addPairsToDict(listOfPairs, dict):
    """takes a list of pairs and dict and returns the dict with the data added"""
    if listOfPairs == []:
        return dict
    for pair in listOfPairs:
        if pair[0] not in dict:
            dict[pair[0]] = [0]*9
        board = pair[0]
        move = pair[1]
        dict[board][move]+=1
    return dict

def sortDataToDicts(listOfDics, listOfBoards):
    ind = 0
    listOfPairs =[[]]*4
    for e in listOfBoards:
        listOfPairs[ind]=pairingData(e)
        ind+=1
    for i in range(2):
        listOfDics[i]=addPairsToDict(listOfPairs[i],listOfDics[i])
        if listOfPairs[i]!=[]:
            listOfDics[i]['count']+=1
        listOfDics[2]=addPairsToDict(listOfPairs[i+2],listOfDics[2]) #yes i know this being in this loop is probably bad practice but it works. 
        if listOfPairs[i+2]!=[]:
            listOfDics[2]['count']+=1
        
    return listOfDics

def gameBoardToKey(board,Turn):
    """takes a string of length 9 and a string representing whos turn it is and returns a string with turn as S and the opponent as E"""
    if len(board) != 9:
        raise ValueError('board needs to be a 9 letter string')
    key = ''
    for e in board:
        if e ==' ':
            key += ' '
        elif e == Turn:
            key += 'S'
        elif e == turnSwitch(Turn):
            key += 'E'
        else: 
            return ''
    return key
        



def sortThroughData(maxFile):
    """takes a int representing the max file number that is in the dataBase of games returns a 
    dictionary with keys 0-8 whos len of data represent win frequency """
    #Most all of my code is generalized to work for both x and o. 
    # therefore this checks if the first move index of the winner of the game
    #
    #since this sorts through data stored on my computer i see no reason 
    #for it to be in the class
    #
    #i made this before i decide to make my ai. This sorts for first move prabability

    curentDir = os.path.dirname(sys.executable if getattr(sys, 'frozen', False) else __file__)
    currentDirTTT = os.path.join(curentDir,'tttData')
    
    lineCount = 0
    firstMoveWins={}
    for i in range(9):
        firstMoveWins[i] = []
    progressPrintVariable = 0
    for i in range(1,maxFile+1):
        if i%10000 == 0:
            progressPrintVariable+=1
            print(str(progressPrintVariable)+'%')
        line = 'magnus_dingus' #tribute to Tristen
        #path to the file
        fileCount = str(i).zfill(6)
        pathToData = os.path.join(currentDirTTT, "gameData"+fileCount+".ttt")
        gameData = open(pathToData, 'r', encoding= "utf-8")

        #who won in this game
        lineCount = 0
        while line != '': #counts the number of lines
            line = gameData.readline()
            lineCount +=1
        if lineCount < 5:
            gameData.close()
            continue
        winPos = (lineCount - 2)*13 + 10 #calculates where the the winning character is
        gameData.seek(winPos)
        gameWinner = gameData.read(1)

        #converting first lin to a 0-8 locataion
        gameData.seek(0)
        firstLine = gameData.readline()
        firstPos = indexOfString(firstLine, gameWinner)
        if firstPos >=0:
            firstMoveWins[firstPos] += [[gameWinner]]
        gameData.close()

    return firstMoveWins

def firstMoveFreqs(firstWinDict, maxFile):
    
    moveFreqs = [0]*9
    for i in range(9):
        moveFreqs[i] = len(firstWinDict[i])/maxFile
    return moveFreqs

    

def makeBoardGraphics(title, scale, color):
    """Takes arguents string, scale, color. Returns graphwin object."""
    TTTBoard = GraphWin(title, 500*scale, 425*scale)
    TTTBoard.setBackground(color_rgb(121,213,219))
    stile1 = Rectangle(Point(196*scale,50*scale), Point(204*scale,350*scale))#stiles are what we call the verticle pieces of wood in a door
    stile2 = Rectangle(Point(296*scale,50*scale), Point(304*scale,350*scale))
    rail1 = Rectangle(Point(100*scale,146*scale), Point(400*scale,154*scale))#rails are what we call the horizontal pieces of wood in a door
    rail2 = Rectangle(Point(100*scale,246*scale), Point(400*scale,254*scale))
    winBoard = [stile1,stile2,rail1,rail2]
    for line in winBoard:
        line.setOutline(color)
        line.setFill(color)
        line.draw(TTTBoard)
    
    return TTTBoard

def getMoveFromMouse(tttWin):
    scale = (tttWin.getWidth())/500
    pos = 0
    while pos == 0:
        clickPoint= tttWin.getMouse()
        
        if clickPoint.getX() >= 100*scale and clickPoint.getX() <= 196*scale:
            if clickPoint.getY() >= 50*scale and clickPoint.getY() <=146*scale:
                pos = (0,0)
            elif clickPoint.getY() >= 154*scale and clickPoint.getY() <=246*scale:
                pos = (1,0)
            elif clickPoint.getY() >= 254*scale and clickPoint.getY() <=350*scale:
                pos = (2,0)
            else:
                pos = 0
        elif clickPoint.getX() >= 204*scale and clickPoint.getX() <= 296*scale:
            if clickPoint.getY() >= 50*scale and clickPoint.getY() <=146*scale:
                pos = (0,1)
            elif clickPoint.getY() >= 154*scale and clickPoint.getY() <=246*scale:
                pos = (1,1)
            elif clickPoint.getY() >= 254*scale and clickPoint.getY() <=350*scale:
                pos = (2,1)
            else:
                pos = 0
        elif clickPoint.getX() >= 304*scale and clickPoint.getX() <= 400*scale:
            if clickPoint.getY() >= 50*scale and clickPoint.getY() <=146*scale:
                pos = (0,2)
            elif clickPoint.getY() >= 154*scale and clickPoint.getY() <=246*scale:
                pos = (1,2)
            elif clickPoint.getY() >= 254*scale and clickPoint.getY() <=350*scale:
                pos = (2,2)
            else:
                pos = 0
    return pos

def scaleFontSize(size, scale):
    """This takes in a desired font size and a board scale both returns an integer that is in bounds for the graphics module"""
    fontSize = size*scale
    if fontSize >36:
        fontSize = 36
    if fontSize < 5:
        fontSize = 5
    return int(fontSize)
        
def initTextArray(tttWin, tSize):
    scale = (tttWin.getWidth())/500
    outArray = [[None, None, None], [None, None, None], [None, None, None]]
    yPos = 100
    for row in range(3):
        xPos = 150
        for col in range(3):
            OXText = Text(Point(xPos*scale,yPos*scale), ' ')
            fontSize = scaleFontSize(tSize, scale)
            OXText.setSize(int(fontSize))
            outArray[row][col] = OXText
            xPos += 100
        yPos += 100
    return outArray
def drawTextArray(tArray,tttWin):
    for row in range(3):
        for col in range(3):
            tArray[row][col].draw(tttWin)
def undrawTextArray(tArray,tttWin):
    for row in range(3):
        for col in range(3):
            tArray[row][col].undraw()
def clearTextArray(tArray,tttWin):
    for row in range(3):
        for col in range(3):
            tArray[row][col].setText(' ')
def updateTextArray(tArray,tttObj):
    for row in range(3):
        for col in range(3):
            tArray[row][col].setText(tttObj.board[row][col])
    


def makeGameMessage(tttWin, message):
    scale = (tttWin.getWidth())/500
    
    mOut = Text(Point(250*scale,25*scale), message)
    fontSize = scaleFontSize(28, scale)
    mOut.setSize(int(fontSize))
    return mOut

def makeDualButton(tttWin,lButton,rButton,message):
    scale = (tttWin.getWidth())/500
    box = Rectangle(Point(150*scale,383*scale),Point(350*scale,417*scale))
    yText = Text(Point(200*scale,400*scale),lButton)
    nText = Text(Point(300*scale,400*scale),rButton)
    playText =Text(Point(250*scale,365*scale),message)
    divider = Line(Point(250*scale,383*scale),Point(250*scale,417*scale))
    fontSize = scaleFontSize(10, scale)
    yText.setSize(int(fontSize))
    nText.setSize(int(fontSize))
    playText.setSize(int(fontSize))
    bList =[box,yText,nText,playText,divider]
    return bList

def drawButton(bList, tttWin):
    for obj in bList:
        obj.draw(tttWin)
def undrawButton(bList):
    for obj in bList:
        obj.undraw()
def pressButton(tttWin):
    answer = None
    scale = (tttWin.getWidth())/500
    while answer == None:
        clickPoint = tttWin.getMouse()
        if clickPoint.getY() > 383*scale and clickPoint.getY() < 417*scale:
            if clickPoint.getX() > 150*scale and clickPoint.getX() < 250*scale:
                answer = "left"
            elif clickPoint.getX() > 250*scale and clickPoint.getX() < 350*scale:
                answer = "right"
    return answer

def turnSwitch(player):
    """This function takse in a sting 'X' or 'O' and returns the opposite. If some other input it will return input"""
    if player == "X":
        player = "O"
    elif player == "O":
        player = "X"
    return player

def makeLogDirectory():

    #path creation for log files
    current_dir = os.path.dirname(sys.executable if getattr(sys, 'frozen', False) else __file__) #gets current working directory
    ttt_data_dir = os.path.join(current_dir, "tttData") #this essential concatinates the folder to the directory makeing sure its properly formated
    os.makedirs(ttt_data_dir, exist_ok=True) #this creates the specified directory. exist_ok = True specifies that its k if the directory already exists.
    
    #data file create or open
    if os.path.isfile("tttData.ttt"):
        data = open("tttData.ttt","r+", encoding="utf-8") #this file acts to long term store how many games have been played
    elif not os.path.isfile("tttData.ttt"):
        data = open("tttData.ttt","w+", encoding="utf-8")
    fileCount = data.readline()
    
    #checking if data file is empty and initiallizing the count in the file
    if fileCount == '':
        data.write("000001")
        data.seek(0)
        fileCount = data.readline()
    return fileCount, data, ttt_data_dir

def initializeDicts(ttt_data_dir):
    listOfDirs=[0,0,0]
    listOfDicts=[{},{},{}]
    listOfDirs[0] = os.path.join(ttt_data_dir,'win.json')
    listOfDirs[1]= os.path.join(ttt_data_dir,'loose.json')
    listOfDirs[2]= os.path.join(ttt_data_dir,'cat.json')
    exists= True
    for i in range(3):
        exists = os.path.isfile(listOfDirs[i]) and exists
    if exists:
        for j in range(3):
            with open(listOfDirs[j],'r') as jsonDict:
                listOfDicts[j] = json.load(jsonDict)
    else:
        for j in range(3):
            listOfDicts[j]['count']=1

    return listOfDicts,listOfDirs

def savingDicts(listOfDicts, listOfDirs):
    for i in range(3):
        with open(listOfDirs[i],'w') as json_file:
            json.dump(listOfDicts[i],json_file,indent=4)

    



def makeMenu(win,s):
    """
    stile1 = Rectangle(Point(196*scale,50*scale), Point(204*scale,350*scale))#stiles are what we call the verticle pieces of wood in a door
    stile2 = Rectangle(Point(296*scale,50*scale), Point(304*scale,350*scale))
    rail1 = Rectangle(Point(100*scale,146*scale), Point(400*scale,154*scale))#rails are what we call the horizontal pieces of wood in a door
    rail2 = Rectangle(Point(100*scale,246*scale), Point(400*scale,254*scale))
    """
    selectMessage = Text(Point(250*s,25*s),'Select Players Then Click Save.')
    easy = Text(Point(150*s,200*s),"EASY")
    medium = Text(Point(250*s,200*s),"MEDIUM")
    hard = Text(Point(350*s,200*s), "HARD")
    ai = Text(Point(150*s,300*s), "AI")
    human1 = Text(Point(250*s,300*s), "HUMAN")
    exitBut = Text(Point(350*s,300*s), "EXIT")
    playerX = Text(Point(150*s,75*s), "PLAYER X")
    playerO = Text(Point(350*s,75*s), "PLAYER O")
    save = Text(Point(250*s,100*s),"SAVE")
    menuList = [easy,medium,hard,ai,human1,exitBut,playerX,playerO,save,selectMessage]

    for e in menuList:
        e.setSize(scaleFontSize(13,s))
        e.setStyle('bold')
        
    menuList[7].setSize(scaleFontSize(10,s))
    menuList[6].setSize(scaleFontSize(10,s))
    menuList[9].setSize(scaleFontSize(15,s))
    menuList[7].setStyle('normal')
    menuList[6].setStyle('normal')
    menuList[9].setStyle('normal')
    menuList[6].setTextColor('blue')
    menuList[7].setTextColor('red')
    return menuList

def transClick(click):
    if click == (0,0):
        return 'playerX'
    elif click ==(0,1):
        return 'save'
    elif click ==(0,2):
        return 'playerO'
    elif click ==(1,0):
        return 'easy'
    elif click ==(1,1):
        return 'medium'
    elif click ==(1,2):
        return 'hard'
    elif click ==(2,0):
        return 'ai'
    elif click ==(2,1):
        return 'human'
    elif click ==(2,2):
        return 'exit'
    else:
        print("Malachi you coded something wrong")

def playerSelect(win,s, currentX = 'human', currentO = 'human'):
    playerX = currentX
    playerO = currentO
    click=''
    playerXText = Text(Point(150*s,100*s),playerX.upper())
    playerOText = Text(Point(350*s,100*s),playerO.upper())

    playerXText.draw(win)
    playerOText.draw(win)
    playerXText.setSize(scaleFontSize(13,s))
    playerOText.setSize(scaleFontSize(13,s))
    playAgain = 'left'
    start = 'left'
    
    while click != 'save' and click != 'exit':
        click = transClick(getMoveFromMouse(win))
        if click == 'playerX':
            playerXText.setText('SELECT')
            while click == 'playerX':
                click = transClick(getMoveFromMouse(win))
                
                if click == 'playerO' or click == 'save' or click == 'playerX':
                    playerXText.setText(playerX.upper())
                    break
                elif click == 'human':
                    playerX = 'human'
                    playerXText.setText(click.upper())
                elif click == 'exit':
                    break
                else:
                    playerX = click
                    playerXText.setText(click.upper())
        elif click == 'playerO':
            playerOText.setText('SELECT')
            while click == 'playerO':
                
                click = transClick(getMoveFromMouse(win))

                if click == 'playerX' or click == 'save' or click == 'playerO':
                    playerOText.setText(playerO.upper())
                    break
                elif click == 'human':
                    playerO = 'human'
                    playerOText.setText(click.upper())
                elif click == 'exit':
                    break
                else:
                    playerO = click
                    playerOText.setText(click.upper())
        if click == 'exit':
            playAgain = 'right'
            start = 'right'
        

    playerXText.undraw()   
    playerOText.undraw()          

            
    return playerX,playerO,playAgain,start


    

def main(sleepMax = .3, numOfRuns = 1):
    """takes an int argument for number of human players. takes 0 1 or 2. and a int for num of runs it will perform without asking if you want to play again. no arguments starts a regular two player game."""
    try:
        
        [fileCount,data,ttt_data_dir] = makeLogDirectory()
            
        scale = 1.25
        
        gameWin = makeBoardGraphics('Tic Tac Toe', scale, 'black')
        
        turnIndicator = Text(Point(25*scale,25*scale), '')#this was added after the game was functioning. Going forward i might make a text array for items that will be on the board
        #all the time that this would go in, until then it lives here.
        playAgain = 'yes'
        win = False
        Turn = 'X' #random.choice('X','O') #both the turn indicator and the value that gets written to the board
        turnIndicator.setSize(int(scaleFontSize(15, scale)))
        playerX = 'human'
        playerO = 'human'
        turnIndicator.draw(gameWin)
        start = 'left'
        while start == 'left':
            mList = makeMenu(gameWin,scale)
            drawButton(mList,gameWin)
            [playerX,playerO,playAgain,start]= playerSelect(gameWin,scale,playerX,playerO)
            undrawButton(mList)
            #pList = makeDualButton(gameWin, "Start","Exit","") #i used to have another menu but decided it was redunant
            #drawButton(pList,gameWin)
            #start = pressButton(gameWin)
            if start == 'right':
                data.close()#closing files when 
                #might be redundant but i confirmed that its ok for it to be redundant.
                gameWin.close()
                break
            #undrawButton(pList)
            

            while playAgain == 'left':
                #this creates/loads the ai weight data dictionairys
                [listOfDicts,listOfDirs] = initializeDicts(ttt_data_dir)

                #this chunk is for data loging
                file_path = os.path.join(ttt_data_dir, "gameData"+fileCount+".ttt") #this adds the filename onto the path
                log  = open(file_path, "w", encoding = "utf-8") 
                

                #this chunk is for initializing TTT object and drawing initial graph object
                gameBoard = TTT('         ')
                turnIndicator.setText(Turn)
                moveData = initTextArray(gameWin, 36) #array of player moves
                drawTextArray(moveData,gameWin)
              
                #variables initializing
                turnCounter = 0 #counts moves to stop the game at 9
                gameEnd = False
                win = False

                while win == False:
                    
                    
                    if Turn == 'X':
                        player = playerX
                    elif Turn == 'O':
                        player =playerO
                    """
                    elif numOfPlayers == 0:
                        player = "a"
                    else:
                        player ="p"
                    """
                    turnIndicator.setText(Turn)
                    turnCounter += 1
                    posCheck = False
                    
                    if player == 'human':
                        while posCheck == False:
                            pos = getMoveFromMouse(gameWin) #pos is a tuple with click position
                            row = pos[0]
                            col = pos[1]
                            posCheck = gameBoard.checkMove(row,col)
                    else:
                        sta = time.time()
                        [row,col]= gameBoard.aiMove(Turn,player,listOfDicts)
                        end = time.time()
                        processTime = end-sta
                        #print(processTime)
                        sleepTime = sleepMax - processTime
                        if sleepTime > 0:
                            sleep(sleepTime)
                        
                    gameBoard.addMove( row, col, Turn)
                    
                    updateTextArray(moveData, gameBoard)
                    win = gameBoard.winsFor(Turn)
                    if win == True:
                        gameEnd = True
                        log.write(gameBoard.data_string+':'+Turn)
                        break
                    elif win == False:
                        log.write(gameBoard.data_string+':n\n')
                    if turnCounter == 9:
                        gameEnd = True                     
                        break
                    Turn = turnSwitch(Turn)
                if gameEnd == True:
                    log.close()#closing log file after game is over
                    
                    if win == True:
                        winMess =makeGameMessage(gameWin, Turn + ' wins!')
                        winMess.draw(gameWin)
                        #sleep(.25)
                        Turn = turnSwitch(Turn)
                    elif turnCounter == 9:
                        winMess =makeGameMessage(gameWin, "Cat's Game")
                        winMess.draw(gameWin)
                        Turn = turnSwitch(Turn)
                        #sleep(.25)

                    #ai data analysis
                     
                    
                    #sta = time.time()
                    for orient in range(3):
                        LoLoBoards = sortThroughOne(file_path) 
                        listOfDicts = sortDataToDicts(listOfDicts, LoLoBoards)
                        [file_path,newCount] =rotateBoard(file_path)
                    #mid = time.time()
                    data.seek(0)
                    data.truncate()
                    data.write(newCount)
                    fileCount = newCount
                    savingDicts(listOfDicts, listOfDirs)
                    #end = time.time()
                    #print(mid-sta)
                    #print(end-mid)

                    bList = makeDualButton(gameWin, "Play","Menu","Play Again?")
                    turnIndicator.setText(' ')
                    drawButton(bList, gameWin)

                    #this is for auto runing bot games
                    if numOfRuns >1:
                        playAgain = 'left'
                        numOfRuns -=1
                    else:
                        playAgain = pressButton(gameWin)
                        
                    if playAgain == 'right':
                        log.close()#making sure log file is closed when game ends. 
                        winMess.undraw()
                        undrawButton(bList)
                        undrawTextArray(moveData,gameWin)
                        break
                    elif playAgain == 'left':
                        winMess.undraw()
                        undrawTextArray(moveData,gameWin)
                        undrawButton(bList)
                        clearTextArray(moveData, gameWin)
                        gameBoard.clearBoard()
                        updateTextArray(moveData,gameBoard)
    except GraphicsError:
        pass
    except Exception as e: #catching errors so that python doesnt crash when no longer able to close window
        print(f"An Error occured: {e}")#printing off erros so they arent lost
        traceback.print_exc()

        try: #this trys to close everything relevant, if its not open it doesnt through an error
            # i belive that because of the order if the first one doesnt exist none of the others will 
            # so it should be ok for them to be in the same try block
            
            gameWin.close()
            data.close()
            log.close()
            
        except NameError:
            pass
    #return gameWin
    
main()
"""
sta = time.time()
#main(0,1000)

end = time.time()
print(end-sta)

t1 = threading.Thread(target=main(0,100))
t2 = threading.Thread(target=main(0,100))

t1.start()
t2.start()
"""
"""
gameWin = makeBoardGraphics('Tic Tac Toe', 1.5, 'black')
mList = makeMenu(gameWin,1.5)
drawButton(mList, gameWin)
"""
"""
for i in range(20000):
    dicttest[chr(i)]=[]
    for j in range(9):
        dicttest[chr(i)]+=[j]

sta = time.time()
with open('data.json','w') as jsonDict:
    json.dump(dicttest,jsonDict,indent=4)
end = time.time()
print(end-sta)

sta = time.time()
with open('C:\\Users\\Malac\\Documents\\CS1\\tttData\\cat.json','r') as jsonDict:
    catDict = json.load(jsonDict)
end = time.time()
print(end-sta)
"""