
def run_sim(character, sims=10000):
    max_hits = sims * character.attacks

    for ac in range(5, 26):
        total_damage = 0
        hits = 0
        turns_with_crit = 0
        for __ in range(sims):
            damage, hit_count, crit_flag  = character.attack(ac)
            total_damage += damage
            hits += hit_count
            turns_with_crit += 1 if crit_flag else 0

        print(
            "AC: {:2d}  ".format(ac) +\
            "DMG/HIT: {:5.1f}  ".format(total_damage/hits) +\
            "ATKHIT%: {:.2f}  ".format(hits/max_hits) +\
            "DMG/TURN: {:6.1f}  ".format(total_damage/sims) +\
            "CRIT%: {:.2f}".format(turns_with_crit/sims)
        )
