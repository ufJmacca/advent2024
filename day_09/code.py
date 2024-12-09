import requests
import os
from dotenv import load_dotenv

def prep_input(input: str) -> list[list[str]]:
    return [[int(x) for x in line] for line in input.split("\n") if len(line) > 0]

def last_non_dot_index(input: str) -> int:
    for index, value in enumerate(input[::-1]):
        # print(index)
        if value != ".":
            return len(input) - index -1
    return len(input)

def advent_1(input: str) -> int:
    input = prep_input(input)[0]

    # print(input)

    string = []
    id = 0

    for index, value in enumerate(input):
        if index % 2 == 0:
            string += [id] * value
            id += 1
        else:
            string += ["."] * value

    blanks = [i for i,x in enumerate(string) if x == "."]

    for i in blanks:
        while string[-1] == ".": string.pop()
        if len(string) <= i: break
        string[i] = string.pop()

    checksum = 0

    for index, value in enumerate(string):
        checksum += int(value) * index

    return checksum

def advent_2(input: str) -> int:
    input = prep_input(input)[0]

    blanks = []
    files = {}
    
    id = 0
    position = 0

    for index, value in enumerate(input):
        if index % 2 == 0:
            if int(value) == 0:
                raise ValueError("Invalid input: file size is zero")
            files[id] = (position, int(value))
            id += 1
        else:
            if int(value) != 0:
                blanks.append((position, int(value)))
        position += int(value)

    while id > 0:
        id -= 1

        file_position, file_size = files[id]

        for i, (blank_start, blank_length) in enumerate(blanks):
            if blank_start >= file_position:
                blanks = blanks[:i]
                break
            if file_size <= blank_length:
                files[id] = (blank_start, file_size)
                if file_size == blank_length:
                    blanks.pop(i)
                else:
                    blanks[i] = (blank_start + file_size, blank_length - file_size)
                break
    
    checksum = 0

    for index, (position, size) in files.items():
        for i in range(position, position + size):
            checksum += index * i

    return checksum

if __name__ == "__main__":
    load_dotenv()

    r = requests.get('https://adventofcode.com/2024/day/9/input', headers={"cookie": os.getenv("COOKIE")})

    print(advent_1(r.text))

    print(advent_2(r.text))