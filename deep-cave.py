import random, sys, time

# set up the constants
WIDTH = 70
PAUSE_AMOUNT = 0.05

print("Deep Cave")
time.sleep(2)
leftWidth = 20
gapWidth = 10

while True:
    # display the tunnel segment
    rightWidth = WIDTH - gapWidth - leftWidth
    print(("#" * leftWidth) + ("." * gapWidth) + ("#" * rightWidth))

    # check for ctrl+c press during the brief pause
    try:
        time.sleep(PAUSE_AMOUNT)
    except KeyboardInterrupt:
        sys.exit()  # when ctrl+C is pressed, end the program

    # adjust the left side width
    diceRoll = random.randint(1, 2)
    if diceRoll == 1 and leftWidth > 1:
        leftWidth -= 1  # decrease the left side width
    elif diceRoll == 2 and leftWidth + gapWidth < WIDTH - 1:
        leftWidth += 1  # increase left side width
    else:
        pass  # do nothing - no change in left side width

    # adjust the gap width (can uncomment if desired)
    diceRoll = random.randint(1, 6)
    if diceRoll == 1 and gapWidth > 1:
        gapWidth -= 1  # decrease gap width
    elif diceRoll == 2 and leftWidth + gapWidth < WIDTH - 1:
        gapWidth += 1  # increase gap width
    else:
        pass  # do nothing - no change in gap width
