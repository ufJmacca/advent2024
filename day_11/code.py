import requests
import os
from dotenv import load_dotenv
from functools import cache

def prep_input(input: str) -> list[list[str]]:
    return [int(line) for line in input.strip().split()]


@cache
def check_value(value: int, steps: int) -> int:
    if steps == 0:
        return 1
    if value == 0:
        return check_value(1, steps -1)
    if len(str(value)) % 2 == 0:
        mid = len(str(value)) // 2
        return check_value(int(str(value)[:mid]), steps -1) + check_value(int(str(value)[mid:]), steps -1)
    else:
        return check_value(value*2024, steps -1)

def advent_1(input: str, blinks: int) -> int:
    input = prep_input(input)
    
    return sum(check_value(value, blinks) for value in input)

def advent_2(input: str, blinks: int) -> int:
    input = prep_input(input)
    
    return sum(check_value(value, blinks) for value in input)

if __name__ == "__main__":
    load_dotenv()

    r = requests.get('https://adventofcode.com/2024/day/11/input', headers={"cookie": os.getenv("COOKIE")})

    print(advent_1(r.text, 25))

    print(advent_2(r.text, 75))