import requests
import os
import re
from dotenv import load_dotenv
from collections import Counter

def prep_input(input: str) -> list[list[str]]:
    return [list(line) for line in input.split("\n") if len(line) > 0]

def is_within_bounds(x: int, y: int, grid: list[list[str]]):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])

def search_next_direction(x: int, y:int, grid: list[list[str]], direction: tuple[int], letter: str) -> bool:
    new_x, new_y = x + direction[0], y + direction[1]
    if is_within_bounds(new_x, new_y, grid): 
        if grid[new_x][new_y] == letter:
            if letter == "A":
                if search_next_direction(new_x, new_y, grid, direction, "S"):
                    return True
            elif letter == "S":
                return True
    return False

def search_adjacent(x: int, y: int, grid: list[list[str]]) -> int:
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

    count_xmas = 0

    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if is_within_bounds(new_x, new_y, grid):
            if grid[new_x][new_y] == "M":
                if search_next_direction(new_x, new_y, grid, (dx, dy), "A"):
                    count_xmas += 1
    return count_xmas


def advent_1(input: str) -> int:
    input = prep_input(input)

    count_xmas = 0

    for x in range(len(input)):
        for y in range(len(input[0])):
            if input[x][y] == "X":
                count_xmas += search_adjacent(x, y, input)

    
    return count_xmas

def search_x(x: int, y: int, grid: list[list[str]]) -> int:
    direction_pairs = [[(1, 1), (-1, -1)], [(1, -1), (-1, 1)]]

    pair_strings = []
    for pair in direction_pairs:
        pair_string = ""
        for angle in pair:
            new_x, new_y = x + angle[0], y + angle[1]
            if is_within_bounds(new_x, new_y, grid):
                pair_string += grid[new_x][new_y]
        pair_strings.append(sorted(pair_string))
    
    if pair_strings == [['M', 'S'], ['M', 'S']]:
        return 1

    return 0

def advent_2(input: str) -> int:
    input = prep_input(input)

    count_x_mas = 0

    for x in range(len(input)):
        for y in range(len(input[0])):
            if input[x][y] == "A":
                count_x_mas += search_x(x, y, input)

    return count_x_mas

if __name__ == "__main__":
    load_dotenv()

    r = requests.get('https://adventofcode.com/2024/day/4/input', headers={"cookie": os.getenv("COOKIE")})

    print(advent_1(r.text))

    print(advent_2(r.text))