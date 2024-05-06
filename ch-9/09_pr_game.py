'''game()function in a program lets the user play the game and returns
the score as an integer .user need to read file'hiscore.txt'
which is either blank or contains previous hi-score 
program to update the high_score whenever game()breaks the hi-score'''

def game():
    return 55
score=game()
with open("hiscore.txt") as f:
   hiscorestr=f.read()
if hiscorestr=='':
    with open("hiscore.txt",'w') as f:
     f.write(str(score))
elif int(hiscorestr)<score : 
    with open("hiscore.txt",'w') as f:
     f.write(str(score))