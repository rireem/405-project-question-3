import time


def dp_shortest_path():
    def tsp(mask, pos):
        if mask == (1 << (n + 1)) - 1:
            # all beepers visited, return to start
            return distance(pos, 0)

        if dp[mask][pos] != -1:
            return dp[mask][pos]

        min_cost = float('inf')
        for next_pos in range(n + 1):
            if mask & (1 << next_pos) == 0:  # If next_pos is not visited
                cost = distance(pos, next_pos) + tsp(mask | (1 << next_pos), next_pos)
                min_cost = min(min_cost, cost)

        dp[mask][pos] = min_cost
        return min_cost

    def distance(a, b):
        return abs(beepers[a][0] - beepers[b][0]) + abs(beepers[a][1] - beepers[b][1])

    scenarios = int(input("Enter number of scenarios: "))
    for _ in range(scenarios):
        # grid size input
        x_size, y_size = map(int, input().split())

        # karel start position
        start_x, start_y = map(int, input().split())

        # no. of beepers
        n = int(input())
        beepers = [(start_x, start_y)]  # Include starting position as beeper 0
        for _ in range(n):
            beepers.append(tuple(map(int, input().split())))

        # initialize DP table
        dp = [[-1] * (n + 1) for _ in range(1 << (n + 1))]

        # solve using TSP
        start_time = time.time()
        result = tsp(1, 0)
        # start from beeper 0
        end_time = time.time()

        print(f"The shortest path has length {result}")
        print(f"Execution time: {end_time - start_time:.6f} seconds")


dp_shortest_path()
"""
use to test. result is 24.

1
10 10
1 1
4
2 3
5 5
9 4
6 5

use to test. result is 12

1
10 10
1 1
3
2 2
3 3
4 4
"""

