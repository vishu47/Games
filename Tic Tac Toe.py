# print("WELCOME TO THE GAME!!!")
# print(" ")
#
import random
def boardform(board):
    print('   |   | ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   | ')
    print('-----------')
    print('   |   | ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   | ')
    print('-----------')
    print('   |   | ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   | ')

board=['#','X','O','X','O','X','O','X','O','X']
# boardform(testboard)
# print('\n'*100)                   #for clear the output
# boardform(testboard)
####################
#player input
def player_input():
    marker=' '
    while marker != 'X' and marker != 'O':
        marker=input("player1: choose X or O: ")
        player1=marker;
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return(player1,player2)
# player1,player2=player_input()
# print("player1 choose: ",player1)
# print("player2 choose: ",player2)
################## print("player1={} and player2={}".format(player1,player2))

#select the position for input
def assign_input(board,marker, position):
    board[position]=marker

# boardform(board)
# assign_input(board,'$',5)

#winning condition
#horizontal
def win_conditions(board,marker):

    return ((board[7] == board[8] == board[9] == marker) or
            (board[4] == board[5] == board[6] == marker) or
            (board[1] == board[2] == board[3] == marker) or
            #Vertical
            (board[3] == board[6] == board[9] == marker) or
            (board[2] == board[5] == board[8] == marker) or
            (board[1] == board[4] == board[7] == marker) or
            #diagonal
            (board[1] == board[5] == board[9] == marker) or
            (board[3] == board[5] == board[7] == marker))
boardform(board)
print(win_conditions(board,'X'))

#choose the player rendomly
def chooseplayer():
    player = random.randint(1,2)
    if player == 1:
        return 'player1'
    else:
        return 'player2'

#check for the space at that place
def space(board,position):
    return board[position] == ' '

#check for space in whole board
def full_board_check(board):
    for i in range(1,10):
        if space(board,i):
            return False
    return True

#choose the position on the board and check the position on the board
def player_choice(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space(board,position):
        position = int(input("Choose the position between(1-9) on board: "))
    return position

#game over check yes or no
def play_again():
    choice = input("Want to play again yes or no? : ")
    return choice == 'yes'

def replay():
    choice = input('play again? yes or no')
    return choice == 'yes'



#GAMEPLAY
#Print("Welcome To the TIC TAC TOE Game")
while True:
    #play the game
    #setup the game board,who's 1st choose marker X,O
    the_board=[' ']*10;
    player1, player2 = player_input()
    print(player1 + ' marker is for player1')
    print(player2 + ' marker is for player2')
    turn=chooseplayer()
    print(turn + ' will go first')
    play_game = input('ready to play? [y/n]:' )
    if play_game == 'y':
        game_on=True
    else:
        game_on=False
#game play
    while game_on:
        if turn == 'player1':

#player1 turn
            #show the board
            boardform(the_board)
            #choose a position
            position = player_choice(the_board)
            #place the marker on the position
            assign_input(boardform,player1, position)
            #check the winning
            if win_conditions(the_board,player1):
                boardform(the_board)
                print('player1 has won!!!')
                game_on = False
            else:
                if  full_board_check(boardform):
                    boardform(the_board)
                    print('GAME TIE!!!')
                    game_on=False
                else:
                    turn = 'player2'

        #check for tie
        #no tie no win then nxt player turn
        else:
            # player2 turn
            # show the board
            boardform(the_board)
            # choose a position
            position = player_choice(the_board)
            # place the marker on the position
            assign_input(board, player2, position)
            # check the winning
            if win_conditions(the_board,player2):
                boardform(the_board)
                print('player2 has won!!!')
                game_on = False
            else:
                if full_board_check(boardform):
                    boardform(the_board)
                    print('GAME TIE!!!')
                    game_on = False
                else:
                    turn = 'player2'
    if not replay():
        break
    #player2 turn


#
#
