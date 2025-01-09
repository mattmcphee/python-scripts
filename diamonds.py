r"""Diamonds
Draws diamonds of various sizes.
"""


def main():
    print("Diamonds. Draws diamonds of different sizes.")

    # display diamonds of sizes 0 through 6
    for diamondSize in range(0, 40):
        displayOutlineDiamond(diamondSize)
        print()  # print a newline
        displayFilledDiamond(diamondSize)
        print()  # print a newline


def displayOutlineDiamond(size):
    # display the top half of the diamond
    for i in range(size):
        print(" " * (size - i - 1), end="")  # left side space
        print("/", end="")  # left side of diamond
        print(" " * (i * 2), end="")  # interior of diamond
        print("\\")  # right side of diamond
    # display the bottom half of the diamond
    for i in range(size):
        print(" " * i, end="")  # left side space
        print("\\", end="")  # left side of diamond
        print(" " * ((size - i - 1) * 2), end="")  # interior of diamond
        print("/")  # right side of diamond


def displayFilledDiamond(size):
    # display the top half of the diamond
    for i in range(size):
        print(" " * (size - i - 1), end="")  # left side space
        print("/" * (i + 1), end="")  # left half of diamond
        print("\\" * (i + 1))  # right half of diamond
    # display the bottom half of the diamond
    for i in range(size):
        print(" " * i, end="")  # left side space
        print("\\" * (size - i), end="")  # left side of diamond
        print("/" * (size - i))  # right side of diamond


# if this program was run (instead of imported), run the game
if __name__ == "__main__":
    main()
