import random
import clear_screen

# Constants for maze generation
WALL = '#'
PATH = ' '
START = 'S'
EXIT = 'E'

# Maze dimensions
WIDTH = 35
HEIGHT = 10

def generate_maze(width, height):
    # Initialize the maze with walls
    maze = [[WALL] * width for _ in range(height)]
    
    # Carve a path in the maze
    def carve(x, y):
        directions = [(2, 0), (-2, 0), (0, 2), (0, -2)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 < nx < width - 1 and 0 < ny < height - 1 and maze[ny][nx] == WALL:
                maze[y + dy // 2][x + dx // 2] = PATH
                maze[ny][nx] = PATH
                carve(nx, ny)

    # Start carving from (1, 1)
    maze[1][1] = START
    carve(1, 1)
    maze[height - 2][width - 2] = EXIT  # Place the exit

    return maze

def display_maze(maze, player_pos):
    for i in range(len(maze)):
        row = ''
        for j in range(len(maze[i])):
            if (i, j) == player_pos:
                row += 'P '  # Player position
            else:
                row += maze[i][j] + ' '
        print(row)
    print()

def check_win(maze, player_pos):
    return maze[player_pos[0]][player_pos[1]] == EXIT

def move_player(maze, player_pos, direction):
    x, y = player_pos
    if direction == 'w':  # Up
        new_pos = (x - 1, y)
    elif direction == 's':  # Down
        new_pos = (x + 1, y)
    elif direction == 'a':  # Left
        new_pos = (x, y - 1)
    elif direction == 'd':  # Right
        new_pos = (x, y + 1)
    else:
        return player_pos

    if maze[new_pos[0]][new_pos[1]] != WALL:
        return new_pos
    return player_pos

# Main game loop
def main(player):
    maze = generate_maze(WIDTH, HEIGHT)
    player_pos = (1, 1)  # Start position

    while True:
        display_maze(maze, player_pos)
        move_input = input("Enter your move (w=up, s=down, a=left, d=right): ").lower()

        player_pos = move_player(maze, player_pos, move_input)

        if check_win(maze, player_pos):
            print("Congratulations! You've reached the exit!")
            player.souls += 1000
            print(f"You got 1000 souls!")
            break
        
        clear_screen.clear_screen()
        

if __name__ == "__main__":
    main()
