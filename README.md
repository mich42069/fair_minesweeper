# Minesweeper  

Implementation of the classic game Minesweeper with "fairness" functionality.  

**Fairness** means that two new rules are added:  
1. If the player has no 100% certainty about any cell, then no matter where they click, there will never be a bomb.  
2. If the player does have 100% certainty about some cell and chooses to click elsewhere, then that cell will always contain a bomb, and the player loses.  

---

## How to Play  
When the game starts, a window with parameter selection opens, where the player can choose a difficulty.  
After selecting, the game automatically launches in a new window.  

When selecting **custom**, the player is offered the option to set their own parameters. These must be natural numbers in the range **1–999**, confirmed by pressing **ENTER**.  

- **Left mouse button** → reveal a mine  
- **Right mouse button** → place a flag  
- **R key** → restart the game at the current difficulty  
- **C key** → evaluate all cells where the existence or non-existence of a mine is certain  

---

## Libraries Used  
- **Pygame** – for rendering the game visuals  
- **Random** – for generating the playing field randomly  
- **Time** – for recording elapsed time for the score  

---

## Program and Function Documentation  

Even though the documentation is written in english functions and their parameters may be in Czech. 

The program consists of two main files: **funkce.py** and **miny.py**  

### `funkce.py`  
This file defines the main functions responsible for the game logic:  

1. **new_game_grid(width, height, number of mines)**  
   - returns a grid of given size with `1` or `0` representing the existence of a mine  

2. **empty_grid(width, height)**  
   - returns a grid of `None` elements of the given size  

3. **is_in_grid(width, height, position(x, y))**  
   - returns `True` if the position lies within the given coordinate space  

4. **surrounding_cells((x, y), grid)**  
   - returns a list of all cells in the 1-cell radius  

5. **cell_number((x, y), grid of mines)**  
   - calculates and returns the number of the cell based on the number of bombs in the surrounding cells  
   - done using `surrounding_cells`, checking whether their coordinates in the bomb grid equal `1`, and incrementing the count accordingly  

6. **lostgame(uncovered grid, grid of mines)**  
   - returns a fully revealed grid if it is not already fully revealed + marks incorrectly flagged mines  

7. **wongame(uncovered grid, grid of mines)**  
   - returns a fully revealed grid if it is not already fully revealed  

8. **zero_chain(uncovered grid, grid of mines, list nulových buňěk)**  
   - for every cell in the revealed grid with value `0` that is not yet in the list of revealed zero cells, it reveals the 8 surrounding cells and adds it to the list  
   - this repeats until all zero cells are included in the list  
   - finally returns the revealed grid and the updated list of zero cells  

9. **simple_filter(uncovered grid, grid of mines, known moves grid)**  
   - for each revealed cell, it checks whether the number of **correctly placed flags** and the number of **certain mines** in the surrounding cells equals the **cell’s number**. If yes, then all other cells (not in the list of certain steps and not yet revealed) are marked as **False**.  
   - similarly, if the **number of flags** and **certain mines** in the surroundings together with the number of **unrevealed surrounding cells** equals the **cell’s number**, then those unrevealed cells are bombs and marked as **True**  
   - returns the grid of certain steps  

10. **complex_filter(uncovered grid, grid of mines, known moves grid)**  
   - creates a list of **border cells** from the revealed grid  
   - for each of these **border cells**, it finds its **dynamic number** (cell number minus the number of certain mines and flags in the surroundings), the list of **surrounding border mines**, and also the list of **surrounding unevaluated cells**  
   - then, for each surrounding **border mine**, it finds its **dynamic number** and the list of **surrounding unevaluated cells**  
   - two lists of uncertain cells are then created: one only from those around the 1st cell, and one only from those around the 2nd cell  
   - if the difference between the **dynamic number of the 2nd cell** and the **dynamic number of the 1st cell** equals the **size of the 2nd list**, then all cells from the 1st list are set to **False** in the grid of certain steps, and all cells from the 2nd list are set to **True**  
   - returns the grid of certain steps  

11. **is_there_next_stepuncovered grid, grid of mines)**  
   - creates an empty grid of certain steps, applies **simple_filter**, **complex_filter**, and **simple_filter** again  
   - then checks whether there is any certain move in this grid, stores this in the variable `possible_step`  
   - returns this variable `possible_step` along with the grid of certain steps  

---

### `miny.py`  
This file contains the main game code, using functions from `funkce.py`.  
It also loads visuals and contains basic functions for rendering the game window and board.  

#### Rendering functions:  

1. **parameters()**  
   - creates a window where the player can choose one of the difficulties, or choose a random difficulty, or custom dimensions and number of mines  

2. **start_game(height, width, number of mines)**  
   - starts the game and sets the main variables and the game board window  

3. **draw_frame(window, uncovered grid, size of a cell in pixels)**  
   - renders the current state of the game field into the window using sprites or text  

During the game, in every frame, the program checks whether the player clicked anywhere and updates the playing field accordingly, using functions from `funkce.py`.  
At the end of every frame, the state of the playing field is re-rendered.  

---

## Additional Information  
- Both files are described in more detail as part of the code.  
- Additionally, 15 PNG files are included, which make up the game’s visuals.  

---

## Sources  
- [CodingWithRuss - YouTube](https://www.youtube.com/watch?v=y9VG3Pztok8&ab_channel=CodingWithRuss)  
- [AppleMaths - YouTube](https://www.youtube.com/watch?v=8j7bkNXNx4M&ab_channel=AppleMaths)  
- [DataGenetics Blog](http://datagenetics.com/blog/june12012/index.html)  
- [Pygame Documentation](https://www.pygame.org/docs/)  
