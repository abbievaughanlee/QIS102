# bubble_sort.py



import random
import time


#sort through an array of numbers and compare them to each other one by one
def bubble_sort(values):
    last_index = len(values) - 1
    is_sorted = False
    #continue sorting
    while not is_sorted:
        swap_needed = False
        for i in range(last_index):
            #compare adjacent values
            if values[i] > values[i + 1]:
                # Swap adjacent values
                values[i], values[i + 1] = values[i + 1], values[i]
                swap_needed = True
        if not swap_needed:
            is_sorted = True
        else:
            last_index -= 1
    return values

#sort 10_000 numbers
def main():
    random.seed(2016)

    num_samples = 10_000
    print(f"Bubble Sort {num_samples:,} random samples...")

    samples = [random.randint(1, 10_000) for _ in range(num_samples)]

    print("UNSORTED")
    print(f"{samples[:10]} ... {samples[-10:]}")

    start_time = time.perf_counter()
    samples = bubble_sort(samples)
    elapsed_time = time.perf_counter() - start_time

    print("SORTED")
    print(f"{samples[:10]} ... {samples[-10:]}")

    print(f"Total run time (sec): {elapsed_time:.3f}\n")


main()
