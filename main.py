import itertools
import time


def bf_shortest_path():
    scenarios = int(input("Enter number of scenarios: "))
    for _ in range(scenarios):

        x_size, y_size = map(int, input().split())

        # starting position
        start_x, start_y = map(int, input().split())

        # no. of beepers
        n = int(input())
        beepers = []
        for _ in range(n):
            beepers.append(tuple(map(int, input().split())))

        # brute force
        start_time = time.time()
        min_distance = float('inf')  # Start with a very large value

        # iterate
        for perm in itertools.permutations(beepers):
            distance = 0
            current_x, current_y = start_x, start_y

            # calculate distance
            for x, y in perm:
                distance += abs(current_x - x) + abs(current_y - y)
                current_x, current_y = x, y

            # add dist to return to start
            distance += abs(current_x - start_x) + abs(current_y - start_y)

            # update min distance
            min_distance = min(min_distance, distance)

        end_time = time.time()

        # result
        print(f"The shortest path has length {min_distance}")
        print(f"Execution time: {end_time - start_time:.6f} seconds")


bf_shortest_path()

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
