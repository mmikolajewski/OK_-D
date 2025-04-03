import time
from tsp_solver import solve_tsp

def read_points(filepath):
    points = []
    with open(filepath, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 3:
                _, x, y = parts
                points.append((float(x), float(y)))
    return points

def main():
    filename = "points_01.txt"
    points = read_points(filename)

    start_index = 1

    start_time = time.perf_counter_ns()
    path, dist = solve_tsp(points, start_index - 1)
    end_time = time.perf_counter_ns()

    print("Najkrótsza trasa:", ' -> '.join(map(str, path + [path[0]])))
    print("Długość:", round(dist, 4))
    print(f"Czas wykonania: {end_time - start_time} ns")

if __name__ == "__main__":
    main()
