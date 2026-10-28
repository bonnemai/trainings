import threading
from collections.abc import Callable
from concurrent.futures import ThreadPoolExecutor


def fizzbuzz_mt(n: int = 100) -> None:
    """Print FizzBuzz from 1 to n using four synchronized threads."""
    condition = threading.Condition()
    current = 1

    def worker(should_print: Callable[[int], bool], text: str = "") -> None:
        nonlocal current

        while True:
            with condition:
                condition.wait_for(lambda: current > n or should_print(current))

                if current > n:
                    condition.notify_all()
                    return

                print(text if text else current)
                current += 1
                condition.notify_all()

    workers = [
        threading.Thread(
            target=worker,
            args=(lambda value: value % 15 == 0, "FizzBuzz"),
            name="fizzbuzz",
        ),
        threading.Thread(
            target=worker,
            args=(lambda value: value % 3 == 0 and value % 5 != 0, "Fizz"),
            name="fizz",
        ),
        threading.Thread(
            target=worker,
            args=(lambda value: value % 5 == 0 and value % 3 != 0, "Buzz"),
            name="buzz",
        ),
        threading.Thread(
            target=worker,
            args=(lambda value: value % 3 != 0 and value % 5 != 0,),
            name="number",
        ),
    ]

    for thread in workers:
        thread.start()

    for thread in workers:
        thread.join()


def fizzbuzz_pool(n: int = 100, max_workers: int = 4) -> None:
    """Print FizzBuzz using a ThreadPoolExecutor."""

    def format_value(value: int) -> str:
        if value % 15 == 0:
            return "FizzBuzz"
        if value % 3 == 0:
            return "Fizz"
        if value % 5 == 0:
            return "Buzz"
        return str(value)

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # map() returns results in the same order as the input iterable.
        results = executor.map(format_value, range(1, n + 1))
        for result in results:
            print(result)


if __name__ == "__main__":
    fizzbuzz_pool()
