from random import randint

class Die():
    
    def __init__(self, num_roll, sides = 6):
        
        self.num_roll = num_roll
        self.sides = sides

    def roll_die(self):

        for num in range(self.num_roll):
            num = randint(1, self.sides)
            print(num)


roll_1 = Die(10)
roll_1.roll_die()

print("\n")

roll_2 = Die(10, 10)
roll_2.roll_die()

print("\n")

roll_3 = Die(10, 20)
roll_3.roll_die()