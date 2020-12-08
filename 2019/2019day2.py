# What is the checksum for your list of box IDs?

openinput = open('inputday2.txt', 'r')
listinputs = []
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
twoletters = 0
threeletters = 0

for ID in openinput:
    ID = ID.rstrip('\n')
    listinputs.append(ID)

for ID in listinputs:
    for letter in alphabet:
        count = ID.count(letter)
        if count == 2:
            for letter in alphabet:
                countsecond = ID.count(letter)
                if countsecond == 3:
                    threeletters += 1
                    break
            twoletters += 1
            break
        if count == 3:
            for letter in alphabet:
                countsecond = ID.count(letter)
                if countsecond == 2:
                    twoletters += 1
                    break
            threeletters += 1
            break

checksum = twoletters * threeletters

print(twoletters)
print(threeletters)
print(checksum)            

# What letters are common between the two correct box IDs?

box1 = 'abcde'
box2 = 'fghij'
box3 = 'klmno'
box4 = 'pqrst'
box5 = 'fguij'
box6 = 'axcye'
box7 = 'wvxyz'
listboxes = [box1, box2, box3, box4, box5, box6, box7]
listremoved = []

for box in listboxes:
    altbox = listboxes.pop(0)
    altbox = list(altbox)
    listboxes.append(altbox)

def checkduplicates(listofelems):
    for elem in listofelems:
        if listofelems.count(elem) > 1:
            print(elem)
            return True
    return False

for i in range(5):
    for altbox in listboxes:
        deletedn = altbox.pop(i)
        listremoved.append(deletedn)
    result = checkduplicates(listboxes)
    if result:
        print('The box above is the duplicate')
    for altbox in listboxes:
        altbox.insert(i, listremoved[0])
        listremoved.pop(0)


# verwijder [0] in alle altbox
# check of lijst[0] overeenkomt met een andere lijst in listboxes
# zo ja:
# print de altbox
# zo nee:
# voeg de letter [0] weer toe op dezelfde plek [0] in altbox

openinput.close()
