# a = Rock
# b = Paper
# c = Scissor

# x = Rock = 1 point
# y = Paper = 2 points
# z = Scissor = 3 points

shapes = []
score = 0

win = 6
draw = 3
lose = 0

rock = 1
paper = 2
scissor = 3

with open('strat_guide.txt') as f:
    strategy_guide = f.readlines()

    for line in strategy_guide:
        line = line.split()
        shapes.append(line)

for game in shapes:
    if game[0] == 'A':
        if game[1] == 'X':
            score += rock + draw
        elif game[1] == 'Y':
            score += paper + win
        elif game[1] == 'Z':
            score += scissor
    elif game[0] == 'B':
        if game[1] == 'X':
            score += rock
        elif game[1] == 'Y':
            score += paper + draw
        elif game[1] == 'Z':
            score += scissor + win
    elif game[0] == 'C':
        if game[1] == 'X':
            score += rock + win
        elif game[1] == 'Y':
            score += paper
        elif game[1] == 'Z':
            score += scissor + draw

print(score)

# X = lose
# Y = draw
# Z = win

score = 0

for game in shapes:
    if game[1] == 'X':
        if game[0] == 'A':
            score += scissor
        if game[0] == 'B':
            score += rock
        if game[0] == 'C':
            score += paper
    if game[1] == 'Y':
        if game[0] == 'A':
            score += rock + draw
        if game[0] == 'B':
            score += paper + draw
        if game[0] == 'C':
            score += scissor + draw
    if game[1] == 'Z':
        if game[0] == 'A':
            score += paper + win
        if game[0] == 'B':
            score += scissor + win
        if game[0] == 'C':
            score += rock + win

print(score)