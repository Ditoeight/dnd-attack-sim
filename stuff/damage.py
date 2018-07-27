import random

class Damage():
    def __init__(self, d4=0, d6=0, d8=0, d10=0, d12=0, flat=0, reroll_on=0):
        self.d4 = d4
        self.d6 = d6
        self.d8 = d8
        self.d10 = d10
        self.d12 = d12
        self.flat = flat
        self.reroll_on = reroll_on

        self.roll_list = self.build_roll_list()

    def roll_damage(self, crit=False):
        loops = 2 if crit else 1
        damage = self.flat

        for loop in range(loops):
            for die in self.roll_list:
                roll = random.randint(1, die)
                if roll <= self.reroll_on:
                    roll = random.randint(1, die)
                damage += roll

        return damage

    def build_roll_list(self):
        roll_list = [4 for count in range(self.d4)]
        roll_list += [6 for count in range(self.d6)]
        roll_list += [8 for count in range(self.d8)]
        roll_list += [10 for count in range(self.d10)]
        roll_list += [12 for count in range(self.d12)]
        return roll_list

    def add_chain(self, chain_target):
        self.chain = chain_target
