import requests
import os
import re
from dotenv import load_dotenv
from collections import Counter

def prep_input(input: str) -> list[int]:
    lines = input.split('\n')
    pattern = r'\s+'
    return [[int(value) for value in re.split(pattern, line)] for line in lines if line.strip()]

def advent_1(input: str) -> int:
    input = prep_input(input)

    left_array = sorted([item[0] for item in input])
    right_array = sorted([item[1] for item in input])

    difference = [abs(right - left) for left, right in zip(left_array, right_array)]

    return sum(difference)

def advent_2(input: str) -> int:
    input = prep_input(input)

    left_array = sorted([item[0] for item in input])
    right_array = sorted([item[1] for item in input])

    right_dict = dict(Counter(right_array))

    similarity = 0
    for value in left_array:
        if value in right_dict:
            similarity += value * right_dict[value]
        else:
            similarity += 0
    
    return similarity


if __name__ == "__main__":
    load_dotenv()

    r = requests.get('https://adventofcode.com/2024/day/1/input', headers={"cookie": os.getenv("COOKIE")})

    print(advent_1(r.text))

    print(advent_2(r.text))