i = 1
pens = 15
pencils = 20
papers = 105
added = 0
added1 = 0
added2 = 0
additem = 0
additem1 = 0
additem2 = 0
while i < 10:

    print(":|WELCOME TO STORAGE CHECKER|:")
    print("           In stock:         ")
    print("Pencils: " + str(pencils))
    print("Pens: " + str(pens))
    print("Papers: " + str(papers))
    if added > 0:
        print(additem + ": " + str(added))
    if added1 > 0:
        print(additem1 + ": " + str(added1))
    if added2 > 0:
        print(additem2 + ": " + str(added2))
    print(" ")
    choice = input("Do you want to add anything?: ")
    print(" ")
    choice.lower()
    if choice == "yes":
        choice1 = input(str("What item do you want to add?: "))
        print(" ")
        choice1.lower()
        if choice1 == "pens":
            pens = pens + int(input("How many pens do you want to add?: "))
            print(" ")

        if choice1 == "pencils":
                pencils = pencils + int(input("How many pencils do you want to add?: "))
                print(" ")

        if choice1 == "papers":
                papers = papers + int(input("How many papers do you want to add?"))
                print(" ")
        if choice1 == "item":
            additem = input("What item do you want to add to the list?:")
            added = int(input("How many items are there?: "))
            print(" ")

        if choice1 == "item1":
            additem1 = input("What item do you want to add to the list?:")
            added1 = int(input("How many items are there?: "))
            print(" ")

        if choice1 == "item2":
            additem2 = input("What item do you want to add to the list?:")
            added2 = int(input("How many items are there?: "))
            print(" ")
        if choice1 == additem:
            added = added + int(input("How many " + additem + " do you want to add?"))
            print(" ")

        if choice1 == additem1:
            added1 = added1 + int(input("How many " + additem1 + " do you want to add?"))
            print(" ")

        if choice1 == additem2:
            added2 = added2 + int(input("How many " + additem2 + " do you want to add?"))
            print(" ")

        else:
            print("INVALID")
            print(" ")
    else:
        print(" ")
        print("Come back when you need to re stock!")
        print(" ")


