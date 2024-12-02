import requests
import os
import re
from dotenv import load_dotenv

def prep_input(input: str) -> list[int]:
    lines = input.split('\n')
    pattern = r'\s+'
    return [[int(num) for num in re.split(pattern, line)] for line in lines if len(line) > 0]

def safety_check(line: list[int]) -> int:
    differences = [line[i+1] - line[i] for i in range(len(line)- 1)]
    if all(difference > 0 for difference in differences):
        if all(1 <= difference <= 3 for difference in differences):
            return 1
    if all(difference < 0 for difference in differences):
        if all(-3 <= difference <= -1 for difference in differences):
            return 1
    return 0

def advent_1(input: str) -> int:
    input = prep_input(input)
    
    safe = 0

    for line in input:
        safe += safety_check(line)
    
    return safe

def advent_2(input: str) -> int:
    input = prep_input(input)
    
    safe = 0

    for line in input:
        first_check = safety_check(line)
        if first_check == 1:
            safe += 1

        else:

            for index in range(len(line)):
                pop_line = line.copy()
                pop_line.pop(index)
                second_check = safety_check(pop_line)
                if second_check == 1:
                    safe += 1
                    break
    
    return safe

if __name__ == "__main__":
    load_dotenv()

    r = requests.get('https://adventofcode.com/2024/day/2/input', headers={"cookie": os.getenv("COOKIE")})

    print(f"Advent 1: {advent_1(r.text)}")
    print(f"Advent 2: {advent_2(r.text)}")