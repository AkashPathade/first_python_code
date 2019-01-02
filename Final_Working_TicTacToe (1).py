
# coding: utf-8

# In[31]:


def display_board(board):
    #this fn will take a 2D list as argument and print the board
    print(board[7],' | ',board[8],' | ',board[9])
    print('--------------')
    print(board[4],' | ',board[5],' | ',board[6])
    print('--------------')
    print(board[1],' | ',board[2],' | ',board[3])


# In[32]:


def player_input():
    #this fn will take user input and assign the marker
    while(True):
        print('Please select your marker:')
        print('Press 1 for x','press 2 for o',sep='\n')
        inp=eval(input())
        if inp==1:
            return('x','o')
            break
        elif inp==2:
            return('o','x')
            break
        else:
            print('Please enter either 1 or 2')


# In[33]:


def place_marker(board,marker,position):
    board[position]=marker


# In[34]:


def win_check(board,mark):
    #checking for horizontal possiblities
    if (board[7]==board[8]==board[9]==mark) or (board[4]==board[5]==board[6]==mark) or (board[1]==board[2]==board[3]==mark):
        return True
        
    #checking for vertical possiblities
    elif (board[7]==board[4]==board[1]==mark) or (board[8]==board[5]==board[2]==mark) or (board[9]==board[6]==board[3]==mark):
        return True
        
    #checking for diagonal possiblities
    elif (board[1]==board[5]==board[9]==mark) or (board[7]==board[5]==board[3]==mark):
        return True
    else:
        return False
    


# In[35]:


import random
def choose_first():
    '''
    this fn selects first player randomly
    '''
    x=random.randint(1,2)
    if x==1:
        return 'player1'
    else:
        return 'player2'


# In[36]:


def space_check(board,position):
    '''
    this fn checks if the position is free or not
    '''
    if board[position]==' ':
        return True
    else:
        return False


# In[37]:


def full_board_check(board):
    '''
    this fn returns true if board is full.
    '''
    for position in range(1,10):
        if board[position]==' ':
            return False
    return True


# In[38]:


def player_choice(board,player):
    #loop chances
    while True:
        print(player,' Enter your next position: ')
        position=eval(input())
        if space_check(board,position):
            return position
        else:
            print('position is already occupied')


# In[39]:


def replay():
    ans=input('Do you want to play again? (Y/N)')
    if ans=='y' or ans=='Y':
        return True
    else:
        return False


# In[ ]:


print('Welcome to tic tac toe!\n')
while True:
    # initial setting
    the_board=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    player1_marker,player2_marker=player_input()
    turn=choose_first()
    print(turn,' will go first')
    game_on=True
    
    while game_on:
        if turn=='player1':
            #player1's turn
            display_board(the_board)
            position=player_choice(the_board,'player1')
            place_marker(the_board,player1_marker,position)
            
            #after placing marker check for win or draw conditions
            if win_check(the_board,player1_marker):     #win condition checking
                display_board(the_board)
                print('Congratulations! player1 won the game!')
                game_on=False
            else:                                       #Draw condition checking
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is draw!')
                    break
                else:
                    turn='player2'
        
        else:
            #player2's turn
            display_board(the_board)
            position=player_choice(the_board,'player2')
            place_marker(the_board,player2_marker,position)
            
            #after placing marker check for win or draw conditions
            if win_check(the_board,player2_marker):     #win condition checking
                display_board(the_board)
                print('Congratulations! player2 won the game!')
                game_on=False
            else:                                       #Draw condition checking
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is draw!')
                    break
                else:
                    turn='player1'
        
    
    
    if not replay():
        break

