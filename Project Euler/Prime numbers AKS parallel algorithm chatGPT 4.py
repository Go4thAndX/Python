import concurrent.futures
import math
import time


def is_prime(n, lo, hi):
    for i in range(lo, hi + 1):
        if n % i == 0:
            return False
    return True


def aks_parallel(n, num_threads=4):
    if n == 2 or n == 3:
        return True
    if n == 1 or n % 2 == 0:
        return False

    sqrt_n = int(math.sqrt(n)) + 1
    thread_ranges = [
        (i * sqrt_n // num_threads + 2, (i + 1) * sqrt_n // num_threads)
        for i in range(num_threads)
    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(
            executor.map(lambda rng: is_prime(n, rng[0], rng[1]), thread_ranges)
        )

    return all(results)


def find_prime(initial):
    while True:
        start_time = time.perf_counter()
        is_prime = aks_parallel(initial)
        end_time = time.perf_counter()
        processor_time = end_time - start_time

        file_name = "Priemgetallen volgens het AKS algoritme.txt"
        with open(file_name, "w") as bestand:
            if is_prime:
                print(
                    f"{initial} is a prime number. Processor time: {processor_time:.6f} seconds"
                )
                print(
                    f"{initial} is a prime number. Processor time: {processor_time:.6f} seconds",
                    file=bestand,
                )
                break
            else:
                print(
                    f"{initial} is not a prime number. Processor time: {processor_time:.6f} seconds"
                )

                initial -= 1

    print("De uitvoer is opgeslagen in het bestand:", file_name)


if __name__ == "__main__":
    # 600.851.475.143
    initial_number = 600851475143
    find_prime(initial_number)
