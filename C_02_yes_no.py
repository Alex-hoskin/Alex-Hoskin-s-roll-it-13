# check users enter yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("you didn't not chose a valid response")


# Main routine
want_instructions = yes_no("do you want to read the instructions ")
print(f"you chose {want_instructions}")

roll_again = yes_no("Do you want to roll again? ")
print(f"you said {roll_again} to rolling again. ")