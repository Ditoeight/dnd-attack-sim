from stuff.attack import Attack
from stuff.damage import Damage
from stuff.sim import run_sim


# Setup Martin's damages
hexblade_curse = Damage(flat=3)
hex = Damage(d6=1)
eldritch_blast = Damage(d10=1, flat=3)

# Package them together into a standard attack
standard_attack = [eldritch_blast, hex]
cursed_attack = [eldritch_blast, hex, hexblade_curse]

martin = Attack(standard_attack, attacks=1, attack_mod=5, crit_range=20)
run_sim(martin)

martin = Attack(cursed_attack, attacks=1, attack_mod=5, crit_range=19)
run_sim(martin)
