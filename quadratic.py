def quadratic(arr: list[int]) -> int:
    pairs = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            pairs = pairs + 1
    return pairs

print(quadratic([1, 2, 3, 4, 5]))