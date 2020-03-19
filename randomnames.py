import random
import sys

#random names

vowels = ["a", "e", "i", "o", "u", "y"]
cons = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "x", "w", "z"]

#improve generate() to make it more random!

def generate():
	
	# 5 possibilities of different lenghts
	# could be done with a for loop that would ensure more random possibilities by using if last letter = vowel then cons
	# and vice versa and would also be a more compact function, less hardcoded
	
	a = random.choice(vowels) + random.choice(cons) + random.choice(vowels)
	
	b = random.choice(vowels) + random.choice(cons) + random.choice(vowels) + random.choice(cons) + random.choice(vowels)
	
	c = random.choice(vowels) + random.choice(cons) + random.choice(vowels) + random.choice(vowels) + random.choice(cons) + random.choice(vowels)
	
	d = random.choice(vowels) + random.choice(cons) + random.choice(vowels) + random.choice(cons) + random.choice(vowels) + random.choice(cons)
	
	e = random.choice(vowels) + random.choice(cons) + random.choice(vowels) + random.choice(cons) + random.choice(vowels) + random.choice(cons) + random.choice(vowels) + random.choice(cons)
	
	e = random.choice(vowels) + random.choice(cons) + random.choice(vowels) + random.choice(cons) + random.choice(vowels) + random.choice(cons) + random.choice(vowels) + random.choice(cons) + random.choice(vowels)
	
	# list of all the possibilities so it can randomly choose one
	
	possibilities = [a, b, c, d, e]
	
	# passing the name created to a var and then making the first letter uppercase
	
	name = random.choice(possibilities)
	newname = name[:1].upper() + name[1:]
	print(newname)
	
	# continue or stop
	
	start =  input("Generate more? Y/N ")
	if start[:1].upper() == "Y":
		start = True
	else:
		start = False
	
	if start == True:
		generate()
	else:
		print("We're done here!")
		exit()

# program start

generate()


