print("welcome to Jayquelin's Quest") 
print("Enter the name of your character:") 
name = str(raw_input())

print("enter your charcaters strength (1-10):")
strength = int(raw_input())
	`
print("enter your charcaters health (1-10):")
health = int(raw_input())

print("enter your characters luck (1-10):")
luck= int(raw_input())

total = (strength + health + luck) 

if total > 15: 
	print("sorry looks like you gave your character too many points")

if total <= 15 
	print(name + "'s  strength:" + str(strength) + ", health:" + str(health) + "and luck:" + str(luck))   
