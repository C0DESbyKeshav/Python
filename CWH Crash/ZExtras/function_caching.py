# Function Caching
# * Ek baar jiss value ke liye function run ho jaayega toh uss function ka result for that value will be stored in the cache memory so that next time when the user wants to call the function for the same value then instead of running the entire function again, it will just return the result of the function for that value for the cache memory so that the time is saved.

# * The cache gets deleted every time the program is run and the new cache gets stored.

# * When to use the cache function:
# When you know that your function is going to run around limited values only.

# * When not to use the cache function:
# When you know that hardly there will be a value for which the function will run again.

import functools
import time


@functools.lru_cache(maxsize=None)
def expensive_function(arg):
    # Some heavy computation that takes an argument and returns a result
    time.sleep(3)
    return arg * 2
    

print(expensive_function(20))
print("done for 20")
print(expensive_function(2))
print("done for 2")
print(expensive_function(6))
print("done for 6\n")

print(expensive_function(20))
print("done for 20")
print(expensive_function(2))
print("done for 2")
print(expensive_function(6))
print("done for 6")
print(expensive_function(61))
print("done for 61")

# Function Caching in Python
# Function caching is a technique for improving the performance of a program by storing the results of a function call so that you can reuse the results instead of recomputing them every time the function is called. This can be particularly useful when a function is computationally expensive, or when the inputs to the function are unlikely to change frequently.

# In Python, function caching can be achieved using the functools.lru_cache decorator. The functools.lru_cache decorator is used to cache the results of a function so that you can reuse the results instead of recomputing them every time the function is called. Here's an example:

# import functools
# @functools.lru_cache(maxsize=None)
# def fib(n):
#     if n < 2:
#         return n
#     return fib(n-1) + fib(n-2)
# print(fib(20))

# As you can see, the functools.lru_cache decorator is used to cache the results of the fib function. The maxsize parameter is used to specify the maximum number of results to cache. If maxsize is set to None, the cache will have an unlimited size.

# Benefits of Function Caching
# Function caching can have a significant impact on the performance of a program, particularly for computationally expensive functions. By caching the results of a function, you can avoid having to recompute the results every time the function is called, which can save a significant amount of time and computational resources.

# Another benefit of function caching is that it can simplify the code of a program by removing the need to manually cache the results of a function. With the functools.lru_cache decorator, the caching is handled automatically, so you can focus on writing the core logic of your program.

# Conclusion
# Function caching is a technique for improving the performance of a program by storing the results of a function so that you can reuse the results instead of recomputing them every time the function is called. In Python 3, function caching can be achieved using the functools.lru_cache decorator, which provides an easy and efficient way to cache the results of a function. Whether you're writing a computationally expensive program, or just want to simplify your code, function caching is a great technique to have in your toolbox.
