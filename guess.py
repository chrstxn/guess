import random

def play(n):
	# Chooses an integer between 1 and n
	num = random.randint(1, n)
	# Asks for guess
	guess = input("Make a guess.")
	while guess != num:
		if guess < num:
			print("Higher!")
			guess = input("Make another guess.")
		else:
			print("Lower!")
			guess = input("Make another guess.")
	if guess == num:
		print("You got it!")
		again = raw_input("Would you like to play again?")
		if again == "YES":
			play(n)
		else:
			"Okay then."

range = input("I'll pick a number between 1 and... ?")
play(int(range))