with open('area.txt') as read_area:
    area = []
    for row in read_area:
        row = row.strip('\n')
        row = row*100
        row = row.split(' ')
        area.append(row)

x = 1
answer = 0
anslist = []

for j in range(4):
    i = 0
    for row in area:
        for coordinates in row:
            if coordinates[i] == '#':
                answer += 1
            i += 1*x
    anslist.append(answer)
    answer = 0
    x += 2

print(anslist)    
i = 0
j = 0

for row in area:
    for coordinates in row:
        if j % 2 == 0:
            if coordinates[i] == '#':
                answer += 1
            i += 1
        j += 1

anslist.append(answer)

print(anslist[0]*anslist[1]*anslist[2]*anslist[3]*anslist[4])