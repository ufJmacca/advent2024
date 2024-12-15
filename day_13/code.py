import requests
import os
from dotenv import load_dotenv
import re
from typing import Generator, Tuple
from collections import deque
import numpy as np

def prep_input(input: str) -> Generator[Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]]]:
    pattern = r'.*X\+(\d*).*Y\+(\d*)\n.*X\+(\d*).*Y\+(\d*)\n.*X=(\d*).*Y=(\d*)'
    matches = re.findall(pattern, input)

    for match in matches:
        yield (int(match[0]), int(match[1])) , (int(match[2]), int(match[3])), (int(match[4]), int(match[5]))

def prep_input_2(input: str) -> Generator[Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]]]:
    pattern = r'.*X\+(\d*).*Y\+(\d*)\n.*X\+(\d*).*Y\+(\d*)\n.*X=(\d*).*Y=(\d*)'
    matches = re.findall(pattern, input)

    for match in matches:
        yield (int(match[0]), int(match[1])) , (int(match[2]), int(match[3])), (int(match[4]) + 10000000000000, int(match[5]) + 10000000000000)

def is_valid(x, y, target):
    return 0 <= x <= target[0] and 0 <= y <= target[1]

def bfs(start, a, b, target):
    queue = deque([(start, 0)])
    visited = set()
    visited.add((start,0))
    min_cost = float('inf')

    while queue:
        (x, y), cost = queue.popleft()
        # print(f"current position ({x}, {y}) with cost {cost}")

        if (x, y) == target:
            # print(f"target found with cost {cost}")
            if cost < min_cost:
                min_cost = cost
                yield cost
            if cost == min_cost:
                yield cost
        
        ax, ay = x + a[0], y + a[1]
        acost = cost + 3
        bx, by = x + b[0], y + b[1]
        bcost = cost + 1

        if is_valid(ax, ay, target) and (ax, ay) not in visited:
            # print(f"moving to {ax}, {ay} with cost {acost}")
            queue.append(((ax, ay), acost))
            visited.add((ax, ay))

        if is_valid(bx, by, target) and (bx, by) not in visited:
            # print(f"moving to {bx}, {by} with cost {bcost}")
            queue.append(((bx, by), bcost))
            visited.add((bx, by))

    return None


def advent_1(input: str) -> int:
    gen = prep_input(input)

    tokens = 0

    for a, b, target in gen:
        print(a, b, target)

        prize_cost = list(bfs((0,0), a, b, target))

        print(f"prize cost {prize_cost}")

        if prize_cost:
            tokens += min(prize_cost)


    return tokens

def advent_2(input: str) -> int:
    gen = prep_input_2(input)

    tokens = 0

    for a, b, target in gen:
        print(a, b, target)

        a_presses = (target[0] * b[1] - target[1] * b[0]) / (a[0] * b[1] - a[1] * b[0])
        b_presses = (target[0] - a[0] * a_presses) / b[0]

        if a_presses % 1 == b_presses % 1 == 0:
            tokens += int(a_presses*3) + int(b_presses)

    return tokens

if __name__ == "__main__":
    load_dotenv()

    r = requests.get('https://adventofcode.com/2024/day/13/input', headers={"cookie": os.getenv("COOKIE")})

    # print(advent_1(r.text))

    print(advent_2(r.text))