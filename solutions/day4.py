#Reads the data in from the text file
#Formats each passport into a dictionary, relating a field to a value
#Returns list of dictionaries 
def readFile(location):
    input = []
    passport = dict()
    file = open(location)
    for line in file:
        if(line=="\n"):
            input.append(passport)
            passport = dict()
        else:
            line = line.rstrip()
            line = line.split(" ")
            for field in line:
                field = field.split(":")
                passport[field[0]] = field[1]
    input.append(passport)
    return input

#Takes a list of passports
#Has a list of necassary fields, and checks that they are contained in each passport
#If they are not, the passport is declared invalid
#Return total passports minus invalid
def checkValid(passports):
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    invalidPassports = 0
    for passport in passports:
        for field in fields:
            if not (field in passport):
                invalidPassports+=1
                break
    return (len(passports) - invalidPassports)

# Part 1

input = readFile("./inputs/day4.txt")
print(input[-1])
output1 = checkValid(input)
print("The answer to part 1 is: " + str(output1))