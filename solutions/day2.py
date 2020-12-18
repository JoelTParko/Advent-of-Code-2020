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
#Check if the password contains the legal amount of the specified character
def countValidPasswords(passList):
    validPassCount = 0
    for passSet in passList:
        count = 0
        policy = passSet[0]
        password = passSet[1]
        [passCount, passChar] = policy.split(" ")
        [lower, upper] = passCount.split("-")
        for char in password:
            if(char == passChar):
                count+=1
        if(count >= int(lower) and count <= int(upper)):
            validPassCount+=1
    return validPassCount

#Part 1
#Made use of seperators in the strings to divide input into computable chunks 
input = readFile("./inputs/day2.txt")
output = countValidPasswords(input)
print(output)