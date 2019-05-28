#!/usr/bin/env python
# coding: utf-8

# # Python Milestone Project-1
# ## Re-Creating Tic-Tac-Toe 
# #### @author: [PseudoCodeNerd](http://github.com/PseudoCodeNerd) <br>
# _Madhav S. Sharma_

# In[1]:


from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(" " + "📍" + " " + "📍")
    print(board[7] + "📍" + board[8] + "📍" + board[9])
    print(" " + "📍" + " " + "📍")
    print("〰️〰️〰️")
    print(" " + "📍" + " " + "📍")
    print(board[4] + "📍" + board[5] + "📍" + board[6])
    print(" " + "📍" + " " + "📍")
    print("〰️〰️〰️")
    print(" " + "📍" + " " + "📍")
    print(board[1] + "📍" + board[2] + "📍" + board[3])
    print(" " + "📍" + " " + "📍")


# In[2]:


test_board=['','X','O','X','O','X','O','X','O','X']
display_board(test_board)


# In[3]:


blank_board=['1','2','3','4','5','6','7','8','9','10']
display_board(blank_board) #blank-board telling the user where exactly the position are on a TIC-TAC-TOE


# In[4]:


def player_input():
    sign = ''
    
    while not (sign == 'X' or sign == 'O'):
        sign = input('Player 1: Do you want to be X or O? ').upper()

    if sign == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


# In[5]:


player_input()


# In[6]:


def place_sign(board, sign, position):
    board[position] = sign


# In[7]:


place_sign(test_board, "X", 1)
display_board(test_board)


# In[8]:


def haveUwon(board, sign):
    return ((board[7] == sign and board[8] == sign and board[9] == sign) or # across the top
    (board[4] == sign and board[5] == sign and board[6] == sign) or # across the middle
    (board[1] == sign and board[2] == sign and board[3] == sign) or # across the bottom
    (board[7] == sign and board[4] == sign and board[1] == sign) or # down the middle
    (board[8] == sign and board[5] == sign and board[2] == sign) or # down the middle
    (board[9] == sign and board[6] == sign and board[3] == sign) or # down the right side
    (board[7] == sign and board[5] == sign and board[3] == sign) or # diagonal
    (board[9] == sign and board[5] == sign and board[1] == sign)) # diagonal


# In[9]:


haveUwon(test_board, "X")


# In[10]:


import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


# In[11]:


def emptyOrnot(board, position):
    return (board[position] == " ")


# In[12]:


emptyOrnot(test_board, 1)


# In[13]:


def isItFull(board):
    for i in range(1,10):
        if emptyOrnot(board, i):
            return False
    return True


# In[14]:


isItFull(test_board)


# In[15]:


def nextChoice(board):
    nextPos = 0
    
    while nextPos not in [1,2,3,4,5,6,7,8,9] or not emptyOrnot(board, nextPos):
        nextPos = int(input("Enter number from 1-9 to mark your sign there : "))
        
    return nextPos


# In[16]:


def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


# THE REAL SHIT BEGINS HERE!

# In[17]:


display_board(blank_board)


# In[19]:


print("🎉 Welcome to Madhav's TIC-TAC-TOE Program 🎉\n\n➡️So, you must be familiar how the game works...\n➡️Above displayed is the grid, in which you have to enter X'S and O's.\n\n😀Hope You Enjoy!")

while True:
    the_board= [" "]*10
    p1_marker, p2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
        
    while game_on:
        
        if turn == 'Player 1':
            
            display_board(the_board)
            position=nextChoice(the_board)
            place_sign(the_board, p1_marker, position)
            
            if haveUwon(the_board, p1_marker):
                display_board(the_board)
                print('🎊🎉 Congratulations! You have won the game! 🎊🎉')
                game_on = False
                
            else:
                
                if isItFull(the_board):
                    display_board(the_board)
                    print('🤞 The game is a draw! 🤞')
                    break
                else:
                    turn = 'Player 2'
        else:
                
            display_board(the_board)
            position=nextChoice(the_board)
            place_sign(the_board, p2_marker, position)
                
            if haveUwon(the_board, p2_marker):
                display_board(the_board)
                print('🎊🎉 Congratulations Player 2 👱🏽! You have won the game! 🎊🎉')
                game_on = False
                    
            else:
                
                if isItFull(the_board):
                    display_board(the_board)
                    print('🤞 The game is a draw! 🤞')
                    break
                else:
                    turn = 'Player 1'
                    
    if not replay():
        break
                


# In[ ]:





# In[ ]:




