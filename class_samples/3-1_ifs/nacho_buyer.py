print("How much do the nachos cost?")
nacho_price = int(raw_input())
print("How much monehy do you have in your pocket?")
cash = int(raw_input()) 

if nacho_price > cash: 
	print("Sorry! No nachos for you") 
if nacho_price <= cash:
	print( " Woot! nachos!") 
	print("Thanks for using nacho_buyer.py") 
if nacho_price ==cash:
	print("That sure was lucky!")
print( "Thanks for using nacho_buyer.py") 
