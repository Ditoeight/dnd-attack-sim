import random

from stuff.damage import Damage

class Attack():
    def __init__(self, damage_package, attacks=1, advantage=0, attack_mod=0,
                 crit_range=20, halfluck=False, elvenacc=False):
        self.damage_package = damage_package
        self.attacks = attacks
        self.advantage = advantage
        self.attack_mod = attack_mod
        self.crit_range = crit_range
        self.halfluck = halfluck
        self.elvenacc = elvenacc

    def attack(self, target_ac):
        total_damage = 0
        hits = 0
        crit_this_turn = False
        halfluck = 1 if self.halfluck else 0

        for attack in range(self.attacks):

            # Determine Attack roll
            d20s = []
            for __ in range(3 if self.elvenacc and self.advantage==1 else 2):
                poproll = random.randint(1,20)
                if poproll == 1 and halfluck > 0:
                    poproll = random.randint(1,20)
                d20s.append(poproll)

            if self.advantage == -1: # Disadvantage
                attempt = min(d20s)
            elif self.advantage == 0: # Regular
                attempt = d20s[0]
            elif self.advantage == 1: # Advantage
                attempt = max(d20s)

            # Deal the Damages
            if attempt >= self.crit_range:
                for item in self.damage_package:
                    total_damage += item.roll_damage(crit=True)
                hits += 1
                crit_this_turn = True
            elif attempt + self.attack_mod >= target_ac:
                for item in self.damage_package:
                    total_damage += item.roll_damage()
                hits += 1
            else:
                total_damage += 0

        return total_damage, hits, crit_this_turn
