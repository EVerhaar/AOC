gamma_rate = ''
epsilon_rate = ''

numbers = ''

with open('pi3.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        numbers += line

n = 0
num_list = []
for x in range(12):
    for num in numbers[n::12]:
        num = int(num)
        num_list.append(num)
    count_one = num_list.count(1)
    count_zero = num_list.count(0)
    if count_one > count_zero:
        gamma_rate += '1'
        epsilon_rate += '0'
    else:
        gamma_rate += '0'
        epsilon_rate += '1'
    n += 1
    num_list = []

# part 2

def count_bits(n_one, n_zero):
    if count_one > count_zero:
        return '1'
    else:
        return '0'

numbers = []
with open('pi3.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        numbers.append(line)

gamma_list = []
epsilon_list = []


for x in range(12):
    for number in numbers[x::12]:
        print(number)
        if number == '1':
            count_one += 1
        elif number == '0':
            count_zero += 1
    most_frequent_number = count_bits(count_one, count_zero)
    print(most_frequent_number)