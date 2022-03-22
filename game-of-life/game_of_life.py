# Game of Life
# Hannah Mae Nicole I. Rosete

import os
import time
import keyboard
import random
import csv


def random_30x30_2D_world(grid):
    '''Generates random 30x30 2D World'''

    rows = 30
    columns = 30

    for _ in range(rows):
        line = []
        for _ in range(columns):
            line.append(random.randint(0, 1))
        grid.append(line)

    return grid


def load_2D_array(filename, grid):
    '''Load 2D world from the csv file to the grid.
    Data in CSV is 10x10 for now'''

    output_file = csv.reader(open(filename, "r"), delimiter=",")
    matrix = list(output_file)

    # Converts every item in the matrix from str to int
    for row in matrix:
        line = []
        for item in row:
            line.append(int(item))
        grid.append(line)

    '''Debug Statements'''
    # print(matrix)
    # print(grid)

    return grid


def print_2D_world(grid):
    '''Prints Black and White (Dead and Alive) blocks
    to the Terminal'''

    for row in grid:
        for column in row:
            if column == 1:  # Prints white block if Alive
                print(u"\u2B1C", end="")
            else:  # Prints black background
                print(u"\u2B1B", end="")
        print()


def neighbors_sum(grid, row, column):
    '''Count the neighbors around the cell'''
    # row = current row of the cell being analyzed
    # column = current column of the cell being analyzed
    # i = offset in row (-1 or +1)
    # j = offset in columns (-1 or +1)

    sum = 0

    # Counts the cell's neighbors in it's 9x9 matrix/grid
    for i in range(-1, 2):
        for j in range(-1, 2):

            # If on the edge, takes the last cell on the row/column
            row_wrap = (row + i + len(grid)) % len(grid)
            column_wrap = (column + j + len(grid[row])) % len(grid[row])
            sum += grid[row_wrap][column_wrap]

            # print("Currently at:", row, column, i, j)
            # print("Adding...", grid[row_wrap][column_wrap])
            # print("Sum:", sum)

    sum -= grid[row][column]  # Minus the cell's own state from the sum

    return sum


def conditions_for_next_state(old_grid, new_grid):
    '''Conditions for the next generation'''
    # i = current row in grid
    # j = current column in row

    for i in range(0, len(old_grid)):
        new_row = []

        for j in range(0, len(old_grid[i])):

            cell_state = old_grid[i][j]
            neighbors = neighbors_sum(old_grid, i, j)
            # print("Currently at:", i, j)
            # print("Cell State:", cell_state)
            # print("Neighbors' count around the cell:", neighbors)

            if (cell_state == 0 and neighbors == 3):
                new_row.append(1)
            elif (cell_state == 1 and (neighbors < 2 or neighbors > 3)):
                new_row.append(0)
            elif (cell_state == 1 and (neighbors == 2 or neighbors == 3)):
                new_row.append(cell_state)
            else:
                new_row.append(cell_state)
        new_grid.append(new_row)

    return new_grid


def main():

    current_state = []
    new_state = []

    have_file = input("Do you have a CSV file? (y/n) ")
    if have_file == "y" or have_file == "Y":
        ''' Loads the 2D array world from the CSV file to current_state'''
        file = input("Enter filename: ")
        load_2D_array(file, current_state)
    elif have_file == "n" or have_file == "N":
        '''Generates a 30x30 Array for the 2D World to the Current State'''
        random_30x30_2D_world(current_state)

    try:
        counter = 0
        while True:
            os.system("CLS")  # Clears the screen
            counter += 1
            print_2D_world(current_state)
            print("Generation", counter)
            conditions_for_next_state(current_state, new_state)
            current_state = new_state
            new_state = []

            if keyboard.is_pressed("space"):
                print("Simulation paused...")
                keyboard.wait("space")

            time.sleep(0.2)
    except KeyboardInterrupt:
        print("KeyboardInterrupt has been caught. Simulation halted.")


if __name__ == "__main__":
    main()
