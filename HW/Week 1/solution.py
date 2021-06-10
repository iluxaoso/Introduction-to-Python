import sys

#stairs_num = input("Введите количество лестниц: ")
stairs_num = sys.argv[1]

i = 0

while i != int(stairs_num):
    string = ""
    for j in range(int(stairs_num) - i - 1):
        string += " "
    for j in range(int(stairs_num) - i - 1, int(stairs_num)):
        string += "#"

    print(string)
    i += 1
