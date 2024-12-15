import requests
import os
from dotenv import load_dotenv
import networkx as nx
import matplotlib.pyplot as plt

def prep_input(input: str) -> list[list[str]]:
    return [list(row) for row in input.split("\n") if len(row) != 0]

def is_within_bounds(x: int, y: int, grid: list[list[str]]) -> bool:
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])

def visualise_graph(graph: nx.Graph, fn: str) -> None:
    pos = nx.spring_layout(graph)
    plt.figure(figsize=(8, 8))
    nx.draw(graph, pos=pos, with_labels=True, node_color='lightblue', font_weight='bold')
    plt.savefig(f'{fn}.png')

def advent_1(input: str) -> int:
    grid = prep_input(input)

    graph = nx.Graph()
    graph_connected = nx.Graph()

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            graph.add_node((r, c), key=grid[r][c])
            graph_connected.add_node((r, c), key=grid[r][c])
            steps = [(r + 1, c), (r - 1, c), (r, c+ 1), (r, c- 1)]
            for step in steps:
                if is_within_bounds(step[0], step[1], grid):
                    graph.add_edge((r, c), step)
                    if grid[r][c] == grid[step[0]][step[1]]:
                        graph_connected.add_edge((r, c), step)

    #virtual nodes for external perimeter
    rows = len(grid)
    cols = len(grid[0])
    print(f"rows - {rows}, cols - {cols}")
    for c in range(cols):
        print(f"col - {c}")
        if (0, c) not in graph.nodes():
            graph.add_node((-1, c))
        if (rows, c) not in graph.nodes():
            print(f"row + 1 - {rows}")
            graph.add_node((rows, c))
    for r in range(rows):
        print(f"row - {r}")
        if (r, 0) not in graph.nodes():
            graph.add_node((r, -1))
        if (r, cols) not in graph.nodes():
            print(f"col + 1 - {cols}")
            graph.add_node((r, cols))

    # Add edges from virtual nodes to existing nodes on the boundary
    for c in range(cols):
        if (-1, c) not in graph.nodes():
            graph.add_edge((-1, c), (0, c))
        if (len(grid) + 1, c) not in graph.nodes():
            print((rows, c))
            print((rows -1 , c))
            graph.add_edge((rows, c), (rows -1 , c))
    for r in range(len(grid)):
        if (r, -1) not in graph.nodes():
            graph.add_edge((r, -1), (r, 0))
        if (r, cols + 1) not in graph.nodes():
            graph.add_edge((r, cols), (r, cols-1))
    
    # visualise_graph(graph, "graph")
    # visualise_graph(graph_connected, "sub-graph")

    def count_perimeter(component):
        perimeter = 0
        nodes_in_component = set(component)
        print(f"nodes in compont - {nodes_in_component}")

        for node in component:
            neighbors = set([node] + list(graph.neighbors(node)))
            print(f"neighbors - {neighbors}")
            boundary_nodes = neighbors - nodes_in_component
            perimeter += len(boundary_nodes)

        print(perimeter)
        return perimeter
    
    components = list(nx.connected_components(graph_connected))
    total_perimeter = 0
    for component in components:
        total_perimeter += len(component) * count_perimeter(component)

    print(f"Total Perimeter: {total_perimeter}")
    

    return total_perimeter

def advent_2(input: str) -> int:
    grid = prep_input(input)

    graph = nx.Graph()
    graph_connected = nx.Graph()

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            graph.add_node((r, c), key=grid[r][c])
            graph_connected.add_node((r, c), key=grid[r][c])
            steps = [(r + 1, c), (r - 1, c), (r, c+ 1), (r, c- 1)]
            for step in steps:
                if is_within_bounds(step[0], step[1], grid):
                    graph.add_edge((r, c), step)
                    if grid[r][c] == grid[step[0]][step[1]]:
                        graph_connected.add_edge((r, c), step)

    #virtual nodes for external perimeter
    rows = len(grid)
    cols = len(grid[0])
    print(f"rows - {rows}, cols - {cols}")
    for c in range(cols):
        print(f"col - {c}")
        if (0, c) not in graph.nodes():
            graph.add_node((-1, c))
        if (rows, c) not in graph.nodes():
            print(f"row + 1 - {rows}")
            graph.add_node((rows, c))
    for r in range(rows):
        print(f"row - {r}")
        if (r, 0) not in graph.nodes():
            graph.add_node((r, -1))
        if (r, cols) not in graph.nodes():
            print(f"col + 1 - {cols}")
            graph.add_node((r, cols))

    # Add edges from virtual nodes to existing nodes on the boundary
    for c in range(cols):
        if (-1, c) not in graph.nodes():
            graph.add_edge((-1, c), (0, c))
        if (len(grid) + 1, c) not in graph.nodes():
            print((rows, c))
            print((rows -1 , c))
            graph.add_edge((rows, c), (rows -1 , c))
    for r in range(len(grid)):
        if (r, -1) not in graph.nodes():
            graph.add_edge((r, -1), (r, 0))
        if (r, cols + 1) not in graph.nodes():
            graph.add_edge((r, cols), (r, cols-1))

    components = list(nx.connected_components(graph_connected))
    total_cost = 0
    for component in components:
        boundary = list(nx.node_boundary(graph, component))
        print(f"boundary - {boundary}")
        print(f"component - {component}")

        corner_candidates = set()

        for node in component:
            print(f"node - {node}")
            
            for corner_r, corner_c in [ (node[0]-0.5, node[1]-0.5), (node[0]+0.5, node[1]-0.5), (node[0]+0.5, node[1]+0.5), (node[0]-0.5, node[1]+0.5) ]:

                corner_candidates.add((corner_r, corner_c))
        
        print(f"corner candidates {corner_candidates}")

        turn_count = 0

        for cr, cc in corner_candidates:
            counts = [(sr, sc) in component for sr, sc in [ (cr-0.5, cc-0.5), (cr+0.5, cc-0.5), (cr+0.5, cc+0.5), (cr-0.5, cc+0.5) ]]
            cells = sum(counts)
            if cells == 1 or cells == 3:
                turn_count += 1
            elif cells == 2:
                if counts == [True, False, True, False] or counts == [False, True, False, True]:
                    turn_count += 2

        print(f"total sides: {turn_count}")

        total_cost += len(component) * turn_count
        print(f"total cost: {total_cost}")

    print(f"Total Perimeter: {total_cost}")
    
    return total_cost

if __name__ == "__main__":
    load_dotenv()

    r = requests.get('https://adventofcode.com/2024/day/12/input', headers={"cookie": os.getenv("COOKIE")})

    print(advent_1(r.text))

    print(advent_2(r.text))