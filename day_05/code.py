import requests
import os
import re
from dotenv import load_dotenv
import networkx as nx
import matplotlib.pyplot as plt

def prep_input(input: str) -> list[list[str], list[str]]:
    input = input.split('\n\n')
    rules = [[int(num) for num in x.split('|')] for x in input[0].split('\n')]
    update = [[int(num) for num in x.split(',')] for x in input[1].split('\n') if len(x) > 0]
    return rules, update

def validate_sequence(dg, sequence: list[int]) -> bool:
    for i in range(len(sequence) - 1):
        if not dg.has_edge(sequence[i], sequence[i+1]):
            return False
    return True

def find_path(dg, nodes):
    def dfs(current_node, path):
        if current_node not in visited:
            visited.add(current_node)
            path.append(current_node)
            if len(path) == len(nodes):
                if list(path) not in paths:
                    paths.append(list(path))
            else:
                for next_node in dg.successors(current_node):
                    if next_node not in visited and next_node in nodes:
                        dfs(next_node, path)
            path.pop()
            visited.remove(current_node)
    
    
    paths = []
    for node in nodes:
        visited = set()
        dfs(node, [])

    return paths


def advent_1(input: str) -> int:
    rules, updates = prep_input(input)

    dg = nx.DiGraph()
    for rule in rules:
        dg.add_edge(rule[0], rule[1])

    pos = nx.spring_layout(dg) 
    nx.draw(dg, pos, with_labels=True)
    plt.savefig('day_05/graph.png')

    middle_page_number = 0

    for update in updates:
        if validate_sequence(dg, update):
            middle_page_number += update[len(update) // 2]

    return middle_page_number

def advent_2(input: str) -> int:
    rules, updates = prep_input(input)

    dg = nx.DiGraph()
    for rule in rules:
        dg.add_edge(rule[0], rule[1])

    pos = nx.spring_layout(dg) 
    nx.draw(dg, pos, with_labels=True)
    plt.savefig('day_05/graph.png')

    middle_page_number = 0

    for update in updates:
        if validate_sequence(dg, update):
            pass
        else:
            x = find_path(dg, update)
            middle_page_number += x[0][len(x[0]) // 2]

    return middle_page_number

if __name__ == "__main__":
    load_dotenv()

    r = requests.get('https://adventofcode.com/2024/day/5/input', headers={"cookie": os.getenv("COOKIE")})

    print(advent_1(r.text))

    print(advent_2(r.text))