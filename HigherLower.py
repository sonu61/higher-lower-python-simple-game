import random
from gamedata import data
from art import logo,vs
import os
#1) pick random data from data nd compre who has more follower

A= random.choice(data)
random.shuffle(data)
B=random.choice(data) 
def is_equal():
    while A==B:
        b=random.choice(data)
game_on =True
print(logo)
#create compare function
score=0
#2)make a function to compare
while game_on:
    print(f"Compare A: {A['name']}, a {A['description']}, 'from',  {A['country']}")
    print(vs)
    print(f"Compare B: {B['name']}, a {B['description']}, 'from',  {B['country']}")
    compare_A_B = input("Who has more followers? Type 'A' or 'B': ")
    os.system('cls')


    if compare_A_B=='A' and A['follower_count']>B['follower_count']:
        score+=1
        print('you are right')
        
        
    elif compare_A_B=='A' and A['follower_count']<B['follower_count']:
        print('you are wrong')
        game_on=False
    elif compare_A_B=='B' and A['follower_count']<B['follower_count']:
        score+=1
        print('you are right')
    else:
        print('you are wrong')
        game_on=False
    print(f"your score is {score}")
    print(f"A: {A['follower_count']}, B {B['follower_count']}")
    A=B
    random.shuffle(data)
    B=random.choice(data)
    is_equal()



