# Define a 2D warehouse layout (for reference, not needed by logic)
warehouse_grid = [
    [0 for _ in range(10)]
    for _ in range(10)
]

# Coordinates of boxes in sets
box_sets = [
    [(1, 1), (1, 2), (1, 3), (1, 4)],  # Line 1
    [(2, 1), (2, 2), (2, 3), (2, 4)],  # Line 2
    [(3, 1), (3, 2), (3, 3), (3, 4)]   # Line 3, etc.
]