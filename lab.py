import time
from algorithms import *

def main(n):
    for_loop(n)


if __name__ == "__main__":
    # cleanup the txt file
    with open("result.txt", "w") as f:
        f.write("")

    for i in range(10000):
        start = time.perf_counter()
        main(i)
        end = time.perf_counter()
        with open("result.txt", "a") as f:
            f.write(str(end - start) + "\n")
