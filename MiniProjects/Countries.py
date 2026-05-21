import random
import openpyxl
path = "C:\\Users\\diivi\\Desktop\\Countries Guesser\\countriesandcapitals.xlsx"
wb = openpyxl.load_workbook(path)
sheet = wb.active
print(sheet["A" + str(random.randint(1, 199))].value)
print("Welcome to the Country Guesser!\n")
inp = input("Would you like to guess countries? or their capitals? ")
if inp.lower() == "countries":
    i1 = 0
    i2 = 0
    print("type end if you want the game to end, enjoy! :)")
    while True:
        rand = random.randint(1, 199)
        country = sheet["A" + str(rand)].value
        capital = sheet["B" + str(rand)].value
        print("\nYour score so far is", i1, "/", )
        print("\nYour country is:", country)
        inp2 = input("What is the country's capital?:")
        if inp2.lower() == capital.lower():
            print("\nCorrect!\n")
            i1 = i1 + 1
            i2 = i2 + 1
        if inp2.lower() == "end":
            print("Thanks for playing :)")
            break
        if inp2.lower() != capital.lower():
            print("\nWrong :(", str(country) + "'s capital is", str(capital))
            i2 = i2 + 1

if inp.lower() == "capitals":
    i1 = 0
    i2 = 0
    print("type end if you want the game to end, enjoy! :)")
    while True:
        rand = random.randint(1, 199)
        country = sheet["A" + str(rand)].value
        capital = sheet["B" + str(rand)].value
        print("\nYour score so far is", i1, "/", i2)
        print("\nYour capital is:", capital)
        inp2 = input("What is the country of that capital?:")
        if inp2.lower() == country.lower():
            print("\nCorrect!\n")
            i1 = i1 + 1
            i2 = i2 + 1
        if inp2.lower() == "end":
            print("Thanks for playing :)")
            break
        if inp2.lower() != country.lower():
            print("\nWrong :(", str(capital) + "'s country is", str(country))
            i2 = i2 + 1
