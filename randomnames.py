import random
import sys
import numpy

# random names

vowels = ["a", "e", "i", "o", "u", "y"]
cons = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "x", "w", "z"]


def question():
    start = input("Generate more? Y/N ")
    if start[:1].upper() == "Y":
        generate()
    elif start[:1].upper() == "N":
        print("We're done here!")
    else:
        print("What?!")
        question()


def generate():
    
    # make a for loop

    s1 = random.choices([random.choice(vowels), random.choice(cons)], weights=[0.4, 0.6], k=1)
    s1 = s1[0]

    if s1 in cons:
        s2 = random.choice(vowels)
    else:
        s2 = random.choice(cons)

    end = random.choice(range(101))
    print(end)

    if end >= 10:
        if s2 in cons:
            s3 = random.choice(vowels)
        else:
            s3 = random.choice(cons)
        if end >= 20:
            if s3 in cons:
                s4 = random.choice(vowels)
            else:
                s4 = random.choice(cons)
            if end >= 30:
                if s4 in cons:
                    s5 = random.choice(vowels)
                else:
                    s5 = random.choice(cons)
                if end >= 45:
                    if s5 in cons:
                        s6 = random.choice(vowels)
                    else:
                        s6 = random.choice(cons)
                    if end >= 62:
                        if s6 in cons:
                            s7 = random.choice(vowels)
                        else:
                            s7 = random.choice(cons)
                        if end >= 75:
                            if s7 in cons:
                                s8 = random.choice(vowels)
                            else:
                                s8 = random.choice(cons)
                            if end >= 90:
                                if s8 in cons:
                                    s9 = random.choice(vowels)
                                else:
                                    s9 = random.choice(cons)
                                name = s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8 + s9
                            elif end < 90:
                                name = s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8
                        elif end < 75:
                            name = s1 + s2 + s3 + s4 + s5 + s6 + s7

                    elif end < 62:
                        name = s1 + s2 + s3 + s4 + s5 + s6
                elif end < 45:
                    name = s1 + s2 + s3 + s4 + s5
            elif end < 30:
                name = s1 + s2 + s3 + s4
        elif end < 20:
            name = s1 + s2 + s3
    elif end < 10:
        name = s1 + s2


    newname = name[:1].upper() + name[1:]
    print(newname)


    question()


generate()
