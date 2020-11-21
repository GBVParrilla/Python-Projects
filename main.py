i = 1
pens = 15
pencils = 20
papers = 105

while i < 10:

    print(":|WELCOME TO STORAGE CHECKER|:")
    print("           In stock:         ")
    print("Pencils: " + str(pencils))
    print("Pens: " + str(pens))
    print("Papers: " + str(papers))
    print(" ")

    choice = input("Do you want to add anything?: ")
    print(" ")

    if choice == "yes":
        choice1 = input(str("What item do you want to add?: "))
        print(" ")
        if choice1 == "pens":
            pens = pens + int(input("How many pens do you want to add?: "))
            print(" ")

        if choice1 == "pencils":
                pencils = pencils + int(input("How many pencils do you want to add?: "))
                print(" ")

        if choice1 == "papers":
                papers = papers + int(input("How many papers do you want to add?"))
                print(" ")
        else:
            print("INVALID")
            print(" ")
    else:
        print(" ")
        print("Come back when you need to re stock!")
        print(" ")













