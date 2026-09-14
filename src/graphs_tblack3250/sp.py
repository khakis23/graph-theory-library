import sys
from graphs_tblack3250.heapq import heappush, heappop
from graphs_tblack3250._core import AStar, Vec2


def astar(source: tuple, goal: tuple, grid) -> list | None:
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
    :return: list of coordinates from source to goal, or None if there is an error
    """

    live_print = input("Would you like to visualize the path "
                       "(this works best in the stock macOS or linux terminal)? (y/n):").lower() == 'y'

    try:
        astar = AStar(grid)
        results = astar.find(
            Vec2(source[0], source[1]),
            Vec2(goal[0], goal[1]),
            live_print=live_print
        )
        return results
    except Exception as e:
        print("Error with C++ AStar implementation: ", e)
        return None


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
