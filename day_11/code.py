import requests
import os
from dotenv import load_dotenv
import concurrent.futures
from collections import deque

def prep_input(input: str) -> list[list[str]]:
    return [int(line) for line in input.strip().split()]


def check_and_append(value: int) -> list[int]:
    if value == 0:
        return [1]
    if len(str(value)) % 2 == 0:
        mid = len(str(value)) // 2
        return [int(str(value)[:mid]), int(str(value)[mid:])]
    else:
        return [value*2024]

def blink(input: list[int]) -> list[int]:
    with concurrent.futures.ThreadPoolExecutor(max_workers=24) as executor:
        queue = deque(executor.submit(check_and_append, value) for value in input)
        next_list = []

        while queue:
            future = queue.popleft()
            try:
                result = future.result()
                next_list.extend(result)
            except Exception as e:
                print(f"Error processing: {e}")
    
    return next_list

# def blink(input: list[int]) -> list[int]:
#     next_list = []
#     for i in range(len(input)):
#         result = check_and_append(input[i])
#         next_list.extend(result)
#     return next_list

def advent_1(input: str, blinks: int) -> int:
    input = prep_input(input)
    # print(input)

    for _ in range(blinks):
        input = blink(input)
        # print(input)
    
    return len(input)

def advent_2(input: str, blinks: int) -> int:
    input = prep_input(input)
    # print(input)

    for i in range(blinks):
        print(f"blink number {i}")
        input = blink(input)
        # print(input)
    
    return len(input)
if __name__ == "__main__":
    load_dotenv()

    r = requests.get('https://adventofcode.com/2024/day/11/input', headers={"cookie": os.getenv("COOKIE")})

    print(advent_1(r.text, 25))

    print(advent_2(r.text, 75))