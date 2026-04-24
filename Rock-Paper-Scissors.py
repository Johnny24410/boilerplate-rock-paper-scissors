import random

def player1(choice_made_P, choice_made_D):
    if choice_made_P == 'R' and choice_made_D == 'S':
        winner = 'Player1 wins'
              
    elif choice_made_P == 'P' and choice_made_D == 'R':
        winner = 'Player1 wins'
            
    elif choice_made_P == 'S' and choice_made_D == 'P':
        winner = 'Player1 wins'
            
    elif choice_made_P == choice_made_D:
        winner = 'Tie'

    else:
        winner = c_p, 'wins'
    return winner

def player2(choice_made_D, choice_made_P):
    if choice_made_D == 'R' and choice_made_P == 'S':
        winner = c_p, 'wins'
            
    elif choice_made_D == 'P' and choice_made_P == 'R':
        winner = c_p, 'wins'
            
    elif choice_made_D == 'S' and choice_made_P == 'P':
        winner = c_p, 'wins'
           
    elif choice_made_P == choice_made_D:
        winner = 'Tie'

    else:
        winner = 'Player1 wins'
    return winner

game_history = []
choice_history_P = []
choice_history_D = []

while True:
    c_p = input('Choose player:')

    print('')

    if c_p == 'Henry':
        c_p = 'Henry'

    elif c_p == 'Emile':
        c_p = 'Emile'

    elif c_p == 'Sonskyn':
        c_p = 'Sonskyn'

    elif c_p == 'Nandos':
        c_p = 'Nandos'

    elif c_p == 'Kayla':
        c_p = 'Kayla'

    elif c_p != 'Henry' or 'Emile' or 'Sonskyn' or 'Nandos' or 'Kayla':
        print('Should be Henry or Emile or Sonskyn or Nandos or Kayla')
        continue

    n_of_g_p = input('How many games to play:')
    try:
        n_of_g_p1 = int(n_of_g_p)
    except:
        print('Should be a number')
        continue

    if n_of_g_p1 > 1000:
        print('Can not play more than a 1000 games')
        exit()
    
    #print('')
    
    total_iterations = 0

    while total_iterations < n_of_g_p1:
        choices_P = ('R', 'P', 'S')
        choice_made_P = random.choice(choices_P)
        #print('Player1:',choice_made_P)


        choices_D = ('R', 'P', 'S')
        choice_made_D = random.choice(choices_D)
        #print('Player:',c_p,':',choice_made_D)

        #print('')

        winner = player1(choice_made_P, choice_made_D)
        #print('Result:', winner)

        #print('')

        game_history.append(winner)

        choice_history_P.append(choice_made_P)

        choice_history_D.append(choice_made_D)

        d_of_chp = dict()
        for i in choice_history_P:
            d_of_chp[i] = d_of_chp.get(i, 0) + 1

        d_of_chd = dict()
        for i in choice_history_D:
            d_of_chd[i] = d_of_chd.get(i, 0) + 1

        d_of_p = dict()
        for c1 in game_history:
            d_of_p[c1] = d_of_p.get(c1, 0) + 1

        total_iterations += 1 

    if total_iterations >= n_of_g_p1:
        break     

print('')

print('Game History:', d_of_p)

print('')

print(d_of_chp)

print('')

print(d_of_chd)

print('')
