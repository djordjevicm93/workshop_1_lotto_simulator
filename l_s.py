import random

chosen_6 = list()
# 1
try:
    chose_1 = int(input("Enter number"))
    if chose_1 not in range(1, 50):
        print("Only numbers 1 to 49")
    elif chose_1 in chosen_6:
        print("Same number. Enter other number.")
    else:
        chosen_6.append(chose_1)
except ValueError:
    print("Not number. Enter number.")
# 2
try:
    chose_2 = int(input("Enter number"))
    if chose_2 not in range(1, 50):
        print("Only numbers 1 to 49")
    elif chose_2 in chosen_6:
        print("Same number. Enter other number.")
    else:
        chosen_6.append(chose_2)
except ValueError:
    print("Not number. Enter number.")
# 3
try:
    chose_3 = int(input("Enter number"))
    if chose_3 not in range(1, 50):
        print("Only numbers 1 to 49")
    elif chose_3 in chosen_6:
        print("Same number. Enter other number.")
    else:
        chosen_6.append(chose_3)
except ValueError:
    print("Not number. Enter number.")
# 4
try:
    chose_4 = int(input("Enter number"))
    if chose_4 not in range(1, 50):
        print("Only numbers 1 to 49")
    elif chose_4 in chosen_6:
        print("Same number. Enter other number.")
    else:
        chosen_6.append(chose_4)
except ValueError:
    print("Not number. Enter number.")
# 5
try:
    chose_5 = int(input("Enter number"))
    if chose_5 not in range(1, 50):
        print("Only numbers 1 to 49")
    elif chose_5 in chosen_6:
        print("Same number. Enter other number.")
    else:
        chosen_6.append(chose_5)
except ValueError:
    print("Not number. Enter number.")
# 6
try:
    chose_6 = int(input("Enter number"))
    if chose_6 not in range(1, 50):
        print("Only numbers 1 to 49")
    elif chose_6 in chosen_6:
        print("Same number. Enter other number.")
    else:
        chosen_6.append(chose_6)
except ValueError:
    print("Not number. Enter number.")

sorted_chosen = sorted(chosen_6)
draw_random_6 = sorted(random.sample(range(1, 50), 6))

print("Chosen numbers", sorted_chosen)
print("Draw numbers", draw_random_6)
