import sys
from graphs_tblack3250.heapq import heappush, heappop
from graphs_tblack3250._core import AStar, Vec2


def astar(source: tuple, goal: tuple, grid, render_speed=250) -> list | None:
    """
    A* search implementation using a C++ accelerated engine.

    Grid format:

    - Characters: 'a' ... 'f' for preset grids.
    - Custom boolean matrix example::

        [[True, True, False],
         [True, False, True],
         [True, True, True]]

    :param source: starting coordinates (x, y)
    :param goal: ending coordinates (x, y)
    :param grid: preset character or custom boolean matrix (see above)
    :param render_speed: speed in milliseconds per frame (default: 250)
    :return: list of coordinates from source to goal, or None if there is an error
    """

    live_print = input("Would you like to visualize the path "
                       "(rendering works best in the stock terminal)? (y/n):").lower() == 'y'

    try:
        astar = AStar(grid)
        astar.setLivePrintSpeed(render_speed)
        results = astar.find(
            Vec2(source[0], source[1]),
            Vec2(goal[0], goal[1]),
            live_print=live_print
        )
        return results
    except Exception as e:
        print("Error with C++ AStar implementation: ", e)
        return None


def format_astar_path(path_nodes) -> str:
    """
    Converts an iterable of Vec2 objects into a human-readable path string.

    :param path_nodes: collection of Vec2 objects from astar search
    :return: formatted string representation of the path
    """
    if not path_nodes:
        return "No path found"

    return " -> ".join(f"({node.x}, {node.y})" for node in path_nodes)


def dijkstra(graph, source):
    dist = {node: sys.maxsize for node in graph}
    dist[source] = 0
    heap = []
    heappush(heap, (0, source))
    path = {source: []}

    while heap:
        w, u = heappop(heap)
        for v in graph[u]:
            if w + graph[u][v] < dist[v]:
                dist[v] = w + graph[u][v]
                heappush(heap, (dist[v], v))
                path[v] = path[u] + [u]

    return dist, path
