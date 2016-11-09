#1- prints “How old are you?”
#2- makes age a variable of what the user inputs, also makes it an integer 
#3- prints “How many inches tall are you?”
#4- makes heights the variable to what the user inputs, also makes it an integer 
#5 - if the GPA is greater than 3.0 and age is greater than 16 
#6 - it print " congrats, welcome to Columbia!" 
#7 - if the GPA is greater than or equal to 3.0 or gretaer than or equal to 16 
#8- if so then it prints "sorry, good luck at Harvard." 
print(" How old are you?")
age = int(raw_input())

print("What is your GPA?") 
GPA = float(raw_input()) 

if GPA > 3.0 and age > 16:
	print( "Congrats, welcome to Columbia!")
if GPA<= 3.0 or age <= 16:
	print("Sorry, good luck at Harvard.")  
