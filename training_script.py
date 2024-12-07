import os
from hw14pr4 import *
def makeLogDirectory():

    #path creation for log files
    current_dir = os.getcwd() #gets current working directory
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
def sortThroughOne(filePath):
    """takes a filepath and returns a list of list of strings. each internal 
    list contains moves in terms of self and enemy this allows all the data to work
    for both x and o. lists are in order of: winner = s, loser =s, firstplayer = s, secondplayer= s"""
    gameData = open(filePath, 'r', encoding= "utf-8")
    lineCount = -1
    line ='magnus_dingus'
    firstMove = ' '
    line = gameData.readline()
    
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
        listOfDics[2]=addPairsToDict(listOfPairs[i+2],listOfDics[2])
        if listOfPairs[i+2]!=[]:
            listOfDics[2]['count']+=1
        
    return listOfDics

def savingDicts(listOfDicts, listOfDirs):
    for i in range(3):
        with open(listOfDirs[i],'w') as json_file:
            json.dump(listOfDicts[i],json_file,indent=4)
c=0
#b =TTT('      O  ')
[fileCount,data,ttt_data_dir] = makeLogDirectory()
[listOfDicts,listOfDirs] =initializeDicts(ttt_data_dir)
#sumScores = b.scoresAvailableAi(listOfDicts,'X')
for i in range(40000,100000):
    if i%1000==0:
        c +=1
        #print(c)
    fileCount = str(i).zfill(6)
    file_path = os.path.join(ttt_data_dir, "gameData"+fileCount+".ttt")
    try:
        LoLoBoards = sortThroughOne(file_path)
        listOfDicts = sortDataToDicts(listOfDicts, LoLoBoards)
    except Exception as e: #catching errors so that python doesnt crash when no longer able to close window
        print('filenum is',i)
        print(f"An Error occured: {e}")#printing off erros so they arent lost
        traceback.print_exc()
savingDicts(listOfDicts, listOfDirs)
