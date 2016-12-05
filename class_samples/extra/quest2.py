# put this line at the start of your program
# to make the functions of this package available
import random
# creates a random number between 3 and 567 - edit as necessary
myNum = random.randint(1, 1000)

print("I'm thinking of a number between 1 and 1000. Enter a guess!") 
guess= int(raw_input())
if guess < 2: 	
	print("Nope. Sorry too low")
if guess >= 3:
	print("Nope. Sorry too high")
if guess == 2: 
	print("YEAH! YOU WON!")




