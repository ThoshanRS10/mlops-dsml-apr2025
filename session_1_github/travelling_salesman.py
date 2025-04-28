import itertools

def solve_tsp_brute_force(distances):
    """
    Solves the Travelling Salesman Problem using brute force.
    
    Parameters:
        distances (list of list of int): A 2D matrix where distances[i][j] represents
                                         the distance from city i to city j.
    
    Returns:
        tuple: A tuple containing the minimum distance and the optimal path.
    """
    num_cities = len(distances)
    cities = range(num_cities)
    min_distance = float('inf')
    best_path = None

    for perm in itertools.permutations(cities):
        current_distance = 0
        for i in range(num_cities - 1):
            current_distance += distances[perm[i]][perm[i + 1]]
        current_distance += distances[perm[-1]][perm[0]]  # Return to the starting city

        if current_distance < min_distance:
            min_distance = current_distance
            best_path = perm

    return min_distance, best_path

# Example usage with a dummy distance matrix
if __name__ == "__main__":
    dummy_distances = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    min_dist, path = solve_tsp_brute_force(dummy_distances)
    print(f"Minimum Distance: {min_dist}")
    print(f"Optimal Path: {path}")