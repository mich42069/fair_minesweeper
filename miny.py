import pygame
from os import chdir
from funkce import *
import time
path = "C:/Users/lachi/OneDrive - Univerzita Karlova/Plocha/school/Cvika/Program Cvika/zapocet python done/Miny"
chdir(path)

pygame.init()
pygame.font.init()

# Visual import
spr_grid = {} # sprites with nonmine related tiles are saved as a dictionary 0-8
miny = {} # sprites of mine related tiles are saved as a dictionary
spr_emptyGrid = pygame.image.load("empty.png")
spr_darkGrid = pygame.image.load("darkgrid.png")
spr_grid[0] = pygame.image.load("grid0.png")
spr_grid[1] = pygame.image.load("grid1.png")
spr_grid[2] = pygame.image.load("grid2.png")
spr_grid[3] = pygame.image.load("grid3.png")
spr_grid[4] = pygame.image.load("grid4.png")
spr_grid[5] = pygame.image.load("grid5.png")
spr_grid[6] = pygame.image.load("grid6.png")
spr_grid[7] = pygame.image.load("grid7.png")
spr_grid[8] = pygame.image.load("grid8.png")
miny['fl'] = pygame.image.load("flag.png")
miny['m'] = pygame.image.load("mine.png")
miny['c'] = pygame.image.load("mineClicked.png")
miny['f'] = pygame.image.load("mineFalse.png")

# Parameters

topbar = 80
sidebar = 16
cellsize = 32
game_on = True
fps = 30
gamefont = pygame.font.SysFont('Times New Roman', 80)
optionsfont = pygame.font.SysFont('Arial', 64, True)
topfont = pygame.font.SysFont('mspgothic', 40)
framerate = pygame.time.Clock()

