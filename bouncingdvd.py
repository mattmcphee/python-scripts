import sys, random, time

try:
    import bext
except ImportError:
    print("This program requires the bext module, which you can install by")
    print("following the instructions at https://pypi.org/project/bext/")
    sys.exit()

# set up the constants
WIDTH, HEIGHT = bext.size()
# we can't print to the last column on Windows without it adding a
# newline automatically, so reduce the width by one
WIDTH -= 1
WIDTH_OFFSET = 4
NUMBER_OF_LOGOS = 5
PAUSE_AMOUNT = 0.1
COLORS = ["red", "green", "yellow", "blue", "magenta", "cyan", "white"]
UP_RIGHT = "ur"
UP_LEFT = "ul"
DOWN_RIGHT = "dr"
DOWN_LEFT = "dl"
DIRECTIONS = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)

# key names for logo dictionaries
COLOR = "color"
X = "x"
Y = "y"
DIR = "direction"


def main():
    bext.clear()

    # generate some logos
    logos = []
    for i in range(NUMBER_OF_LOGOS):
        logos.append(
            {
                COLOR: random.choice(COLORS),
                X: random.randint(1, WIDTH - 4),
                Y: random.randint(1, HEIGHT - 4),
                DIR: random.choice(DIRECTIONS),
            }
        )
        if logos[-1][X] % 2 == 1:
            # make sure X is even so it can hit the corner
            logos[-1][X] -= 1
    cornerBounces = 0  # count how many times a logo hits a corner
    while True:  # main program loop
        for logo in logos:  # handle each logo in the logos list
            # erase the logo's current location
            bext.goto(logo[X], logo[Y])
            print("   ", end="")
            originalDirection = logo[DIR]

            # see if the logo bounces off the corners
            # WIDTH - 3 because DVD has 3 letters
            if logo[X] == 0 and logo[Y] == 0:
                logo[DIR] = DOWN_RIGHT
                cornerBounces += 1
            elif logo[X] == 0 and logo[Y] == HEIGHT - 1:
                logo[DIR] = UP_RIGHT
                cornerBounces += 1
            elif logo[X] == WIDTH - WIDTH_OFFSET and logo[Y] == 0:
                logo[DIR] = DOWN_LEFT
                cornerBounces += 1
            elif logo[X] == WIDTH - WIDTH_OFFSET and logo[Y] == HEIGHT - 1:
                logo[DIR] = UP_LEFT
                cornerBounces += 1

            # see if the logo bounces off the left edge
            elif logo[X] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = UP_RIGHT
            elif logo[X] == 0 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = DOWN_RIGHT

            # see if the logo bounces off the right edge
            elif logo[X] == WIDTH - WIDTH_OFFSET and logo[DIR] == UP_RIGHT:
                logo[DIR] = UP_LEFT
            elif logo[X] == WIDTH - WIDTH_OFFSET and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = DOWN_LEFT

            # see if the logo bounces off the top edge
            elif logo[Y] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = DOWN_LEFT
            elif logo[Y] == 0 and logo[DIR] == UP_RIGHT:
                logo[DIR] = DOWN_RIGHT

            # see if the logo bounces off the bottom edge
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = UP_LEFT
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = UP_RIGHT

            # change color when the logo bounces
            if logo[DIR] != originalDirection:
                logo[COLOR] = random.choice(COLORS)

            # move the logo
            # X moves by 2 because the terminal characters are twice as tall
            # as they are wide
            if logo[DIR] == UP_RIGHT:
                logo[X] += 2
                logo[Y] -= 1
            elif logo[DIR] == UP_LEFT:
                logo[X] -= 2
                logo[Y] -= 1
            elif logo[DIR] == DOWN_RIGHT:
                logo[X] += 2
                logo[Y] += 1
            elif logo[DIR] == DOWN_LEFT:
                logo[X] -= 2
                logo[Y] += 1

        # display number of corner bounces
        bext.goto(5, 0)
        bext.fg("white")
        print("Corner bounces:", cornerBounces, end="")

        for logo in logos:
            # draw the logos at their location
            bext.goto(logo[X], logo[Y])
            bext.fg(logo[COLOR])
            print("DVD", end="")

        bext.goto(0, 0)

        sys.stdout.flush()  # required when using bext
        time.sleep(PAUSE_AMOUNT)


# if this program was run instead of imported, run the game
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        print("Bouncing DVD Logo")
        sys.exit()  # when ctrl+c is pressed, end the program
