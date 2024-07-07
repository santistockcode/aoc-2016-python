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
    print("Move:", value)
    print("x =", x)
    print("y =", y)
    print("------")


input = "R3, R1, R4, L4, R3, R1, R1, L3, L5, L5, L3, R1, R4, L2, L1, R3, L3, R2, R1, R1, L5, L2, L1, R2, L4, R1, L2, L4, R2, R2, L2, L4, L3, R1, R4, R3, L1, R1, L5, R4, L2, R185, L2, R4, R49, L3, L4, R5, R1, R1, L1, L1, R2, L1, L4, R4, R5, R4, L3, L5, R1, R71, L1, R1, R186, L5, L2, R5, R4, R1, L5, L2, R3, R2, R5, R5, R4, R1, R4, R2, L1, R4, L1, L4, L5, L4, R4, R5, R1, L2, L4, L1, L5, L3, L5, R2, L5, R4, L4, R3, R3, R1, R4, L1, L2, R2, L1, R4, R2, R2, R5, R2, R5, L1, R1, L4, R5, R4, R2, R4, L5, R3, R2, R5, R3, L3, L5, L4, L3, L2, L2, R3, R2, L1, L1, L5, R1, L3, R3, R4, R5, L3, L5, R1, L3, L5, L5, L2, R1, L3, L1, L3, R4, L1, R3, L2, L2, R3, R3, R4, R4, R1, L4, R1, L5"
# Initialize the coordinates
x = 0
y = 0
# Read from the string buffer by commas
data = input.split(', ')
# Get the first letter to determine the sign of the x coordinate
goTo = getSign(data[0][0])
# Get the first number to determine the value of the x coordinate
x = goTo * getNumber(data[0])
print("Horizontal move")
printCoordinates(x, y, data[0])

# Iterate over the input data except the first element
counter = 1
for value in data[1:]:
    wentTo = goTo
    if(counter % 2 == 1):
        print("Vertical move")
        # Increase the coordinate y
        goTo = getNumberVertical(getSign(value[0]), wentTo)
        y += getNumber(value) * goTo
    elif(counter % 2 == 0):
        print("Horizontal move")
        goTo = getNumberHorizontal(getSign(value[0]), wentTo)   
        x += getNumber(value) * goTo
    counter += 1
    printCoordinates(x, y, value)

# Print the data
print("FINAL ANSWER: " ,abs(x) + abs(y))