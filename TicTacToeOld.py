#
# hw9pr3.py
#
# Name:Malachi
#

# TTT-class
# game-play AND visualization!
from graphics import *
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
        
#Answers. 
#1. variable = TTT('         ')
#2. One is useful for the raw data and the other is read to be interated through by row and column
#3. I this the LOL is more useful as each indivual x/o can be called and manipulated indiviually.
#4. __repr__ is useful for use to have to make sure our code is working long before we have a functioning graphic. 


def makeBoardGraphics(title, scale, color):
    TTTBoard = GraphWin(title, 500*scale, 425*scale)
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
    fontSize = size*scale
    if fontSize >36:
        fontSize = 36
    if fontSize < 5:
        fontSize = 5
    return fontSize
        
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

def makeDualButton(tttWin):
    scale = (tttWin.getWidth())/500
    box = Rectangle(Point(150*scale,383*scale),Point(350*scale,417*scale))
    yText = Text(Point(200*scale,400*scale),"Yes")
    nText = Text(Point(300*scale,400*scale),"No")
    playText =Text(Point(250*scale,365*scale),"Play Again?")
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
                answer = "yes"
            elif clickPoint.getX() > 250*scale and clickPoint.getX() < 350*scale:
                answer = "no"
    return answer
def turnSwitch(player):
    if player == "X":
        player = "O"
    elif player == "O":
        player = "X"
    return player
    
    

def main():
    scale = 1.0111
    gameWin = makeBoardGraphics('Tic Tac Toe', scale, 'black')
    gameWin.setBackground(color_rgb(121,213,219))
    turnIndicator = Text(Point(25*scale,25*scale), '')
    playAgain = 'yes'
    win = False
    Turn = 'X'
    turnIndicator.draw(gameWin)
    turnIndicator.setSize(int(scaleFontSize(15, scale)))
    while playAgain == 'yes':
        
        gameBoard = TTT('         ')
        turnIndicator.setText(Turn)
        moveData = initTextArray(gameWin, 36)
        drawTextArray(moveData,gameWin)
        
        if win == True:
            Turn = turnSwitch(Turn)
        
        turnCounter = 0 
        gameEnd = False
        win = False
        while win == False:
            turnIndicator.setText(Turn)
            turnCounter += 1
            posCheck = False
            while posCheck == False:
                pos = getMoveFromMouse(gameWin)
                row = pos[0]
                col = pos[1]
                posCheck = gameBoard.checkMove(row,col)
            gameBoard.addMove( row, col, Turn)
            moveData[row][col].setText(Turn)
            updateTextArray(moveData, gameBoard)
            win = gameBoard.winsFor(Turn)
            if win == True:
                gameEnd = True
                break

            
            
            if turnCounter == 9:
                gameEnd = True
                break
            Turn = turnSwitch(Turn)
        if gameEnd == True:
            
            if win == True:
                winMess =makeGameMessage(gameWin, Turn + ' wins!')
                winMess.draw(gameWin)
            elif turnCounter == 9:
                winMess =makeGameMessage(gameWin, "Cat's Game")
                winMess.draw(gameWin)
            bList = makeDualButton(gameWin)
            turnIndicator.setText(' ')
            drawButton(bList, gameWin)
            playAgain = pressButton(gameWin)
            
            if playAgain == 'no':
                
                
                gameWin.close()

        if playAgain == 'yes':
            winMess.undraw()
            undrawButton(bList)
            clearTextArray(moveData, gameWin)
            gameBoard.clearBoard()
            updateTextArray(moveData,gameBoard)
        
main()
