all_passwords = []

with open('passwords.txt') as read_pw:
    new_password = []
    for passwords in read_pw:
        passwords = passwords.strip('\n')
        passwords = passwords.replace('-', ' ')
        passwords = passwords.replace(':', '')
        passwords = passwords.split(' ')
        all_passwords.append(passwords)

i = 0
answer = 0

for password_seq in all_passwords:
    min_val = int(password_seq[0])
    max_val = int(password_seq[1])
    letter = password_seq[2]
    possible_password = password_seq[3]
    i = 0
    for check_letter in possible_password:
        if letter == check_letter:
            i += 1
    if i in range(min_val, max_val+1):
        answer += 1
    
print(answer)
answer = 0

for password_seq in all_passwords:
    first_char = int(password_seq[0])
    second_char = int(password_seq[1])
    letter = password_seq[2]
    possible_password = password_seq[3]
    if possible_password[first_char-1] == letter or possible_password[second_char-1] == letter:
        if possible_password[first_char-1] != possible_password[second_char-1]:
            print(password_seq)
            answer += 1

print(answer)