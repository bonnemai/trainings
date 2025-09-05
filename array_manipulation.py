def array_manipulation(n, queries):
    """Return the maximum value after applying inclusive range additions.

    Uses a difference-array technique for O(n + q) performance.

    Parameters
    - n: length of the 1-indexed array (filled with zeros initially)
    - queries: iterable of (a, b, k) where k is added to indices a..b inclusive
    """

    # Difference array with two extra slots to safely handle b + 1 index
    difference = [0] * (n + 2)

    for a, b, k in queries:
        difference[a] += k
        difference[b + 1] -= k

    running_total = 0
    max_value = 0
    for i in range(1, n + 1):
        running_total += difference[i]
        if running_total > max_value:
            max_value = running_total

    return max_value


if __name__ == "__main__":
    # Example from the prompt
    n = 10
    queries = [(1, 5, 3), (4, 8, 7), (6, 9, 1)]
    print(array_manipulation(n, queries))  # Expected: 10


