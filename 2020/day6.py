import re
import string

# part 1
answer_list = []
new_group = []
group_answers = []
counts = []

with open('answers.txt', 'r') as read_answers:
    for line in read_answers:
        line = line.strip('\n')
        if line != '':
            new_group.append(line)
        else:
            answer_list.append(new_group)
            new_group = []

for group in answer_list:
    group_answers = []
    for answers in group:
        for answer in answers:
            group_answers.append(answer)
        group_answers = list(set(group_answers))
    counts.append(len(group_answers))

answer = 0
for count in counts:
    answer = int(count) + answer

print(answer)

# part 2
alphabet = list(string.ascii_lowercase)
all_counts = []
count = 0
i = 0
answered_by_all = 0


for group in answer_list:
    for letter in alphabet:
        i = 0
        for answer in group:
            if letter in answer:
                count += 1
                i += 1
                if count == (len(group)):
                    answered_by_all += 1
        else:
            count = 0
    all_counts.append(answered_by_all)
    answered_by_all = 0
    
final_answer = 0
print(all_counts)
for answer in all_counts:
    final_answer = answer + final_answer

print(final_answer)
