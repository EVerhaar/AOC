horizontal = 0
depth = 0
puzzle_input = []

with open('pi2.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        line = line.split()
        line[-1] = int(line[-1])
        puzzle_input.append(line)


for line in puzzle_input:
    command = line[0]
    movement = line[1]

    # for command in line:
    if command == 'forward':
        horizontal += movement
    elif command == 'down':
        depth += movement
    elif command == 'up':
        depth -= movement

result = horizontal * depth
print(result)

horizontal = 0
depth = 0
aim = 0

for line in puzzle_input:
    command = line[0]
    movement = line[1]
    if command == 'forward':
        horizontal += movement
        depth += (movement * aim)
        print(horizontal, aim, depth)
    elif command == 'down':
        aim += movement
    elif command == 'up':
        aim -= movement

result = horizontal * depth
print(result)