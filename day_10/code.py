import requests
import os
from dotenv import load_dotenv
import queue

def prep_input(input: str) -> list[list[int]]:
    return [[int(num) for num in line] for line in input.split('\n') if len(line) > 0]

def is_within_bounds(x: int, y: int, grid: list[list[str]]):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])

def find_next_steps(x: int, y: int, next_step: int, input: list[list[int]]) -> list[(int, int)]:
    steps = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    return [step for step in steps if is_within_bounds(step[0], step[1], input) and input[step[0]][step[1]] == next_step]


def advent_1(input: str) -> int:
    input = prep_input(input)
    # print(input)

    simple_queue = queue.SimpleQueue()

    for x in range(len(input)):
        for y in range(len(input[x])):
            if input[x][y] == 0:
                simple_queue.put((x, y, 1, [[x, y]]))

    complete_paths = set()

    while not simple_queue.empty():
        x, y, next_value, history = simple_queue.get()
        # print(f"Location ({x}, {y}) next value {next_value} history {history}")
        next_steps = find_next_steps(x, y, next_value, input)
        # print(f"Next steps {next_steps}")
        for step in next_steps:
            if next_value == 9:
                complete_paths.add((history[0][0], history[0][1], step[0], step[1]))
                continue
            simple_queue.put((step[0], step[1], next_value + 1, history + [(step[0], step[1])]))
 
    # print(complete_paths)
    return len(complete_paths)

def advent_2(input: str) -> int:
    input = prep_input(input)
    # print(input)

    simple_queue = queue.SimpleQueue()

    for x in range(len(input)):
        for y in range(len(input[x])):
            if input[x][y] == 0:
                simple_queue.put((x, y, 1, [[x, y]]))

    complete_paths = 0

    while not simple_queue.empty():
        x, y, next_value, history = simple_queue.get()
        # print(f"Location ({x}, {y}) next value {next_value} history {history}")
        next_steps = find_next_steps(x, y, next_value, input)
        # print(f"Next steps {next_steps}")
        for step in next_steps:
            if next_value == 9:
                complete_paths += 1
                continue
            simple_queue.put((step[0], step[1], next_value + 1, history + [(step[0], step[1])]))
 
    # print(complete_paths)
    return complete_paths

if __name__ == "__main__":
    load_dotenv()

    r = requests.get('https://adventofcode.com/2024/day/10/input', headers={"cookie": os.getenv("COOKIE")})

    print(advent_1(r.text))

    print(advent_2(r.text))