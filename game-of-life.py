import copy, random, sys, time

# set up the constants
WIDTH = 79
HEIGHT = 20

ALIVE = "O"
DEAD = " "

# cells and nextCells are dictionaries for the state of the game
# keys are (col, row) tuples
nextCells = {}
# put random dead and alive cells into nextCells
for col in range(WIDTH):  # loop over every possible column
    for row in range(HEIGHT):  # loop over every possible row
        # 50/50 chance for starting cells being alive or dead
        if random.randint(0, 1) == 0:
            nextCells[(col, row)] = ALIVE  # add a living cell
        else:
            nextCells[(col, row)] = DEAD  # add a dead cell

while True:  # main program loop
    # each loop is a step of the simulation
    print("\n" * 50)  # separate each step with newlines
    cells = copy.deepcopy(nextCells)
    # print cells on the screen
    for row in range(HEIGHT):
        for col in range(WIDTH):
            print(cells[(col, row)], end="")  # print the | or -
        print()  # print a newline at the end of the row
    # print("Press Ctrl+C to quit.")

    # calculate the next step's cells based on current step's cells
    for col in range(WIDTH):
        for row in range(HEIGHT):
            # get the neighbouring coordinates of (col, row) even if they
            # wrap around the edge
            left = (col - 1) % WIDTH
            right = (col + 1) % WIDTH
            above = (row - 1) % HEIGHT
            below = (row + 1) % HEIGHT

            # count the number of living neighbours
            numNeighbours = 0
            if cells[(left, above)] == ALIVE:
                numNeighbours += 1  # top left neighbour is alive
            if cells[(col, above)] == ALIVE:
                numNeighbours += 1  # top neighbour is alive
            if cells[(right, above)] == ALIVE:
                numNeighbours += 1  # top right neighbour is alive
            if cells[(left, row)] == ALIVE:
                numNeighbours += 1  # left neighbour is alive
            if cells[(right, row)] == ALIVE:
                numNeighbours += 1  # right neighbour is alive
            if cells[(left, below)] == ALIVE:
                numNeighbours += 1  # bottom left neighbour is alive
            if cells[(col, below)] == ALIVE:
                numNeighbours += 1  # bottom neighbour is alive
            if cells[(right, below)] == ALIVE:
                numNeighbours += 1  # bottom right neighbour is alive

            # set cell based on game of life rules
            if cells[(col, row)] == ALIVE and (
                numNeighbours == 2 or numNeighbours == 3
            ):
                # living cells with 2 or 3 neighbours stay alive
                nextCells[(col, row)] = ALIVE
            elif cells[(col, row)] == DEAD and numNeighbours == 3:
                # dead cells with 3 neighbours become alive
                nextCells[(col, row)] = ALIVE
            else:
                # everything else dies or stays dead
                nextCells[(col, row)] = DEAD

    try:
        time.sleep(0.2)  # add a 1 second pause to reduce flickering
    except KeyboardInterrupt:
        print()
        print("Game of Life")
        sys.exit()  # when Ctrl+C is pressed, end the program
