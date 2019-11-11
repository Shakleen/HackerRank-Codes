def minion_game(string):
    vowels = {'A', 'E', 'I', 'O', 'U'}
    scoreStuart = scoreKevin = 0
    for pos, char in enumerate(string):
        if char in vowels: scoreKevin += len(string) - pos
        else: scoreStuart += len(string) - pos
    
    if scoreStuart > scoreKevin: print('Stuart ' + str(scoreStuart))
    elif scoreStuart < scoreKevin: print('Kevin ' + str(scoreKevin))
    else: print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)