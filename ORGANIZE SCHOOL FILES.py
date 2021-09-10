import os
from pathlib import Path
poop = os.listdir("C:\\Users\\diivi\\Desktop\\Unsorted_SchoolWork")
print(poop)

for i in poop:
    if i[0:2].lower() == "cs":
        part = "C:\\Users\\diivi\\Desktop\\Unsorted_SchoolWork\\" + i
        part2 = "C:\\Users\\diivi\\Desktop\\Sorted_SchoolWork\\CS\\" + i
        Path(part).rename(part2)
    elif i[0:7].lower() == "english":
        part = "C:\\Users\\diivi\\Desktop\\Unsorted_SchoolWork\\" + i
        part2 = "C:\\Users\\diivi\\Desktop\\Sorted_SchoolWork\\English_10_Honors\\" + i
        Path(part).rename(part2)
    elif i[0:7].lower() == "biology":
        part = "C:\\Users\\diivi\\Desktop\\Unsorted_SchoolWork\\" + i
        part2 = "C:\\Users\\diivi\\Desktop\\Sorted_SchoolWork\\Biology_Honors\\" + i
        Path(part).rename(part2)
    elif i[0:6].lower() == "french":
        part = "C:\\Users\\diivi\\Desktop\\Unsorted_SchoolWork\\" + i
        part2 = "C:\\Users\\diivi\\Desktop\\Sorted_SchoolWork\\French_2\\" + i
        Path(part).rename(part2)
    elif i[0:8].lower() == "geometry":
        part = "C:\\Users\\diivi\\Desktop\\Unsorted_SchoolWork\\" + i
        part2 = "C:\\Users\\diivi\\Desktop\\Sorted_SchoolWork\\Geometry_Honors\\" + i
        Path(part).rename(part2)
    elif i[0:7].lower() == "history":
        part = "C:\\Users\\diivi\\Desktop\\Unsorted_SchoolWork\\" + i
        part2 = "C:\\Users\\diivi\\Desktop\\Sorted_SchoolWork\\US_History\\" + i
        Path(part).rename(part2)
    else:
        print("Invalid file: " + i)
