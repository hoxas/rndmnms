import random

# random names


class RandomNameGenerator:
    def __init__(self):
        self.vowels = ["a", "e", "i", "o", "u", "y"]
        self.cons = ["b", "c", "d", "f", "g", "h", "j", "k", "l",
                     "m", "n", "p", "q", "r", "s", "t", "v", "x", "w", "z"]
        self.vowel_weight = 0.4
        self.cons_weight = 0.6
        self.name = ""
        self.name_length = None

    def ask(self):
        start = input("Generate more? Y/N \n")
        if start[:1].upper() == "Y":
            self.run()
        elif start[:1].upper() == "N" or start[:1].upper() == "E":
            print("We're done here!")
        else:
            print("What?!")
            self.ask()

    def name_to_string(self):
        _name = ""
        letters = (letter for letter in self.name)
        for letter in letters:
            _name += letter
        self.name = _name

    def capitalize(self):
        self.name = self.name.capitalize()

    def generate_name_length(self):
        self.name_length = random.randint(2, 12)

    def generate_letter(self):
        if not self.name:
            self.name = random.choices([random.choice(self.vowels), random.choice(
                self.cons)], weights=[self.vowel_weight, self.cons_weight], k=1)
        elif self.name[-1] in self.vowels:
            self.name += random.choice(self.cons)
        else:
            self.name += random.choice(self.vowels)

    def run(self):
        self.name = ""
        self.generate_name_length()
        for _ in range(0, self.name_length):
            self.generate_letter()
        self.name_to_string()
        self.capitalize()
        print(self.name)
        self.ask()


if __name__ == "__main__":
    RandomNameGenerator().run()
