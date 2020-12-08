import pandas as pd
import random

def thewinneris(computer,human):
    if df.loc[computer,human] == 2:
        return 'human'
    if df.loc[computer,human] == 1:
        return 'computer'
    if df.loc[computer,human] == 'tie':
        return 'tie'

df = pd.read_excel(r'rock_paper_scissors_lizard_spock.xlsx', index_col=0)
liste = ["rock","paper","scissors","lizard","spock"]
pts_computer = 0
pts_human = 0

while pts_computer<5 and pts_human<5:
    x = random.choice(liste)
    y = input("rock, paper, scissors, lizard, spock? ")
    while y not in liste:
        print("Choose a valid option")
        y = input("rock, paper, scissors, lizard, spock? ")
    if thewinneris(x,y) == 'human':
        pts_human = pts_human+1
        print("Computer: ",str(x),", Human: ",str(y))
        print('The winner is human')
        print('Computer\'s score is ',str(pts_computer),'human\'s score is ',str(pts_human))
    if thewinneris(x,y) == 'computer':
        pts_computer = pts_computer+1
        print("Computer: ",str(x),", Human: ",str(y))
        print('The winner is computer')
        print('Computer\'s score is ',str(pts_computer),'human\'s score is ',str(pts_human))
    if thewinneris(x,y) == 'tie':
        print('It\'s a tie!')
        print('Computer\'s score is ',str(pts_computer),'human\'s score is ',str(pts_human))
if pts_computer == 5:
    print('The computer has 5 pts, they won')
if pts_human == 5:
    print('The human has 5 pts, you won')