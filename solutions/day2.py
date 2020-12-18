#Read and format data from input file
def readFile(location):
    input = []
    file = open(location)
    for line in file:
        line = line.rstrip()
        temp = line.split(":")
        input.append(temp)
    return input

#Count number of valid passwords according to rules explained in the question
#Can be setup to work for part 1 or part 2
def countValidPasswords(passList, type= 1):
    validPassCount = 0
    if(type==1):
        validateFunc = countValidChar
    if(type==2):
        validateFunc = checkValidPos
    for passSet in passList:    
        policy = passSet[0]
        password = passSet[1]
        [passCount, passChar] = policy.split(" ")
        [lower, upper] = passCount.split("-")
        validPassCount += validateFunc(lower, upper, passChar, password)

    return validPassCount

#Helper function for part 1
#Check if the password contains the legal amount of the specified character
def countValidChar(lower, upper, passChar, password):
    count = 0
    for char in password:
        if(char == passChar):
            count+=1
    if(count >= int(lower) and count <= int(upper)):
        return 1
    return 0

#Helper function for part 2
#Checks that the specified char appears in one and only one of the given positions
def checkValidPos(lower, upper, passChar, password):
    lowerPos = int(lower)
    upperPos = int(upper)
    if(password[lowerPos] == passChar and password[upperPos]== passChar):
        return 0
    elif(password[lowerPos] == passChar or password[upperPos]== passChar):
        return 1
    return 0

#Part 1
#Made use of seperators in the strings to divide input into computable chunks 
input = readFile("./inputs/day2.txt")
output = countValidPasswords(input, 1)
print("The answer to part 1 is: " + str(output))

#Part 2
#For part 2, the function used in part one was repurposed so that it could be used for both parts
#The char counting section of part 1 was split off into the helper function countValidChar
#Meanwhile, the new position check for part 2 was added in the helper function checkValidPos
output = countValidPasswords(input, 2)
print("The answer to part 2 is: " + str(output))