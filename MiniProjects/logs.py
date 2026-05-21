def start():
    print("                     LOGS                       ")
    print("------------------------------------------------")
    print("   Date       |     Time (time1-time2)   | Paid ")
    print("------------------------------------------------")

date = ["--/--/----","--/--/----","--/--/----","--/--/----","--/--/----","--/--/----","--/--/----","--/--/----","--/--/----","--/--/----"]
time1 = ["--:--","--:--","--:--","--:--","--:--","--:--","--:--","--:--","--:--","--:--"]
time2 = ["--:--","--:--","--:--","--:--","--:--","--:--","--:--","--:--","--:--","--:--"]
paid = [" "," "," "," "," "," "," "," "," "," "]
count = 0
i = 0
p = 0
while i < 1:
    while p == 0:
        start()
        p = p + 1
    while count < 10:
        print(date[count] + "    |    " + time1[count] + "   -   " + time2[count]  + "    | "  + paid[count])
        count = count + 1
    edit = input("Do you want to edit anything? ")
    edit.lower()
    if edit == "yes":
        edit1 = input("Which column do you want to edit?")
        edit1.lower()
        if edit1 == "date":
            edit2 = int(input("Which row do you want to edit?"))
            if edit2 < 11:
                print("EDITING DATE ROW: " + str(edit2))
                print("Format: --/--/----")
                date[edit2 - 1] = input("Type the date here: ")
                p = 0
                count = 0
                print(" ")
                print(" ")
                print(" ")
            else:
                print("Invalid Row")

        if edit1 == "time1":
            edit2 = int(input("Which row do you want to edit?"))
            if edit2 < 11:
                print("EDITING TIME1 ROW: " + str(edit2))
                print("Format: --:--")
                time1[edit2 - 1] = input("Type the time1 here: ")
                p = 0
                count = 0
                print(" ")
                print(" ")
                print(" ")
            else:
                print("Invalid Row")

        if edit1 == "time2":
            edit2 = int(input("Which row do you want to edit?"))
            if edit2 < 11:
                print("EDITING TIME2 ROW: " + str(edit2))
                print("Format: --:--")
                time2[edit2 - 1] = input("Type the time2 here: ")
                p = 0
                count = 0
                print(" ")
                print(" ")
                print(" ")
            else:
                print("Invalid Row")

        if edit1 == "paid":
            edit2 = int(input("Which row do you want to edit?"))
            if edit2 < 11:
                print("EDITING DATE ROW: " + str(edit2))
                print("Format: Paid or Unpaid")
                paid[edit2 - 1] = input("Type if paid or unpaid here: ")
                p = 0
                count = 0
                print(" ")
                print(" ")
                print(" ")
            else:
                print("Invalid Row")

    else:
        print("Have a good day!")
        i = i + 1





