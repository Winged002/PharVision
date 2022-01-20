import random
import csv


winningVariants = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [7, 5, 3]]


player = 'O'
bot = 'X'
bot2 = 'O'

def printBoard(board,_writer=' '):
    print('---------------')
    print(' | ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' | ')
    print('---------------')
    print(' | ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' | ')
    print('---------------')
    print(' | ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' | ')
    print('---------------')
    print("\n")
    if _writer != ' ':
        _writer.writerow([board[1],board[2],board[3],board[4],board[5],board[6],board[7],board[8],board[9],])


def spaceIsFree(board, position):
    if board[position] == ' ':
        return True
    else:
        return False


def insertLetter(board, letter, position, _steps, _writer_1=' ',_writer_2=' ', _int=99, _bool=False):
    if spaceIsFree(board, position):
        board[position] = letter
        printBoard(board,_writer_2)
        _steps += 1
        if (checkDraw(board)):
            print("Draw!")
            # exit()
        if checkForWin(board) in winningVariants:
            if letter == 'X':
                print("Bot wins!")
                if _writer_1 != ' ':
                    _writer_1.writerow([_int,_bool,checkForWin(board),_steps])
                # exit()
            else:
                print("Player wins!")
                if _writer_1 != ' ':
                    _writer_1.writerow([_int,_bool,checkForWin(board),_steps])
                # exit()

        return _steps


    else:
        print("Can't insert there!")
        position = int(input("Please enter new position:  "))
        _steps = insertLetter(board, letter, position, _steps)
        return _steps


def checkForWin(board):
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return [1, 2, 3]
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return [4, 5, 6]
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return [7, 8, 9]
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return [1, 4, 7]
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return [2, 5, 8]
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return [3, 6, 9]
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return [1, 5, 9]
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return [7, 5, 3]
    else:
        return False


def checkWhichMarkWon(board, mark):
    if board[1] == board[2] and board[1] == board[3] and board[1] == mark:
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False


def checkDraw(board):
    for key in board.keys():
        if (board[key] == ' '):
            return False
    return True


def playerMove(board, _steps, _writer=' '):
    position = int(input("Enter the position for 'O':  "))
    _steps = insertLetter(board, player, position, _steps, _writer)
    return _steps


def compMove(board, _int, _bool, comp1_steps,_writer_1=' ',_writer_2=' '):
    bestScore = -800
    bestMove = 0
    for key in board.keys():
        if (board[key] == ' '):
            board[key] = bot
            score = minimax(board, _int, _bool)
            board[key] = ' '
            if (score > bestScore):
                bestScore = score
                bestMove = key
    try:
        comp1_steps = insertLetter(board, bot, bestMove, comp1_steps,_writer_1,_writer_2, _int, _bool)
        return comp1_steps
    except:
        return


def compMove2(board, _int, _bool, comp2_steps,_writer_1=' ',_writer_2=' '):
    bestScore = -800
    bestMove = 0
    for key in board.keys():
        if (board[key] == ' '):
            board[key] = bot2
            score = minimax(board, _int, _bool)
            board[key] = ' '
            if (score > bestScore):
                bestScore = score
                bestMove = key

    comp2_steps = insertLetter(board, bot2, bestMove, comp2_steps,_writer_1,_writer_2, _int, _bool)
    return comp2_steps


def minimax(board, depth, isMaximizing):
    if (checkWhichMarkWon(board, bot)):
        return 1
    elif (checkWhichMarkWon(board,player)):
        return -1
    elif (checkDraw(board)):
        return 0

    if (isMaximizing):
        bestScore = -800
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = bot
                score = minimax(board, depth + 1, False)
                board[key] = ' '
                if (score > bestScore):
                    bestScore = score
        return bestScore

    else:
        bestScore = 800
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = player
                score = minimax(board, depth + 1, True)
                board[key] = ' '
                if (score < bestScore):
                    bestScore = score
        return bestScore


def run(player_first):
    comp2_steps = 0
    comp1_steps = 0
    player_steps = 0
    board = {1: ' ', 2: ' ', 3: ' ',
             4: ' ', 5: ' ', 6: ' ',
             7: ' ', 8: ' ', 9: ' '}

    printBoard(board)
    # print("Computer goes first! Good luck.")
    print("Positions are as follow:")
    print("1, 2, 3 ")
    print("4, 5, 6 ")
    print("7, 8, 9 ")
    print("\n")

    global firstComputerMove
    firstComputerMove = False

    if player_first == 'player':
        print("Player goes first!")
        while not checkForWin(board):
            player_steps = playerMove(board,player_steps)
            comp1_steps = compMove(board, 0, False, comp1_steps)
    else:
        print("Bot goes first!")
        while not checkForWin(board):
            comp1_steps = compMove(board, 0, False, comp1_steps)
            player_steps = playerMove(board, player_steps)


def runAnalysis(_times=50):
    _data_id = random.randint(0,999999)
    openCSV = open('ai_data_' + str(_data_id) + '.csv', 'w', newline='', encoding='utf-8')
    csvWriter = csv.writer(openCSV)
    csvWriter.writerow(['int_state', 'bool_state', 'winning_variables', 'step_count'])

    openCSV_ = open('ai_data_' + str(_data_id) + '_turns.csv', 'w', newline='', encoding='utf-8')
    csvWriter_ = csv.writer(openCSV_)
    csvWriter_.writerow(['steps'])
    for y in range(_times):
        comp2_steps = 0
        comp1_steps = 0
        ai_varialbes = [True, False]

        board = {1: ' ', 2: ' ', 3: ' ',
                 4: ' ', 5: ' ', 6: ' ',
                 7: ' ', 8: ' ', 9: ' '}

        printBoard(board)
        # print("Computer goes first! Good luck.")
        print("Positions are as follow:")
        print("1, 2, 3 ")
        print("4, 5, 6 ")
        print("7, 8, 9 ")
        print("\n")

        global firstComputerMove
        firstComputerMove = False

        ai1_random_int_depth = random.randint(0, 8)
        ai1_random_int_variables = ai_varialbes[random.randint(0, 1)]
        ai2_random_int_depth = random.randint(0, 8)
        ai2_random_int_variables = ai_varialbes[random.randint(0, 1)]
        while not checkForWin(board):
            try:
                comp2_steps = compMove2(board, ai2_random_int_depth, ai2_random_int_variables, comp2_steps, csvWriter, csvWriter_)
                comp1_steps = compMove(board, ai1_random_int_depth, ai1_random_int_variables, comp1_steps, csvWriter, csvWriter_)
            except:
                continue
    return _data_id

def printAnalysis(ids):
    # loadCSV_turns = open('ai_data_' + str(_id_) + '_turns.csv', 'r')
    for _id_ in ids:
        loadCSV_data = open('ai_data_' + str(_id_) + '.csv','r')
        # turns_reader = csv.reader(loadCSV_turns)
        data_reader = csv.reader(loadCSV_data)
        next(data_reader)
        _winningVariants = {}
        _stepCount = {}
        for data_row in data_reader:
            if data_row[2] not in _winningVariants:
                _winningVariants.update({data_row[2]:0})
                _stepCount.update({data_row[2]:int(data_row[3])})
            else:
                i = _winningVariants.get(data_row[2])
                _winningVariants.update({data_row[2]:i+1})
        print('\n')
        print('Times winning combination : ')
        print({k: v for k, v in sorted(_winningVariants.items(), key=lambda item: item[1])})
        print('\n')
        print('Step count : ')
        print({k: v for k, v in sorted(_stepCount.items(), key=lambda item: item[1])})
        print('\n')



# to run an analysis, you need to call this function and insert the number of games the data to be collected from
# the default value is set to 50 games

_trialRun = runAnalysis(50)


# in order to print out the analysis for the saved data, you can insert the id's of the data files as a list into the
# function and it will process the numbers and give the most efficient combination

printAnalysis([_trialRun])



# to run the game, the run function needs to be called and state who goes first, the bot or the player

isPlayerFirst = input('Who should go first?     (player/bot)')
run(isPlayerFirst)