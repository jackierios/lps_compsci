# put this line at the start of your program
# to make the functions of this package available
import random
# creates a random number between 3 and 567 - edit as necessary
myNum = random.randint(1, 1000)
wrong = 0
print("I'm thinking of a number between 1 and 1000. Enter a guess!")  
while wrong < myNum: 
	guess= int(raw_input())
	if guess < myNum: 	
		print("Nope. Sorry too low. Guess again")
	if guess > myNum:
		print("Nope. Sorry too high. GUess again")
	if guess == myNum: 
		print("YEAH! YOU WON!")




