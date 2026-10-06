def bubble_sort(values):
    """Return a sorted copy of the values."""
    result = values.copy()

    for end in range(len(result) - 1, 0, -1):
        for i in range(end):
            if result[i] > result[i + 1]:
                result[i], result[i + 1] = result[i + 1], result[i]

    return result


print(bubble_sort([5, 1, 4, 2, 8]))