# Function that takes a letter and a number and returns a number
def getNumberVertical(letter, last):
    if (letter == last):
        return -1
    elif (letter != last):
        return 1

def getNumberHorizontal(letter, last):
    if (letter == last):
        return 1
    elif (letter != last):
        return -1
    
# Function returns 1 if R or -1 if L
def getSign(letter):
    if (letter == 'R'):
        return 1
    elif (letter == 'L'):
        return -1
    
# Function get number from value
def getNumber(value):
    final = 0
    for character in value[1:]:
        final = final * 10 + int(character)
    return final

# Function prints coordenates where we are
def printCoordinates(x, y, value):
    # Create dictionary with coordenates
    print("Move:", value)
    print("x =", x)
    print("y =", y)
    print("------")

def add_to_list(ma_list, z):
    ma_list.append(z)

def check_for_dup(seq):
    return len(seq) != len(set(seq))


# dict for duplicates
list_for_dup = []

input = "R3, R1, R4, L4, R3, R1, R1, L3, L5, L5, L3, R1, R4, L2, L1, R3, L3, R2, R1, R1, L5, L2, L1, R2, L4, R1, L2, L4, R2, R2, L2, L4, L3, R1, R4, R3, L1, R1, L5, R4, L2, R185, L2, R4, R49, L3, L4, R5, R1, R1, L1, L1, R2, L1, L4, R4, R5, R4, L3, L5, R1, R71, L1, R1, R186, L5, L2, R5, R4, R1, L5, L2, R3, R2, R5, R5, R4, R1, R4, R2, L1, R4, L1, L4, L5, L4, R4, R5, R1, L2, L4, L1, L5, L3, L5, R2, L5, R4, L4, R3, R3, R1, R4, L1, L2, R2, L1, R4, R2, R2, R5, R2, R5, L1, R1, L4, R5, R4, R2, R4, L5, R3, R2, R5, R3, L3, L5, L4, L3, L2, L2, R3, R2, L1, L1, L5, R1, L3, R3, R4, R5, L3, L5, R1, L3, L5, L5, L2, R1, L3, L1, L3, R4, L1, R3, L2, L2, R3, R3, R4, R4, R1, L4, R1, L5"

# Initialize the coordinates
x = 0
y = 0
# Read from the string buffer by commas
data = input.split(', ')
# Get the first letter to determine the sign of the x coordinate
goTo = getSign(data[0][0])

# for the list
last_x = 0
# Get the first number to determine the value of the x coordinate
x = goTo * getNumber(data[0])
followed_path = x - last_x
i = 0
while i < abs(followed_path):
    add_to_list(list_for_dup, str(last_x) + ":" + str(y))
    last_x += 1 * goTo
    i += 1

print("First Horizontal move")
printCoordinates(x, y, data[0])

# Iterate over the input data except the first element
counter = 1
for value in data[1:]:
    wentTo = goTo
    
    if(counter % 2 == 1):
        print("Vertical move")
        # Increase the coordinate y
        goTo = getNumberVertical(getSign(value[0]), wentTo)
        last_y = y; 
        y += getNumber(value) * goTo
        # iterate and add to list
        followed_path = y - last_y
        i = 0
        while i < abs(followed_path):
            add_to_list(list_for_dup, str(x) + ":" + str(last_y))
            if(check_for_dup(list_for_dup)):
                print("Hurray" + str(x) + ":" + str(last_y))
                print(abs(x) + abs(last_y))
                exit(1)
            last_y += 1 * goTo
            i += 1
        print("added vertical to list")

    elif(counter % 2 == 0):
        print("Horizontal move")
        goTo = getNumberHorizontal(getSign(value[0]), wentTo)
        # save last x position
        last_x = x
        # get next x position
        x += getNumber(value) * goTo
        # iterate over each position in path
        followed_path = x - last_x
        i = 0
        while i < abs(followed_path):
            add_to_list(list_for_dup, str(last_x) + ":" + str(y))
            if(check_for_dup(list_for_dup)):
                print("hurray" + str(last_x) + ":" + str(y))
                print(abs(last_x)+abs(y))
                exit(1)
            last_x += 1 * goTo
            i += 1
        print("added horizontal to list")
    
    print("This is the list now:")
    for n in list_for_dup:
        print(n)


    counter += 1
    #printCoordinates(x, y, value)
    #add_to_list(list_for_dup, str(x) + ":" + str(y))
    #if (check_for_dup(list_for_dup)):
    #    printCoordinates(x, y, value)
    #    print(abs(int(str(x))) + abs(int(str(y))))
    #    exit(1)

for j in list_for_dup:
    print(j)

# Print the data
print("FINAL ANSWER: " ,abs(x) + abs(y))
