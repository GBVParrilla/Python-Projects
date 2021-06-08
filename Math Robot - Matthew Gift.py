import math


i = 1

while i == 1:
    print("\n\n\n\n\n\n\n\n\n\n\nMATH ROBOT")
    print("\nWelcome Matthew! What do you want to do today?\n")
    print("CHOICES: area, perimeter, find side, calculator (you can use just the first letter for all choices)")
    choice = input("Input choice here:")
    choice.lower()

    #Calculating area
    if choice[0] == "a":
        print("\n\nWhat shape are you trying to find the area of?\n")
        print("CHOICES: square, rectangle, triangle")
        achoice = input("Input choice here:")
        achoice.lower()
        if achoice[0] == "s":
            slength = int(input("\n\nWhat is the length of one side of the square?:"))
            print("The area of the square is", slength * slength)
            end = input("Do you want to do more math? (yes,no):")
            if end[0] == "y":
                continue
            elif end[0] == "n":
                break

        elif achoice[0] == "r":
            rlength = int(input("\n\nWhat is the length of one sides of the rectangle?:"))
            rwidth = int(input("What is the width of one sides of the rectangle?:"))
            print("The area of the rectangle is", rlength * rwidth)
            end = input("Do you want to do more math? (yes,no):")
            if end[0] == "y":
                continue
            elif end[0] == "n":
                break

        elif achoice[0] == "t":
            theight = int(input("\n\nWhat is the height of the triangle?:"))
            twidth = int(input("What is the width of the triangle?:"))
            print("The area of the triangle is", theight * twidth / 2)
            end = input("Do you want to do more math? (yes,no):")
            if end[0] == "y":
                continue
            elif end[0] == "n":
                break

    #CALCULATING PERIMETER
    elif choice[0] == "p":
        print("\n\nWhat shape are you trying to find the perimeter of?\n")
        print("CHOICES: square, rectangle, triangle")
        pchoice = input("Input choice here:")
        pchoice.lower()
        if pchoice[0] == "s":
            plength = int(input("\n\nWhat is the length of one side of the square?:"))
            print("The perimeter of the square is", plength * 4)
            end = input("Do you want to do more math? (yes,no):")
            if end[0] == "y":
                continue
            elif end[0] == "n":
                break
        elif pchoice[0] == "r":
            plength = int(input("\n\nWhat is the length of the rectangle?:"))
            pwidth = int(input("What is the width of the rectangle?:"))
            answer = (plength * 2) + (pwidth * 2)
            print("The perimeter of the rectangle is", answer)
            end = input("Do you want to do more math? (yes,no):")
            if end[0] == "y":
                continue
            elif end[0] == "n":
                break
        elif pchoice[0] == "t":
            pside1 = int(input("\n\nWhat is the length of side 1?:"))
            pside2 = int(input("What is the length of side 2?:"))
            pside3 = int(input("What is the length of side 3?:"))
            print("The perimeter of the triangle is", pside1 + pside2 + pside3)
            end = input("Do you want to do more math? (yes,no):")
            if end[0] == "y":
                continue
            elif end[0] == "n":
                break

    #FIND SIDE
    elif choice[0] == "f":
        print("\n\nWhat shape are you trying to find the side of?\n")
        print("CHOICES: square, rectangle, triangle")
        fchoice = input("Input choice here:")
        fchoice.lower()
        if fchoice[0] == "s":
            squarechoice = input("\n\nDo have the perimeter or area?")
            squarechoice.lower()
            if squarechoice[0] == "a":
                farea = int(input("What is the area of the square?"))
                print("The side of the square is", math.sqrt(farea))
                end = input("Do you want to do more math? (yes,no):")
                if end[0] == "y":
                    continue
                elif end[0] == "n":
                    break
            elif squarechoice[0] == "p":
                fperimeter = int(input("What is the perimeter of the square?"))
                print("The side of the square is", fperimeter / 4)
                end = input("Do you want to do more math? (yes,no):")
                if end[0] == "y":
                    continue
                elif end[0] == "n":
                    break

        elif fchoice[0] == "r":
            rectanglechoice = input("\n\nDo you have area and a side (area) or do you have perimeter and a side? (perimeter):")
            rectanglechoice.lower()
            if rectanglechoice[0] == "a":
                rarea = int(input("What is the area of the rectangle?:"))
                rside = int(input("What is the side of the rectangle?"))
                print("The other side of the rectangle is", rarea / rside)
                end = input("Do you want to do more math? (yes,no):")
                if end[0] == "y":
                    continue
                elif end[0] == "n":
                    break
                else:
                    print("Invalid choice!")

            elif rectanglechoice[0] == "p":
                parea = int(input("What is the perimeter of the rectangle?:"))
                pside = int(input("What is the side of the rectangle?"))
                answer = (parea - (pside * 2)) / 2
                print("The other side of the rectangle is", answer)
                end = input("Do you want to do more math? (yes,no):")
                if end[0] == "y":
                    continue
                elif end[0] == "n":
                    break
                else:
                    print("Invalid choice!")

            else:
                print("Invalid choice!")

        elif fchoice[0] == "t":
            trianglechoice = input("\n\nDo you have the area or the perimeter of the triangle?:")
            trianglechoice.lower()
            if trianglechoice[0] == "p":
                rperimeter = int(input("What is the perimeter of the triangle?:"))
                rside1 = int(input("What is the side 1 of the triangle?:"))
                rside2 = int(input("What is the side 2 of the triangle?:"))
                answer = rperimeter - (rside1 + rside2)
                print("The missing side of the triangle is", answer)
                end = input("Do you want to do more math? (yes,no):")
                if end[0] == "y":
                    continue
                elif end[0] == "n":
                    break
                else:
                    print("Invalid choice!")


            elif trianglechoice[0] == "a":
                trianglechoice1 = input("Do you have the height or the width?:")
                trianglechoice1.lower()
                if trianglechoice1[0] == "h":
                    rarea = int(input("What is the area of the triangle?:"))
                    rheight = int(input("What is the height of the triangle?:"))
                    print("The width of the triangle is", (rarea * 2)/rheight)
                    end = input("Do you want to do more math? (yes,no):")
                    if end[0] == "y":
                        continue
                    elif end[0] == "n":
                        break
                elif trianglechoice1[0] == "w":
                    rarea = int(input("What is the area of the triangle?:"))
                    rwidth = int(input("What is the width of the triangle?:"))
                    print("The height of the triangle is", (rarea * 2)/rwidth)
                    end = input("Do you want to do more math? (yes,no):")
                    if end[0] == "y":
                        continue
                    elif end[0] == "n":
                        break
                else:
                    print("Invalid choice!")
        else:
            print("Invalid choice!")


    #CALCULATOR
    elif choice[0] == "c":
        print("Welcome to the Calculator,  Mr. Matthew!")
        answer = 0
        while i == 1:
            print("\n\nThe number right now is", answer)
            print("CHOICES: add, subtract, multiply, divide, clear, end (You can use just the first letter)")
            cchoice = input("What do you want to do?")
            cchoice.lower()
            if cchoice[0] == "c":
                try:
                    print("\nThe answer has been cleared!")
                    answer = 0
                except:
                    print("Something went horribly wrong!")

            elif cchoice[0] == "e":
                try:
                    print("\nThank you for using the calculator!")
                    break
                except:
                    print("Something went horribly wrong!")

            elif cchoice[0] == "a":
                try:
                    add = int(input("\nHow much do you want to add?:"))
                    answer += add
                except:
                    print("Something went horribly wrong!")

            elif cchoice[0] == "s":
                try:
                    subtract = int(input("\nHow much do you want to subtract?:"))
                    answer -= subtract
                except:
                    print("Something went horribly wrong!")

            elif cchoice[0] == "m":
                try:
                    multiply = int(input("\nHow much do you want to multiply?:"))
                    answer *= multiply
                except:
                    print("Something went horribly wrong!")

            elif cchoice[0] == "d":
                try:
                    divide = int(input("\nHow much do you want to divide?"))
                    answer /= divide
                except ZeroDivisionError:
                    print("You cant divide by zero!")
                except:
                    print("Something went horribly wrong!")

            else:
                print("Invalid choice!")
    else:
        print("Invalid choice!")






