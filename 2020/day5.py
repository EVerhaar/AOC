# part 1
all_boarding_passes = []
row_list = [x for x in range(128)]
col_list = [x for x in range(8)]
all_seat_ids = []

def lower_list(l):
    x = int(len(l)/2)
    new_list = l[:x]
    return new_list

def upper_list(l):
    x = int(len(l)/2)
    new_list = l[x:]
    return new_list

with open('boarding_passes.txt', 'r') as read_boarding_passes:
    for line in read_boarding_passes:
        line = line.strip('\n')
        all_boarding_passes.append(line)

for boarding_pass in all_boarding_passes:
    keep_rows = row_list
    keep_cols = col_list
    for char in boarding_pass:
        if char == 'F':
            keep_rows = lower_list(keep_rows)
        elif char == 'B':
            keep_rows = upper_list(keep_rows)
        elif char == 'L':
            keep_cols = lower_list(keep_cols)
        elif char == 'R':
            keep_cols = upper_list(keep_cols)
        else:
            print('error')
    seat_id = keep_rows[0] * 8 + keep_cols[0]
    all_seat_ids.append(seat_id)

print(max(all_seat_ids))

# part 2
missing_seats = []
for seat in range(max(all_seat_ids)):
    if seat not in all_seat_ids:
        missing_seats.append(seat)
print(missing_seats)