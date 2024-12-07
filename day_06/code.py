import requests
import os
import re
from dotenv import load_dotenv
from typing import List, Tuple
import copy

def prep_input(input: str) -> Tuple[List[List[str]], Tuple[int, int]]: 
    grid = [[x for x in line] for line in input.split("\n") if len(line) > 0]

    start = ()

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "^":
                start = (i, j)
    
    return grid, start

def is_within_bounds(x: int, y: int, grid: list[list[str]]):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])

def search_next_direction(x: int, y:int, grid: list[list[str]], direction: tuple[int], current_direction: int, visits: tuple[int] = None) -> str:
    new_x, new_y = x + direction[0], y + direction[1]
    if visits is None:
        visited = False
    else:
        visited = (x, y, current_direction) in visits
    if visited:
        return "visited"
    
    if is_within_bounds(new_x, new_y, grid): 
        if grid[new_x][new_y] == "#":
            return "turn"
        elif grid[new_x][new_y] == "O":
            return "turn"
        else:
            return "forward"

    return "end"

def move(pos: tuple[int, int], direction: int, directions: dict[tuple[int, int]]) -> tuple[int, int]:
    return (pos[0] + directions[direction][0], pos[1] + directions[direction][1])

def print_grid(grid: list[list[str]], visited: set[tuple[int, int], int], pos: tuple[int, int]):
    for visited_pos in visited:
        grid[visited_pos[0]][visited_pos[1]] = str(visited_pos[2])

    grid[pos[0]][pos[1]] = "O"

    for line in grid:
        print("".join(line))
   



def advent_1(input: str) -> int:
    input, start_location = prep_input(input)

    directions = {
        1: (-1, 0),
        2: (0, 1),
        3: (1, 0),
        0: (0, -1)
    }
    
    visited = set()
    position = start_location
    visited.add(position)
    current_direction = 1

    while True:
        next_direction = search_next_direction(position[0], position[1], input, directions[current_direction], current_direction)
        if next_direction == "turn":
            current_direction += 1
            current_direction = current_direction % 4
        elif next_direction == "forward":
            position = move(position, current_direction, directions)
            visited.add(position)
        elif next_direction == "end":
            break
    

    return len(visited)

def advent_2(input: str) -> int:
    input, start_location = prep_input(input)

    directions = {
        1: (-1, 0),
        2: (0, 1),
        3: (1, 0),
        0: (0, -1)
    }

    loops = 0

    for o_x in range(len(input)):
        for o_y in range(len(input[o_x])):
            visited = set()

            grid = copy.deepcopy(input)
            grid[o_x][o_y] = "O"
            position = start_location
            current_direction = 1

            while True:
                next_direction = search_next_direction(position[0], position[1], grid, directions[current_direction], current_direction, visited)
                if next_direction == "visited":
                    loops += 1
                    break
                elif next_direction == "turn":
                    current_direction += 1
                    current_direction = current_direction % 4
                elif next_direction == "forward":
                    visited.add((position[0], position[1], current_direction))
                    position = move(position, current_direction, directions)
                elif next_direction == "end":
                    break
    

    return loops

if __name__ == "__main__":
    load_dotenv()

    r = requests.get('https://adventofcode.com/2024/day/6/input', headers={"cookie": os.getenv("COOKIE")})

    print(advent_1(r.text))

    print(advent_2(r.text))