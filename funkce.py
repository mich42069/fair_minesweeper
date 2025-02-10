import random

def new_game_grid(width, height, nmines): # generates bombs in game grid - 1 if bomb 0 if not bomb
    grid = [[0] * width for i in range(height)]
    notmine = []
    for y in range(height):
        for x in range(width):
            notmine.append((x, y))
    for i in range(nmines):
        newmine = random.choice(notmine)
        grid[newmine[1]][newmine[0]] = 1
        notmine.remove(newmine)
    return grid

def empty_grid(width, height): # generates 'empty' grid of None 
    grid = [[None] * width for i in range(height)]
    return grid

def is_in_grid(width, height, coords): # checks if the coordinates are on the grid to prevent later indexing errors
    if 0 <= coords[0] < width and 0 <= coords[1] < height:
        return True
    else:
        return False

def surrounding_cells(coords, grid): # generates a list of all surrounding cells
    surrounding_cell_list = []
    width = len(grid[0])
    height = len(grid)
    for x, y in [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]: # for x and y in 8 coordinates around like a donut
        new_cord_x = coords[0] + x
        new_cord_y = coords[1] + y
        if is_in_grid(width, height, (new_cord_x, new_cord_y)):
            surrounding_cell_list.append((new_cord_x, new_cord_y))
    return surrounding_cell_list

def cell_number(coords, grid): # creates the number of a cell based on the number of mines around it
    number = 0
    width = len(grid[0])
    height = len(grid)
    for x, y in [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]:
        check_x = coords[0] + x
        check_y = coords[1] + y
        if is_in_grid(width, height, (check_x, check_y)):
            if grid[check_y][check_x] == 1:
                number += 1
    return number

# it imputs a numbered grid - number if it is uncovered and None if it isnt, 
# uncovers surrounding cells around every '0' cell and returns back the numbered grid,
# uses helping list - seenlist, that knows which 0 cells already have their surrounding
# cells uncovered
def zero_chain(numberedgrid, grid, seenlist): 
    numberof0 = None
    while numberof0 != 0: # runs while there are new '0' cells uncovered every pass
        numberof0 = 0
        cell0 = []
        for y, row in enumerate(numberedgrid):                      # for every row
            for x, cell in enumerate(row):                          # for every cell in row
                if cell == 0 and (x, y) not in seenlist:            # for every 0 cell that isnt uncovered
                    for cells in surrounding_cells((x, y), grid):   # for every surrounding cell
                        number_of_cell = cell_number(cells, grid)
                        if number_of_cell == 0:                     # adds the new 0 cells to the list and repeats
                            numberof0 += 1
                            cell0.append(cells)
                        else:
                            numberedgrid[cells[1]][cells[0]] = number_of_cell
                    seenlist.append((x, y))
        for x, y in cell0:
            numberedgrid[y][x] = 0
    return(numberedgrid, seenlist)

def simple_filter(numberedgrid, grid, stepsgrid):
    for y, row in enumerate(numberedgrid):
        for x, cell in enumerate(row):
            if type(cell) == int and cell != 0:
                NoneCells = []
                FlagCells = []
                for coordsur in surrounding_cells((x, y), grid):
                    if numberedgrid[coordsur[1]][coordsur[0]] == None and stepsgrid[coordsur[1]][coordsur[0]] == None:
                        NoneCells.append((coordsur[0], coordsur[1]))
                        
                    elif numberedgrid[coordsur[1]][coordsur[0]] == 'fl' and grid[coordsur[1]][coordsur[0]] == 1 or stepsgrid[coordsur[1]][coordsur[0]] == True:
                        FlagCells.append((coordsur[0], coordsur[1]))
                        
                if len(NoneCells) + len(FlagCells) == cell:
                    for coordofmine in NoneCells:
                        stepsgrid[coordofmine[1]][coordofmine[0]] = True
                        
                if len(FlagCells) == cell:
                    for coordofnotmine in NoneCells:
                        stepsgrid[coordofnotmine[1]][coordofnotmine[0]] = False
    return stepsgrid

