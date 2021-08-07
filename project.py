x = int(input("Guess and write a number:"))

if x < 10 and x > 7:
    print("Too high. Try again")

elif x > 5 and x < 7:
    print("Medium. Try a little less.")

else:
    print("Yay! You guessed the correct number.")