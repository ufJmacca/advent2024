import requests
import os
from dotenv import load_dotenv

def prep_input(input: str) -> list[list[str]]:
    return [[x for x in line] for line in input.split("\n") if len(line) > 0]

def is_within_bounds(x: int, y: int, grid: list[list[str]]):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])

def create_antenna_locations(grid: list[list[str]]) -> dict[tuple[int, int]]:
    locations = dict()
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            node = grid[x][y]
            if node != ".":
                if node not in locations:
                    locations[node] = []
                locations[node].append((x, y))
    return locations

def advent_1(input: str) -> int:
    input = prep_input(input)
    
    antenna_locations = create_antenna_locations(input)

    seen_nodes = set()
    
    for key, value in antenna_locations.items():
        for a in range(len(value)):
            for b in range(len(value)):
                if a != b:
                    x1, y1 = value[a]
                    x2, y2 = value[b]
                    distance = (x1 - x2, y1 - y2)
                    antinode_location = x1 + distance[0], y1 + distance[1]
                    inbound = is_within_bounds(antinode_location[0], antinode_location[1], input)
                    if inbound and antinode_location not in seen_nodes: 
                        seen_nodes.add(antinode_location)
                    print(f"Key {key} - point ({x1}, {y1}) to point ({x2}, {y2}) distance: {distance} - antinode in bounds: {inbound} - ({x1 + distance[0]}, {y1 + distance[1]})")
    return len(seen_nodes)

def advent_2(input: str) -> int:
    input = prep_input(input)
    
    antenna_locations = create_antenna_locations(input)

    seen_nodes = set()
    
    for key, value in antenna_locations.items():
        for a in range(len(value)):
            for b in range(len(value)):
                if a != b:
                    x1, y1 = value[a]
                    x2, y2 = value[b]
                    current_node = (x1, y1)
                    seen_nodes.add(current_node)
                    distance = (x1 - x2, y1 - y2) 
                    while is_within_bounds(current_node[0] + distance[0], current_node[1] + distance[1], input):
                        antinode_location = current_node[0] + distance[0], current_node[1] + distance[1]
                        inbound = is_within_bounds(antinode_location[0], antinode_location[1], input)
                        if inbound: 
                            seen_nodes.add(antinode_location)
                            current_node = antinode_location
                        print(f"Key {key} - point ({x1}, {y1}) to point ({x2}, {y2}) distance: {distance} - antinode in bounds: {inbound} - ({antinode_location[0]}, {antinode_location[1]})")
    return len(seen_nodes)

if __name__ == "__main__":
    load_dotenv()

    r = requests.get('https://adventofcode.com/2024/day/8/input', headers={"cookie": os.getenv("COOKIE")})

    print(advent_1(r.text))

    print(advent_2(r.text))