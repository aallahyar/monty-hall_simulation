# explanation: https://www.reddit.com/r/askmath/comments/14suc7s/can_someone_explain_to_me_the_monty_hall_problem/
# Try it with 1,000,000 doors and remember that the host knows which door has the prize behind it.
# You pick a door and the host removes 999,998 of the other doors. You are now given the option to stay or switch. 
# It's guaranteed that those 999,998 doors that were removed were all duds. The prize is guaranteed to be behind one of the 2 
# remaining doors. Do you stick with your original choice, knowing it was a 1 in a million shot that it was right or do you swap? Do you still think it's a 50/50 shot?
# You have a 999,999 in 1,000,000 chance of winning if you switch.

import numpy as np
import pandas as pd

trials = []
n_trial = 10000
rng = np.random.default_rng() # seed=42
doors = np.array([0, 0, 1])

for switch in [False, True]:
    for ti in range(n_trial):
        
        # place the car behind one of the doors
        rng.shuffle(doors)

        # choose 1st door
        choice1 = rng.choice([0, 1, 2])

        # monthy opens door
        goats = np.where((doors == 0))[0]
        can_open = goats[goats != choice1]
        opened = rng.choice(can_open)

        # do you want to switch?
        if switch:
            choice2 = [d for d in [0, 1, 2] if d != choice1 and d != opened][0]
        else:
            choice2 = choice1
        
        # result
        if doors[choice2] == 1:
            status = 'Won'
        else:
            status = 'Lost'
        
        trials.append({
            'door0': doors[0],
            'door1': doors[1],
            'door2': doors[2],
            'choice1': choice1,
            'opened': opened,
            'switch': switch,
            'choice2': choice2,
            'status': status,
        })
trials = pd.DataFrame(trials)

print(
    trials
    .value_counts(subset=['switch', 'status'], sort=False, dropna=False)
    .unstack()
)
