name = input("Hey type your name: ")
print("Hey " + name + " welcome to my game!")

should_we_play = input("Do you want to play").lower()
# play = should_we_play == "yes"
# print(play)

if should_we_play == "yes" or should_we_play == 'y':
    print("Let go!")

    direction = input("Do you want to go left or right?").lower()
    if direction == "left":
        print("You went left and fell os a cliff, game over, try again.")
    elif direction == 'right':
        print("We went right")
        choice = input("Okay, you now see a bridge, do you want to swim under it or cross it? (swim/cross)")
        if choice == "swim":
            print("You got eaten by an alligator, you die, the end!")
        else:
            print("You found the gold and won!")
    else:
        print('You die!')

elif should_we_play == "no" or should_we_play == 'n':
    print("We are not playing")
else:
    print("Enter yes or no")