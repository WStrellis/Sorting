from basic_recursion import *
import time
import random
import statistics


# create array of test arrays
test_array = [random.sample(range(0, 2000), 100) for x in range(0, 100)]


def timed(f, a, i):
    start = time.time()
    f(a, i)
    end = time.time()
    return end - start


# run both recursive functions 100 times and get time
rl1_time = statistics.mean(
    [timed(recursive_linear, x, random.randint(0, 100)) for x in test_array])

rl2_time = statistics.mean(
    [timed(recursive_linear_alt, x, random.randint(0, 100)) for x in test_array])
# calculate average run time for both and display
print(f"Popping item from end: {rl1_time}")
print(f"Popping item from beginning: {rl2_time}")
