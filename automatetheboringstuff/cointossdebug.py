#Excercise 1 Chapter 10 
#Debugging Coin Toss
import random
import logging 
logging.basicConfig(level=logging.DEBUG,format ='%(asctime)s - %(levelname)s - %(message)s') 


guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    
toss = random.randint(0, 1) # 0 is tails, 1 is heads
toss = ('heads','tails')[toss]
logging.debug(toss)
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
       print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
