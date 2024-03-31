# gun > water
# snack > water
# gun < snack

import random

# check for win
def check(comp, user):
    if (comp == user):
        return 0
    elif (comp == 1 and user == 2) or (comp == 2 and user == 3) or (comp == 3 and user == 1):
        return -1
    else:
        return 1


def score_card(i, j):
	if(i > j):
		print(f"You Won by {i}")
	elif(j > i):
		print(f"You lose by {j}")
	else:
		print(f"It's draw by {i} and {j}")


i = 0
j = 0

n = 0
while(n<5):
	list = ["gun","water","snack"]
	print("\t\tWelcome to the game_snack_water_gun\t\t\n")
	print("1 for gun\t2 for water\t3 for snack\n")
	user = int(input("Enter the number between 1 to 3:\t"))
	while(user>0):
		if(user==1 or user==2 or user==3):
			print(f"The user has selected {list[user-1]}")
			break  
		else:
			print("Invalid Input!")
			break

	comp = random.randint(1,3)
	print("The computer has selected {} ".format(list[comp-1]))
  
	score = check(comp, user)

	if(score==0):
		i=j=0
	elif (score==-1):
		j+=1
	else: 
		i+=1
	
	score_card(i, j)
	n = n + 1


  
  




  