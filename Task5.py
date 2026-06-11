import time #time4eva


def climb_recursive(n: int) -> int:
    if n <= 1:
        return 1
    return climb_recursive(n - 1) + climb_recursive(n - 2)


def climb_iterative(n: int) -> int:
    if n <= 1:
        return 1

    prev2 = 1
    prev1 = 1

    for i in range(2, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current

    return prev1


def measure(func, n: int):
    start = time.perf_counter()
    result = func(n)
    end = time.perf_counter()
    return result, end - start


def main():
    test_cases = [10, 20, 30, 35]

    for n in test_cases:
        rec_result, rec_time = measure(climb_recursive, n)
        itr_result, itr_time = measure(climb_iterative, n)

        print(f"n = {n}")
        print(f"  recursive:  {rec_result} ways,  {rec_time:.6f}s")
        print(f"  iterative:  {itr_result} ways,  {itr_time:.6f}s")
        print()


main()