def complex_filter(numberedgrid, grid, stepsgrid):
    edgecells = [] # a list of all cells that have a number and also have uncovered cells around
    for y, row in enumerate(numberedgrid):
        for x, cell in enumerate(row):
            if type(cell) == int and cell != 0:
                if None in [numberedgrid[x[1]][x[0]] for x in surrounding_cells((x, y), grid)]:
                    edgecells.append((x, y))
    
    for edgecell in edgecells: # for every cell 
        surcells = [x for x in surrounding_cells(edgecell, grid) if x in edgecells] # creates a list of every surrounding edgecells
        sur_not_numbered = [x for x in surrounding_cells(edgecell, grid) if numberedgrid[x[1]][x[0]] == None and stepsgrid[x[1]][x[0]] == None] # and for all surrounding cells that havent been numbered and are not determined
        cell_found_number = len([x for x in surrounding_cells(edgecell, grid) if numberedgrid[x[1]][x[0]] == 'fl' or stepsgrid[x[1]][x[0]]]) # number of cells around that are uncovered or have known bombs
        cellnum = numberedgrid[edgecell[1]][edgecell[0]] - cell_found_number # hence the 'active' number of the cell is the number of the cell - the number of uncovered or known bombs around
        
        for surcell in surcells: # for every surrounding edgecell, creates the same mesurements
            sur_sur_not_numbered = [x for x in surrounding_cells(surcell, grid) if numberedgrid[x[1]][x[0]] == None and stepsgrid[x[1]][x[0]] == None]
            sur_cell_found_number = len([x for x in surrounding_cells(surcell, grid) if numberedgrid[x[1]][x[0]] == 'fl' or stepsgrid[x[1]][x[0]]])
            sur_cellnum = numberedgrid[surcell[1]][surcell[0]] - sur_cell_found_number
            
            sur_sur_only = [x for x in sur_sur_not_numbered if x not in sur_not_numbered]
            sur_only = [x for x in sur_not_numbered if x not in sur_sur_not_numbered]
            
            if sur_cellnum - cellnum == len(sur_sur_only): 
                for cell in sur_sur_only:
                    stepsgrid[cell[1]][cell[0]] = True
                for cell in sur_only:
                    stepsgrid[cell[1]][cell[0]] = False
    return stepsgrid
    
def is_there_next_step(numberedgrid, grid): # the function that calculates if there is a next step
    stepsgrid = empty_grid(len(grid[0]), len(grid))
    
    # the easy ones => number = uncovered mines
    stepsgrid = simple_filter(numberedgrid, grid, stepsgrid)
    
    # harder ones => usage of groups of surrounding squares
    stepsgrid = complex_filter(numberedgrid, grid, stepsgrid)
    
    # second pass of the easy filter with small changes, now knowing where cannot be mines due to the harder ones algorithm
    stepsgrid = simple_filter(numberedgrid, grid, stepsgrid)
    
    possible_step = False # if there is any possible step then it changes it to 1
    for row in stepsgrid:
        for cell in row:
            if cell != None:
                possible_step = True
                break
        if possible_step:
            break
    return possible_step, stepsgrid

def lostgame(numbered_grid, grid): # if game is lost uncoveres every mine and makes a wrongful flag for every wrong flag
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if numbered_grid[y][x] == 'fl' and cell == 0:
                numbered_grid[y][x] = 'f'
            if cell == 1 and numbered_grid[y][x] != 'c':
                numbered_grid[y][x] = 'm'
    return numbered_grid

def wongame(numbered_grid, grid): # if game is won uncoveres every mine and uncovers every covered cell
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == 1:
                numbered_grid[y][x] = 'm'
            else:
                numbered_grid[y][x] = cell_number((x, y), grid)
    return numbered_grid
