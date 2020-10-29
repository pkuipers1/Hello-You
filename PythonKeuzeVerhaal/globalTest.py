import os
# Test

test = False

def func():

    global test
    test = True

print(test)

func()

os.system("cls")

print(test)

nurseJob = False

def nurseJobHired():
    os.system("cls")
    print("Oo------------oOo-------------oO")
    print("| -UMC Amsterdam-             |")
    print("|                             |")
    print("| You are now hired!          |")
    print("|                             |")
    print("| Salary: €55K Anually        |")
    print("|                             |")
    print("Oo---------------------------oO")

    global nurseJob
    nurseJob = True
    print(nurseJob)
nurseJobHired()

def testtest():
    print(nurseJob)
testtest()
