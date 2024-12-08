import requests
import os
from dotenv import load_dotenv

def prep_input(input: str) -> list[int, list[int]]:
    output = []
    for line in input.split('\n'):
        if len(line) > 0:
            line_array = line.split(": ")
            value = int(line_array[0])
            numbers = [int(num) for num in line_array[1].split(" ") if len(num)>0]
            output.append([value, numbers])
            print([value, numbers])
    return output

def value_test(target: int, numbers: list[int]) -> int:
    if len(numbers) == 1:
        print(f"target {target} numbers {numbers}")
        return target == numbers[0]
    
    if target % numbers[-1] == 0 and value_test(target // numbers[-1], numbers[:-1]):
        print(f"% brach - target {target} numbers {numbers}")
        return True
    
    if target > numbers[-1] and value_test(target - numbers[-1], numbers[:-1]):
        print(f"> branch - target {target} numbers {numbers}")
        return True
    
    return False

def advent_1(input: str) -> int:
    input = prep_input(input)

    total = 0

    for item in input:
        value, numbers = item

        print(f"value {value} numbers {numbers}")

        if value_test(value, numbers):
            print(f"value {value} is obtainable")
            total += value

    return total

def value_test_part_2(target: int, numbers: list[int]) -> int:
    if len(numbers) == 1:
        print(f"target {target} numbers {numbers}")
        return target == numbers[0]
    
    if target % numbers[-1] == 0 and value_test_part_2(target // numbers[-1], numbers[:-1]):
        print(f"% brach - target {target} numbers {numbers}")
        return True
    
    if target > numbers[-1] and value_test_part_2(target - numbers[-1], numbers[:-1]):
        print(f"> branch - target {target} numbers {numbers}")
        return True
    
    string_target = str(target)
    string_last_elemetn = str(numbers[-1])
    
    if len(string_target) > len(string_last_elemetn) and string_target.endswith(string_last_elemetn) and value_test_part_2(int(string_target[:-len(string_last_elemetn)]), numbers[:-1]):
        return True
    
    return False

def advent_2(input: str) -> int:
    input = prep_input(input)

    total = 0

    for item in input:
        value, numbers = item

        print(f"value {value} numbers {numbers}")

        if value_test_part_2(value, numbers):
            print(f"value {value} is obtainable")
            total += value

    return total

if __name__ == "__main__":
    load_dotenv()

    r = requests.get('https://adventofcode.com/2024/day/7/input', headers={"cookie": os.getenv("COOKIE")})

    print(advent_1(r.text))

    print(advent_2(r.text))