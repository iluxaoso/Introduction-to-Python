import sys

digit_string = sys.argv[1]
sum = 0

"""
digit_string = input("Введите строку из чисел: ")

    if digit_string is None:
        print("Введите число")
        continue

    if not digit_string.isdigit():
        print("Введите правильное число")
        continue
    else:
        if int(digit_string) < 0:
            print("Введите положительное число")
            continue
        else:
            break
"""

for number in digit_string:
    sum += int(number)

print(sum)
