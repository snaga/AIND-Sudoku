# -*- coding: utf-8 -*-

assignments = []

def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """

    # Find all instances of naked twins
    # Eliminate the naked twins as possibilities for their peers

rows = 'ABCDEFGHI'
cols = '123456789'

def cross(a, b):
    "Cross product of elements in A and elements in B."
    return [s+t for s in a for t in b]

boxes = cross(rows, cols)

row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
unitlist = row_units + column_units + square_units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)

def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    values = [x if x != '.' else '123456789' for x in grid]
    return dict(zip(boxes, values))

def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return

def eliminate(values):
    """Eliminate values from peers of each box with a single value.

    Go through all the boxes, and whenever there is a box with a single value,
    eliminate this value from the set of values of all its peers.

    Args:
        values: Sudoku in dictionary form.
    Returns:
        Resulting Sudoku in dictionary form after eliminating values.
    """
    # 各ユニット内で確定している数字を除く。
    values_new = values.copy()
    for box in boxes:
        units = [u for u in unitlist if box in u]
        for unit in units:
            elims = [values[x] for x in unit if len(values[x]) == 1 and x != box]
            for e in elims:
                values_new[box] = values_new[box].replace(e, '')
    values = values_new.copy()
    return values

def trace(s):
    #print (s)
    pass

import sys

def only_choice(values):
    """Finalize all values that are the only choice for a unit.

    Go through all the units, and whenever there is a unit with a value
    that only fits in one box, assign the value to this box.

    Input: Sudoku in dictionary form.
    Output: Resulting Sudoku in dictionary form after filling in only choices.
    """
    # 各ユニット内で1ヵ所にしか候補が無い数字を確定させる。
    # TODO: Implement only choice strategy here
    values2 = values.copy()
    for box in boxes:
        trace("box: %s" % box)
        # boxの属するunitを探す
        units = [u for u in unitlist if box in u]
        for unit in units:
            trace("unit: %s" % unit)
            # peerに出てくる候補の数字をすべて連結する
            all = ''.join([values[p] for p in unit])
            trace("all: %s" % all)
            # 候補の数字のunit内での出現回数を調べ、1回だけ候補になっている数字を取得する
            only_chars = list(set([ch for ch in all if all.count(ch) == 1]))
            trace("only_chars: %s" % only_chars)
            for ch in only_chars:
                for b in unit:
                    if ch in values[b] and b != box:
                        values2[b] = ch
                        trace("set %s, %s => %s" % (b, values[b], ch))
    values = values2.copy()
#    display(values)
    return values

def reduce_puzzle(values):
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        # Your code here: Use the Eliminate Strategy
        values = eliminate(values)
        # Your code here: Use the Only Choice Strategy
        values = only_choice(values)
        # Check how many boxes have a determined value, to compare
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        # If no new values were added, stop the loop.
        stalled = solved_values_before == solved_values_after
        # Sanity check, return False if there is a box with zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values

def search(values):
    "Using depth-first search and propagation, create a search tree and solve the sudoku."
    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)
    if values is False:
        return False
    # すべてのboxの値が確定している場合
    if all(len(values[s]) == 1 for s in boxes):
        return values

    # Choose one of the unfilled squares with the fewest possibilities
    # 複数の候補があるboxについて、候補数が最も少ないbox（と長さ）を取得する
    # s:box名, n:候補数
    s,n = min((s, len(values[s])) for s in boxes if len(values[s]) > 1)

    # Now use recursion to solve each one of the resulting sudokus, and if one returns a value (not False), return that answer!
    # boxの候補を1つに固定して再帰で探索。解が見つかったら返す。
    for value in values[s]:
        attempt_values = values.copy()
        attempt_values[s] = value
        attempt = search(attempt_values)
        if attempt:
            return attempt
    # If you're stuck, see the solution.py tab!
    # 解が見つからなかった場合
    return False

def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """

if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
