import os
from pathlib import Path
print("Welcome to the File Organizer!\n\n")
start = ""
end = ""

print("Let's first set up the start folder.\n")
while True:
    inp1 = input("What is the letter of the drive you are trying to start with? (i.e C, D)")
    if len(inp1) != 1:
        print("It should only be one letter!")
    if len(inp1) == 1:
        print("Input received. File drive:", inp1)
        start += inp1.upper() + ":"
        break


print("Now it's time for the file path! Just type 'done' when you are finished")
print("NOTE: ONLY FOLDERS!")
while True:
    print("\nFile path so far:","'" + start + "'")
    inp2 = input("What would you like to add to the file path:")
    if inp2 == "done":
        break
    if inp2 == "":
        print("You're supposed to input something!")
    if inp2 != "done":
        print("Input received! Folder added:", inp2)
        start += "\\" + inp2


print("\n\nNow it's time for the destination folder.")
while True:
    inp1 = input("What is the letter of the drive you are trying to start with? (i.e C, D)")
    if len(inp1) != 1:
        print("It should only be one letter!")
    if len(inp1) == 1:
        print("Input received. File drive:", inp1)
        end += inp1.upper() + ":"
        break

print("Now it's time for the destination folder! Just type 'done' when you are finished")
print("NOTE: ONLY FOLDERS!")
while True:
    print("\nFile path so far:","'"+end+"'")
    inp2 = input("What would you like to add to the file path:")
    if inp2 == "done":
        break
    if inp2 == "":
        print("You're supposed to input something!")
    if inp2 != "done":
        print("Input received! Folder added:", inp2)
        end += "\\" + inp2


print("\nNow it's time for the file paths! Just type 'done' when you are finished (folder doesn't have to exist)")
i = 0
list = []
print("Input 'done' if you're finished")
while True:
    print("\nFolders so far:", list)
    inp = input("What should the program look for in the file name?")
    if inp != "":
        list += "t"
        list[i] = inp
        i += 1
    if inp == "":
        print("You're supposed to input something!")
    if inp == "done":
        break

for i2 in list:
    try:
        folder = end + "\\" + i2
        os.mkdir(folder)
    except:
        None


files = os.listdir(start)
for i1 in files:
    for i2 in list:
        for i3 in range(len(i1)):
            try:
                chunk = i1[i3:(i3 + len(i2))]
            except:
                None
            if chunk.lower() == i2.lower():
                part = start + "\\" + i1
                part2 = end + "\\" + i2 + "\\" + i1
                Path(part).rename(part2)





