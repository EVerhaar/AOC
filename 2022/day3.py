import string

item_priorities = dict.fromkeys(string.ascii_lowercase + string.ascii_uppercase, 0)
n = 1
for key in item_priorities:
    item_priorities[key] = item_priorities[key] + n
    n += 1

all_backpacks = []
backpacks = []

with open('backpacks.txt') as f:
    backpack_file = f.readlines()
    for backpack_code in backpack_file:
        backpack_code = backpack_code.strip()
        all_backpacks.append(backpack_code)
        compartment_1 = backpack_code[:(len(backpack_code))//2]
        compartment_2 = backpack_code[(len(backpack_code))//2:]
        compartments = [compartment_1, compartment_2]
        backpacks.append(compartments)

wrong_items = []
for backpack in backpacks:
    for compartment in backpack:
        for item in backpack[0]:
            if item in backpack[1]:
                wrong_items.append(item)
                break
        break

sum = 0
for item in wrong_items:
    sum += item_priorities[item]

print(sum)
group = []
grouped_backpacks = []
i = 0

for backpack in all_backpacks:
    group.append(backpack)
    i += 1
    if i > 2:
        grouped_backpacks.append(group)
        group = []
        i = 0

badges = []
for groups in grouped_backpacks:
    for backpack in groups:
        for item in groups[0]:
            if item in groups[1] and item in groups[2]:
                badges.append(item)
                break
        break

sum = 0
for item in badges:
    sum += item_priorities[item]
print(sum)