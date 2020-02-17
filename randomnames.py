import random
import sys

#random names

vowels = ["a", "e", "i", "o", "u", "y"]
cons = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "x", "w", "z"]

#improve generate() to make it more random!

def generate():
	a = random.choice(vowels) + random.choice(cons) + random.choice(vowels)
	
	b = random.choice(vowels) + random.choice(cons) + random.choice(vowels) + random.choice(cons) + random.choice(vowels)
	
	c = random.choice(vowels) + random.choice(cons) + random.choice(vowels) + random.choice(vowels) + random.choice(cons) + random.choice(vowels)
	
	d = random.choice(vowels) + random.choice(cons) + random.choice(vowels) + random.choice(cons) + random.choice(vowels) + random.choice(cons)
	
	e = random.choice(vowels) + random.choice(cons) + random.choice(vowels) + random.choice(cons) + random.choice(vowels) + random.choice(cons) + random.choice(vowels) + random.choice(cons)
	
	e = random.choice(vowels) + random.choice(cons) + random.choice(vowels) + random.choice(cons) + random.choice(vowels) + random.choice(cons) + random.choice(vowels) + random.choice(cons) + random.choice(vowels)
	
	possibilities = [a, b, c, d, e]
	
	name = random.choice(possibilities)
	newname = name[:1].upper() + name[1:]
	print(newname)
	
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
	

generate()


