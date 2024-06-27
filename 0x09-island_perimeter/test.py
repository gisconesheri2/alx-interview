def island_perimeter(grid):
    if len(grid) > 100 or len(grid[0]) > 100:
        print('grid size exceeded')
        return
    if 1 in grid[0] or 1 in grid[len(grid) -1 ]:
        print('grid is not an island')
        return
    
    total_sum = 0
    prev_indexes = []
    prev_zero_indexes = []
    for r in range(1, len(grid) -1 ):
        row = grid[r]
        next_row = grid[r+1]
        if row[0] == 1 or row[len(row)- 1] == 1:
            print('first column and last column has no water')
            return
        
        indexes_one_found = []
        indexes_zero_found = []
        row_sum = 0
        prev_row_sub = 0
        for idx in range(1, len(row) -1 ):
            if len(prev_indexes) == 0 and total_sum != 0 and 1 in row:
                print('grid must have onle one island')
                return
            if row[idx] == 1:
                if len(indexes_one_found) == 0:
                    idx_sum = 4
                else:
                    idx_sum = 2
                indexes_one_found.append(idx)
                row_sum += idx_sum
            
                if idx in prev_indexes:
                    prev_row_sub += 2
            if row[idx] == 0:
                indexes_zero_found.append(idx)
        
        # for pos in range(len(indexes_one_found) - 1):
        #     crid = indexes_one_found[pos + 1] - indexes_one_found[pos]
        #     prid = prev_indexes[pos + 1] - prev_indexes[pos] 
        #     if crid > 1:
        #         print('no water in island')
        #         return

        for pos in indexes_zero_found:
            if pos in prev_zero_indexes:
                continue
            if pos in prev_indexes:
                if pos-1 in prev_indexes and pos+1 in prev_indexes and pos+1 in indexes_one_found:
                    print('no lakes')
                    return
                if pos-1 in indexes_one_found and pos+1 in indexes_one_found and next_row[pos] == 1:
                    print('no lake, ones all around')
                    return
                if pos+1 in prev_zero_indexes and pos -1 in indexes_zero_found and pos+1 in indexes_one_found:
                    print('no verticals 0 based')
                    return
        for pos in indexes_one_found:
            if pos in prev_zero_indexes and pos-1 in indexes_zero_found and (pos+1 in indexes_zero_found):
                print('no  vertical connections')
                return


        print(indexes_one_found)
        prev_indexes = indexes_one_found
        prev_zero_indexes = indexes_zero_found
        indexes_one_found = []
        row_sum -= prev_row_sub
        total_sum += row_sum
    print(total_sum)
        
grid = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]

island_perimeter(grid=grid)
for row in grid:
    print(row)