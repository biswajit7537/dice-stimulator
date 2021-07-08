import random
print("__________ Dice Stimulator __________")
while True:
    number = random.randint(1,6)
    if number == 1:
        print("----------")
        print("|        |")
        print("|   O    |")
        print("|        |")
        print("----------")
    elif number == 2:
        print("----------")
        print("| O      |")
        print("|        |")
        print("|      O |")
        print("----------")
    elif number == 3:
        print("----------")
        print("| O      |")
        print("|    O   |")
        print("|      O |")
        print("----------")
    elif number == 4:
        print("----------")
        print("| O    O |")
        print("|        |")
        print("| O    O |")
        print("----------")
    elif number == 5:
        print("----------")
        print("| O    O |")
        print("|    O   |")
        print("| O    O |")
        print("----------")
    elif number == 6:
        print("----------")
        print("| O    O |")
        print("| O    O |")
        print("| O    O |")
        print("----------")
    print("\n")
    stop = input("Press y for continue or q for quite : ")
    if stop == 'q':
        break

    