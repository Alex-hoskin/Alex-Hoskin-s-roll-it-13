print("🎲🎲 roll it 13 🎲🎲")


want_instructions = input("Do you want to read the instruction? ").lower()

 # checks users enter yes (y) or no (n)
if want_instructions == "yes" or want_instructions == "y":
    print("you chose yes")
elif want_instructions == "no" or want_instructions == "n":
     print("you chose no")
else:
     print("you didn't not chose a valid response")
