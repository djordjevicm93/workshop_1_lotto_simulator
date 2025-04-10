from random import *

chosen_6 = list()  # empty list for 6 entered numbers
draw_6 = set()  # empty set for 6 draw numbers

def chose_6():
    """function for enter and filtrate 6 numbers"""
    while len(chosen_6) < 6:
        enter_6 = input("Enter number: ")
        try:
            if int(enter_6) < 1 or int(enter_6) > 49:
                print("Only numbers 1 to 49")
            elif enter_6 in chosen_6:
                print("Same number. Enter other number.")
            else:
                chosen_6.append(enter_6)  # if number pass if elif, go to list
        except ValueError:  # str
            print("Not number.")
    return chosen_6

# draw lotto numbers
while len(draw_6) < 6:
    draw_6.add(randint(1, 50))

chose_6()
print("Your numbers: ", sorted(list(chosen_6)))
print("Lotto numbers: ", sorted(list(draw_6)))

# count numbers
count_numbers = set(chosen_6) & set(draw_6)
print("Win:", len(count_numbers))
