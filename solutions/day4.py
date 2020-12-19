import re

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
        valid = True
        for field in fields:
            if not (field in passport):
                invalidPassports+=1
                valid = False
                break
        if(valid):
            invalidPassports += dataValidation(passport)
    return (len(passports) - invalidPassports)

#Data Validation function
def dataValidation(passport):
    byrVal = passport["byr"]
    iyrVal = passport["iyr"]
    eyrVal = passport["eyr"]
    hgtVal = passport["hgt"]
    hclVal = passport["hcl"]
    hclPattern = "^#[0-9a-f]{6}$"
    eclVal = passport["ecl"]
    pidVal = passport["pid"]
    if(len(byrVal) != 4 or int(byrVal) < 1920 or int(byrVal) > 2002):
        return 1
    if(len(iyrVal) != 4 or int(iyrVal) < 2010 or int(iyrVal) > 2020):
        return 1
    if(len(eyrVal) != 4 or int(eyrVal) < 2020 or int(eyrVal) > 2030):
        return 1
    if(len(hgtVal)<3):
        return 1
    if(hgtVal[2] == "i"): 
        if (int(hgtVal[:2]) < 59 or int(hgtVal[:2]) > 76):
            return 1

    elif(hgtVal[3] == "c"):
            if (int(hgtVal[:3]) < 150 or int(hgtVal[:3]) > 193):     
                return 1
    else:
        return 1
    if not(bool(re.match(hclPattern, hclVal))):
        return 1
    if not(eclVal == "amb" or eclVal == "blu" or eclVal == "brn" or eclVal == "gry" or eclVal == "grn" or eclVal == "hzl" or eclVal == "oth"):
        return 1
    if(len(pidVal) != 9 or pidVal.isnumeric() == False):
        return 1
    print(passport)
    return 0  


# Part 1

input = readFile("./inputs/day4.txt")
output1 = checkValid(input)
print("The answer to part 1 is: " + str(output1))

# Part 2
#Part 2 involved making a massive validation function that performed sanity checks on the data
#It was not fun it took forever, and I put the issue year instead of the expiry year in one of the comparisons
#Took ages to find, very annoying
