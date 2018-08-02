from random import randint as rand
BLANK = "_"
SUCCESS = "o"
FAILURE = "x"
ADVANTAGE = "^"
THREAT = "v"
TRIUMPH = "O"
DESPAIR = "X"
BOOST = [BLANK,
         BLANK,
         SUCCESS,
         SUCCESS+ADVANTAGE,
         ADVANTAGE+ADVANTAGE,
         ADVANTAGE]
SETBACK = [BLANK,
           BLANK,
           FAILURE,
           FAILURE,
           THREAT,
           THREAT]
ABILITY = [BLANK,
           SUCCESS,
           SUCCESS,
           SUCCESS+SUCCESS,
           ADVANTAGE,
           ADVANTAGE,
           SUCCESS+ADVANTAGE,
           ADVANTAGE+ADVANTAGE]
DIFFICULTY = [BLANK,
              FAILURE,
              FAILURE+FAILURE,
              THREAT,
              THREAT,
              THREAT,
              THREAT+THREAT,
              FAILURE+THREAT]
PROFICIENCY = [BLANK,
               SUCCESS,
               SUCCESS,
               SUCCESS+SUCCESS,
               SUCCESS+SUCCESS,
               ADVANTAGE,
               SUCCESS+ADVANTAGE,
               SUCCESS+ADVANTAGE,
               SUCCESS+ADVANTAGE,
               ADVANTAGE+ADVANTAGE,
               ADVANTAGE+ADVANTAGE,
               TRIUMPH]
CHALLENGE = [BLANK,
             FAILURE,
             FAILURE,
             FAILURE+FAILURE,
             FAILURE+FAILURE,
             THREAT,
             THREAT,
             FAILURE+THREAT,
             FAILURE+THREAT,
             THREAT+THREAT,
             THREAT+THREAT,
             DESPAIR]

def interpret(dice):
    #print(dice)
    # remove blank results
    results = [x for x in dice if x != BLANK]
    #print("no blanks: {}".format(results))
    # split double symbols
    results = [x if len(x) == 1 else [x[0], x[1]] for x in results]
    #print("split doubles: {}".format(results))
    # flatten and sort list
    results = sorted([x for y in results for x in y])
    #print("flattened: {}".format(results))
    # cancel opposing results
    while True:
        # cancel success/failure
        if SUCCESS in results and FAILURE in results:
            results.remove(SUCCESS)
            results.remove(FAILURE)
        # cancel advantage/threat
        elif ADVANTAGE in results and THREAT in results:
            results.remove(ADVANTAGE)
            results.remove(THREAT)
        else:
            break

    #print(results)

    # return 1 for success/advantage, 0 for failure/threat
    if SUCCESS in results:
        if ADVANTAGE in results:
            return (1, 1)
        else:
            return (1, 0)
    elif ADVANTAGE in results:
        return (0, 1)
    return (0, 0)

results = [0, 0]
times = 10000
for _ in range(times):
    dice = []
    # roll boost dice
    for a in range(0):
        dice.append(BOOST[rand(0,5)])
    # roll ability dice
    for a in range(2):
        dice.append(ABILITY[rand(0,7)])
    # roll proficiency dice
    for p in range(0):
        dice.append(PROFICIENCY[rand(0,11)])
    # roll difficulty dice
    for d in range(2):
        dice.append(DIFFICULTY[rand(0,7)])
    result = interpret(dice)
    results[0] += result[0]
    results[1] += result[1]
print("SUCCESS RATE: {}%".format(100*results[0]/times))
print("THREAT LEVEL: {}%".format(100*results[1]/times))
