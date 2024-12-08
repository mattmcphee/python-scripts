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
    print(("#" * leftWidth) + (" " * gapWidth) + ("#" * rightWidth))

    # check for ctrl+c press during the brief pause
    try:
        time.sleep(PAUSE_AMOUNT)
    except KeyboardInterrupt:
        sys.exit()  # when ctrl+C is pressed, end the program

    # adjust the left side width
    diceRoll = random.randint(1, 6)
    if diceRoll == 1 and leftWidth > 1:
        leftWidth -= 1
