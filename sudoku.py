#!/usr/bin/env python
#coding:utf-8

import sys
import time
import os
import copy
import statistics

"""
Each sudoku board is represented as a dictionary with string keys and
int values.
e.g. my_board['A1'] = 8
"""

ROW = "ABCDEFGHI"
COL = "123456789"


def print_board(board):
    """Helper function to print board in a square."""
    print("-----------------")
    for i in ROW:
        row = ''
        for j in COL:
            row += (str(board[i + j]) + " ")
        print(row)


def board_to_string(board):
    """Helper function to convert board dictionary to string for writing."""
    ordered_vals = []
    for r in ROW:
        for c in COL:
            ordered_vals.append(str(board[r + c]))
    return ''.join(ordered_vals)


def getDomain(board, var):
    domain = set(range(1, 10))

    for i in neighbors(var):
        if board[i] != 0:
            domain.discard(board[i])
    return domain

def SelectUnassigned(board):
    unassigned = dict()
    for i in board:
        if board[i] == 0:
            unassigned[i] = len(getDomain(board, i))
    mrv = min(unassigned, key=unassigned.get)
    return mrv


def neighbors(key):
    neighbors = set()
    for i in COL:
        neighbors.add(key[0] + i)
    for i in ROW:
        neighbors.add(i + key[1])
    chaRow = key[0]
    chaCol = key[1]
    rstart = chr(ord(chaRow) - (ord(chaRow) - 65) % 3)
    cstart = ord(chaCol) - (ord(chaCol) - 49) % 3
    for i in range(0, 3):
        chaRow = chr(ord(rstart) + i)
        for j in range(0, 3):
            chaCol = chr(cstart + j)
            neighbors.add(chaRow + chaCol)
    neighbors.discard(key)
    return neighbors

def isComplete(board):
    for key in board:
        if board[key] == 0:
            return False
    return True

def isConsistent(board, var, val):
    for element in neighbors(var):
        if board[element] == val:
            return False
    return True

def backtracking(board):
    """Takes a board and returns solved board."""
    if isComplete(board):
        return board
    var = SelectUnassigned(board)
    for value in getDomain(board, var):
        if isConsistent(board, var, value):
            board[var] = value
            if forwardChecking(board, var, value):
                if backtracking(board):
                    return board
            board[var] = 0

    return False

def forwardChecking(board, var, val):
    for element in neighbors(var):
        if val in getDomain(board, element):
            if len(getDomain(board, element)) == 1:
                return False
    return True

if __name__ == '__main__':
    #  Read boards from source.
    print("hello")
    if len(sys.argv) > 1:
        line = sys.argv[1]
        board = { ROW[r] + COL[c]: int(line[9*r+c])
                   for r in range(9) for c in range(9)}
        
        #print_board(board)
        start_time  = time.time()
        solved_board = backtracking(board)
        end_time = time.time()
        print("Program completed in %.3f second(s)"%(end_time-start_time))
        print_board(solved_board)
        with open("output.txt", "w") as f:
            f.write(board_to_string(solved_board))
        
    else:

        src_filename = 'sudokus_start.txt'
        try:
            srcfile = open(src_filename, "r")
            sudoku_list = srcfile.read()
        except:
            print("Error reading the sudoku file %s" % src_filename)
            exit()

        # Setup output file
        out_filename = 'README.txt'
        #outfile = open(out_filename, "w")
        # Solve each board using backtracking
        minTime = 1000
        maxTime = 0
        sample = []
        count = 0
        for line in sudoku_list.split("\n"):

            if len(line) < 9:
                continue

            # Parse boards to dict representation, scanning board L to R, Up to Down
            board = { ROW[r] + COL[c]: int(line[9*r+c])
                      for r in range(9) for c in range(9)}

            # Print starting board. TODO: Comment this out when timing runs.
            #print_board(board)

            # Solve with backtracking
            start_time  = time.time()
            solved_board = backtracking(board)
            end_time = time.time()
            count += 1
            # Print solved board. TODO: Comment this out when timing runs.
            #print_board(solved_board)
            #print("Program completed in %.3f second(s)"%(end_time-start_time))
            totalTime = end_time-start_time
            sample.append(totalTime)
            if totalTime < minTime:
                minTime = totalTime
            if totalTime > maxTime:
                maxTime = totalTime

            # Write board to file
            #outfile.write(board_to_string(solved_board))
            #outfile.write('\n')

        print("Finishing all boards in file.")
        mean = statistics.mean(sample)
        stdev = statistics.stdev(sample)
        with open("README.txt", "w") as f:
            f.write("Number of puzzles solved: " + str(count) + "\n")
            f.write("Min time to run puzzle: " + str(minTime) + "\n")
            f.write("Max time to run puzzle: " + str(maxTime) + "\n")
            f.write("Mean time for a run: " + str(mean) + "\n")
            f.write("Standard deviation: " + str(stdev) + "\n")
        



