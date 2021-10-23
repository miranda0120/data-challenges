def sudoku_validator(grid):
    if not grid:
        return False

    #rows by rows checking
    row = set()
    for i in range(9):
        for j in range(9):
            if grid[i][j] in row:
                return False
            else:
                row.add(grid[i][j])
        row = set()

    #cols by cols checking
    row = set()
    for i in range(9):
        for j in range(9):
            if grid[j][i] in row:
                return False
            else:
                row.add(grid[j][i])
        row = set()

    # 3 by 3 check
    subs = [range(0,3), range(3,6), range(6,9)]
    subgrids = []
    for x in subs:
        for y in subs:
            subgrids.append([x,y])
    for (row_range, column_range) in subgrids:
        row = set()
        for i in row_range:
            for j in column_range:
                if grid[i][j] in row:
                    return False
                else:
                    row.add(grid[i][j])
    return True
