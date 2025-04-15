from random import shuffle

def chose_6():
    """
    Lotto simulator

    Enter 6 number from 1 to 49. Computer will draw 6 numbers.
    You will se if you guessed 3, 4, 5, 6 or nothing.
    """
    chosen_6 = list()  # empty list for 6 entered numbers
    while len(chosen_6) < 6:
        enter_6 = input("Enter number 1 - 49: ")
        try:
            number = int(enter_6)
            if number < 1 or number > 49:
                print("Only numbers 1 to 49")
            elif number in chosen_6:
                print("Same number. Enter other number.")
            else:
                chosen_6.append(number)  # if number pass if elif, go to list
        except ValueError:  # str
            print("That is not number.")
    return chosen_6

# draw lotto numbers
draw_6 = list(range(1, 50))
shuffle(draw_6)
drawn_numbers = draw_6[:6]

#chose_6()
chosen_6 = chose_6()
sorted_6 = sorted(chosen_6)
print("Your numbers: ", sorted_6)
print("Lotto numbers: ", sorted(drawn_numbers))

# count matched
matches = [x for x in sorted_6 if x in drawn_numbers]
match_count = len(matches)
print("Matched numbers:", matches)
print("Total matches:", match_count)

rewards = {
    6: "JACKPOT! You hit all 6 numbers!",
    5: "Great job! You matched 5 numbers!",
    4: "Nice! You matched 4 numbers!",
    3: "You matched 3 numbers. Small win!",
}

print("Result:", rewards.get(match_count))
