import requests
import os
import re
from dotenv import load_dotenv

def advent_1(input: str) -> int:
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    matches = re.findall(pattern, input)

    multiplication = 0

    print(matches)
    if matches:
        for match in matches:
            a, b = int(match[0]), int(match[1])
            multiplication += (a * b)

    return multiplication

def find_closest_lower(index: int, do_list: list[int], dont_list: list[int]) -> list[int]:
    closest_list1 = max([num for num in do_list if num <= index], default=None)
    closest_list2 = max([num for num in dont_list if num <= index], default=None)

    return [closest_list1, closest_list2]

def advent_2(input: str) -> int:
    mul_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    do_pattern = r'do\(\)'
    dont_pattern = r'don\'t\(\)'

    mul_matches = [(match.start(), match.end(), int(match.groups()[0]) * int(match.groups()[1])) for match in re.finditer(mul_pattern, input)]
    do_matches = [0] + [match.end() for match in re.finditer(do_pattern, input)]
    dont_matches = [match.end() for match in re.finditer(dont_pattern, input)]

    multiplication = 0

    for mul in mul_matches:
        closest = find_closest_lower(mul[0], do_matches, dont_matches)
        print(f"mul: {mul}, closest values: {closest}")
        if closest[1] is None:
            print("adding to multiplication")
            multiplication += mul[2]
        elif closest[0] > closest[1]:
            print("adding to multiplication")
            multiplication += mul[2]
    
    return multiplication

if __name__ == "__main__":
    load_dotenv()

    r = requests.get('https://adventofcode.com/2024/day/3/input', headers={"cookie": os.getenv("COOKIE")})

    print(advent_1(r.text))

    print(advent_2(r.text))