def parameters():
    # a function that reads text and allows us to write measurements
    def choosewhat(what):
        for row in range(parameters_display_height):
            for col in range(parameters_display_width):
                parameters_display.blit(spr_darkGrid, pygame.Rect(cellsize*col, cellsize*row, cellsize, cellsize))
        
        text = gamefont.render(what, 1, pygame.Color('white'))
        parameters_display.blit(text, pygame.Rect(cellsize, cellsize, cellsize*3, cellsize*2))
        choosing = True
        chosen = ''
        while choosing:
            framerate.tick(fps)
            text = gamefont.render(chosen, 1, pygame.Color('white'))
            parameters_display.blit(text, pygame.Rect(cellsize*2, cellsize*9//2, cellsize*3, cellsize*2))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    choosing = False
                if event.type == pygame.KEYDOWN:
                    if event.key == 13: # code for enter
                        return int(chosen)
                    if len(chosen) < 3: # must be smaller than 3 so that it isnt too big of a number
                        if event.key in range(1073741913, 1073741923): # since event.key is in order we can just have this instead of 10 different if statements
                            chosen += str(event.key - 1073741912)[-1]
                        elif event.key in range(48, 58): # same as above but not numboard
                            chosen += str(event.key - 48)
                    if event.key == 8: # code for backspace
                        chosen = chosen[0:-1]
                        for row in range(4,9):
                            for col in range(0,7):
                                parameters_display.blit(spr_darkGrid, pygame.Rect(cellsize*col, cellsize*row, cellsize, cellsize))

    def randomgame(): # decides random parameters
        width = random.randint(9, 32)
        height = random.randint(9, 24)
        nmines = round(width * height * random.randint(2, 17) / 100)

        return height, width, nmines
    
    def easy(): # decides easy parameters
        width = 9
        height = 9
        nmines = 10

        return height, width, nmines
        
    def medium(): # decides medium parameters
        width = 16
        height = 16
        nmines = 40

        return height, width, nmines
    
    def hard(): # decides hard parameters
        width = 30
        height = 20
        nmines = 99

        return height, width, nmines
        
    def custom(): # allows player to customize the game field
        width = choosewhat('Choose width')
        while width == 0: # makes sure that width isnt 0
            width = choosewhat('Choose width')
                
        height = choosewhat('Choose height')
        while height == 0: # makes sure that height isnt 0
            height = choosewhat('Choose height')
        
        nmines = choosewhat('Number of Mines')
        while nmines > height*width: # makes sure there arent more bombs than free spaces
            nmines = choosewhat('Number of Mines')

        return height, width, nmines
        
    def choose_gamemode():
        pygame.display.set_caption('Choose game parameters')
        
        for row in range(parameters_display_height):
            for col in range(parameters_display_width):
                parameters_display.blit(spr_grid[0], pygame.Rect(cellsize*col, cellsize*row, cellsize, cellsize))
        
        #draws the options while creating clickable rectangles
        
        easy_rect = pygame.Rect(cellsize, cellsize, (parameters_display_width-4*cellsize)//3, cellsize*3)
        medium_rect = pygame.Rect((parameters_display_width-4*cellsize)//3 + 2*cellsize, cellsize, (parameters_display_width-4*cellsize)//3, cellsize*3)
        hard_rect = pygame.Rect((parameters_display_width-4*cellsize)//3*2 + 3*cellsize, cellsize, (parameters_display_width-4*cellsize)//3, cellsize*3)
        random_rect = pygame.Rect(cellsize, 5*cellsize, (parameters_display_width-3*cellsize)//2, cellsize*3)
        custom_rect = pygame.Rect((parameters_display_width-3*cellsize)//2 + 2*cellsize, 5*cellsize, (parameters_display_width-3*cellsize)//2, cellsize*3)
        
        easy_rect_co = [1, 1, (parameters_display_width//cellsize-4)//3, 3]
        medium_rect_co = [(parameters_display_width//cellsize-4)//3 + 2, 1, (parameters_display_width//cellsize-4)//3, 3]
        hard_rect_co = [(parameters_display_width//cellsize-4)//3*2 + 3, 1, (parameters_display_width//cellsize-4)//3, 3]
        random_rect_co = [1, 5, (parameters_display_width//cellsize-3)//2, 3]
        custom_rect_co = [(parameters_display_width//cellsize-3)//2 + 2, 5, (parameters_display_width//cellsize-3)//2, 3]
        
        for rect in [easy_rect_co, medium_rect_co, hard_rect_co, random_rect_co, custom_rect_co]:
            for col in range(rect[2]):
                for row in range(rect[3]):
                    parameters_display.blit(spr_emptyGrid, pygame.Rect(rect[0] * cellsize + cellsize * col, rect[1] * cellsize + cellsize * row, cellsize, cellsize))
                
        # text so that player knows whats happening
        text = optionsfont.render('EASY', 1, pygame.Color('black'))
        parameters_display.blit(text, easy_rect)
        text = optionsfont.render('MEDIUM', 1, pygame.Color('black'))
        parameters_display.blit(text, medium_rect)
        text = optionsfont.render('HARD', 1, pygame.Color('black'))
        parameters_display.blit(text, hard_rect)
        text = optionsfont.render('RANDOM', 1, pygame.Color('black'))
        parameters_display.blit(text, random_rect)
        text = optionsfont.render('CUSTOM', 1, pygame.Color('black'))
        parameters_display.blit(text, custom_rect)
        
        pygame.display.flip()
        # runs the loop
        
        choosing = True
        while choosing:
            framerate.tick(fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    choosing = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        for e, rect in enumerate([easy_rect, medium_rect, hard_rect, random_rect, custom_rect]):
                            if rect.collidepoint(event.pos):
                                if e == 0:
                                    return easy()
                                if e == 1:
                                    return medium()
                                if e == 2:
                                    return hard()
                                if e == 3:
                                    return randomgame()
                                if e == 4:
                                    return custom()
                    
        
    parameters_display_height = 9 * cellsize
    parameters_display_width = 25 * cellsize
    parameters_display = pygame.display.set_mode((parameters_display_width, parameters_display_height))
    
    height, width, nmines = choose_gamemode()
    return height, width, nmines

def start_game(height, width, nmines):
    global grid                 # a grid with 0 / 1 reffering to bombs
    global uncovered_grid       # a grid of what the player can see [0,9], flag, bomb, wrongflag, clickedbomb
    global seenlist             # list of 0 squares from uncovered grid that have already been seen by the 0clearing function
    global game_window          # game window
    global time0
    global won
    global lost
    pygame.display.set_caption('Good Luck!')
    won = lost = False
    grid = new_game_grid(width, height, nmines)
    time0 = round(time.time(), 0)
    uncovered_grid = empty_grid(width, height)
    seenlist = []
    window_width = game_width*cellsize + sidebar*2
    window_height = game_height*cellsize + topbar + sidebar
    
    # the following draws the game window and its shadows
    game_window = pygame.display.set_mode((window_width, window_height))
    pygame.draw.rect(game_window, (255, 255, 255), pygame.Rect(0, 0, window_width, window_height))
    pygame.draw.rect(game_window, (125, 125, 125), pygame.Rect(4, 4, window_width - 4, window_height - 4))
    pygame.draw.rect(game_window, (189, 189, 189), pygame.Rect(4, 4, window_width - 8, window_height - 8))
    pygame.draw.rect(game_window, (125, 125, 125), pygame.Rect(12, 12, window_width - 24, topbar - 24))
    pygame.draw.rect(game_window, (255, 255, 255), pygame.Rect(16, 16, window_width - 28, topbar - 28))
    pygame.draw.rect(game_window, (189, 189, 189), pygame.Rect(16, 16, window_width - 32, topbar - 32))
    pygame.draw.rect(game_window, (125, 125, 125), pygame.Rect(12, topbar -4, window_width - 24, window_height - topbar - sidebar + 8))
    pygame.draw.rect(game_window, (255, 255, 255), pygame.Rect(16, topbar, window_width - 28, window_height - topbar - sidebar + 4))
    pygame.draw.rect(game_window, (0, 0, 0), pygame.Rect(20, 20, 80, topbar - 40))
    pygame.draw.rect(game_window, (0, 0, 0), pygame.Rect(window_width - 100, 20, 80, topbar - 40))
    
    # the following draws the emoji at the top
    pygame.draw.rect(game_window, (255, 255, 0), pygame.Rect(window_width // 2 - 20, 20, 40, topbar - 40))
    text = topfont.render(':I', 1, pygame.Color('black'))
    game_window.blit(text, pygame.Rect(window_width//2 - 20, 20, 80, 30))

def draw_frame(game_window, uncovered_grid, cellsize):
    # time
    if not lost and not won:
        pygame.draw.rect(game_window, (0, 0, 0), pygame.Rect(20, 20, 80, topbar - 40))
        text = topfont.render(str(int(round(time.time(), 0) - time0)), 1, pygame.Color('red'))
        game_window.blit(text, pygame.Rect(20, 20, 80, 30))
    
    # number of mines remaining
    pygame.draw.rect(game_window, (0, 0, 0), pygame.Rect(game_width*cellsize + sidebar*2 - 100, 20, 80, topbar - 40))
    text = topfont.render(str(players_mines), 1, pygame.Color('red'))
    game_window.blit(text, pygame.Rect(game_width*cellsize + sidebar*2 - 100, 20, 80, 30))
    
    if won == True:
        pygame.draw.rect(game_window, (0, 255, 0), pygame.Rect(game_width*cellsize // 2 - 20 + sidebar, 20, 40, topbar - 40))
        text = topfont.render(':D', 1, pygame.Color('black'))
        game_window.blit(text, pygame.Rect(game_width*cellsize // 2 - 20 + sidebar, 20, 80, 30))
    elif lost == True:
        pygame.draw.rect(game_window, (255, 0, 0), pygame.Rect(game_width*cellsize // 2 - 20 + sidebar, 20, 40, topbar - 40))
        text = topfont.render(':(', 1, pygame.Color('black'))
        game_window.blit(text, pygame.Rect(game_width*cellsize // 2 - 20 + sidebar, 20, 80, 30))
    
    ### this section draws every tile on the grid ###
    
    for y, row in enumerate(uncovered_grid):
        for x, cell in enumerate(row):
            if type(cell) == int:
                game_window.blit(spr_grid[cell], pygame.Rect(x*cellsize + sidebar, y*cellsize + topbar, cellsize, cellsize))
            elif type(cell) == str:
                game_window.blit(miny[cell], pygame.Rect(x*cellsize + sidebar, y*cellsize + topbar, cellsize, cellsize))
            else:
                game_window.blit(spr_emptyGrid, pygame.Rect(x*cellsize + sidebar, y*cellsize + topbar, cellsize, cellsize))

#starting game
game_height, game_width, number_of_mines = parameters()
players_mines = number_of_mines
real_mines = number_of_mines
start_game(game_height, game_width, number_of_mines)
possible_step, possibles_grid = is_there_next_step(uncovered_grid, grid)

while game_on:
    framerate.tick(fps)
    draw_frame(game_window, uncovered_grid, cellsize) # draws the frame
    pygame.display.flip()
    for event in pygame.event.get(): # checks for input every frame
        if event.type == pygame.QUIT: # end game call
            game_on = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                start_game(game_height, game_width, number_of_mines)
                players_mines = number_of_mines
                real_mines = number_of_mines
                possible_step, possibles_grid = is_there_next_step(uncovered_grid, grid)
                
            if event.key == pygame.K_c: # makes the game easy by automatically clickin on the known cells for the player
                for y, row in enumerate(possibles_grid):
                    for x, cell in enumerate(row):
                        if cell:
                            uncovered_grid[y][x] = 'fl'
                            players_mines -= 1
                            real_mines -= 1
                        elif cell == False:
                            uncovered_grid[y][x] = cell_number((x, y), grid)
                uncovered_grid, seenlist = zero_chain(uncovered_grid, grid, seenlist)
                possible_step, possibles_grid = is_there_next_step(uncovered_grid, grid)
            
        if not lost and not won: # only lets us use mouse if the game didnt end
            if event.type == pygame.MOUSEBUTTONUP:
                # finds the position where the player clicked
                x, y = pygame.mouse.get_pos()
                if x < sidebar or y < topbar:
                    continue
                x -= sidebar
                y -= topbar
                col = x // cellsize
                row = y // cellsize
                if col >= game_width or row >= game_height:
                    continue
                
                if event.button == 1: # left mouse button
                    if uncovered_grid[row][col] == None: # only procceeds if we clicked on uncovered square
                        if possible_step: # if there is a possible step to take
                            if possibles_grid[row][col] == False: # if the cell we clicked on was one of the possible steps
                                uncovered_grid[row][col] = cell_number((col, row), grid)
                                
                            else:
                                uncovered_grid[row][col] = 'c'
                                lost = True
                                uncovered_grid = lostgame(uncovered_grid, grid)
                                
                        else: # if there arent any sure steps to take (player has to guess)
                            if grid[row][col] == 0:
                                uncovered_grid[row][col] = cell_number((col, row), grid)
                                
                            else: # if there was a mine on the guessed square the mine is removed and any surrounding numbers are substracted by one
                                    grid[row][col] = 0
                                    real_mines -= 1
                                    players_mines -= 1
                                    uncovered_grid[row][col] = cell_number((col, row), grid)
                                    
                                    for surrounding in surrounding_cells((col, row), grid):
                                        if type(uncovered_grid[surrounding[1]][surrounding[0]]) == int:
                                            uncovered_grid[surrounding[1]][surrounding[0]] -= 1
                                            
                        uncovered_grid, seenlist = zero_chain(uncovered_grid, grid, seenlist)

                elif event.button == 3: # adressess flag placement
                    if uncovered_grid[row][col] == None:
                        uncovered_grid[row][col] = 'fl'
                        players_mines -= 1
                        if grid[row][col] == 1:
                            real_mines -= 1
                    elif uncovered_grid[row][col] == 'fl':
                        uncovered_grid[row][col] = None
                        players_mines += 1
                        if grid[row][col] == 1:
                            real_mines += 1
                
                # at the end of the click it calculates if there are any new steps possible
                possible_step, possibles_grid = is_there_next_step(uncovered_grid, grid)
                #print(possible_step)
                
    number_of_remaining_uncovered = 0 # counting still covered cells
    for y, row in enumerate(uncovered_grid):
        for x, cell in enumerate(row):
            if cell == None:
                number_of_remaining_uncovered += 1
    # if the number of remaining mines is equal to zero, and only the real mines are under flags
    # or
    # the number of remaining squares are all mines and no badly placed flags are present
    if (real_mines == 0 and 0 == players_mines) or (number_of_remaining_uncovered == real_mines and players_mines == real_mines):
        won = True
        uncovered_grid = wongame(uncovered_grid, grid)

pygame.quit()