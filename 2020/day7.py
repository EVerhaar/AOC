all_bags = []

def listToString(l):  
    str1 = " " 
    return (str1.join(l)) 
 
with open('bag_rules.txt', 'r') as read_bag_rules:
    for line in read_bag_rules:
        line = line.strip('\n')
        line = line.split(' ')
        new_bag = {}
        first_bag = []
        second_bag = []
        third_bag = []
        fourth_bag = []
        for i, word in enumerate(line):
            if word == line[4]:
                first_bag.append(line[4]+' '+line[5]+' '+line[6])
            if line[8]:
                if word == line[8]:
                    second_bag.append(line[8]+' '+line[9]+' '+line[10])
            if line[12]:
                if word == line[12]:
                    third_bag.append(line[12]+' '+line[13]+' '+line[14])
            if line[16]:
                if word == line[16]:
                    fourth_bag.append(line[16]+' '+line[17]+' '+line[18])
            print(first_bag)