import time
import asyncio 
import requests


async def function1():
  print("func 1") 
  URL = "https://imgs.search.brave.com/-dw187VVCPAuWNRUAeYkOVDMznqXWsrsBMFJq8m30cs/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9pMC53/cC5jb20vcGljanVt/Ym8uY29tL3dwLWNv/bnRlbnQvdXBsb2Fk/cy9idWRkaGEtM2Qt/d2FsbHBhcGVyLWZy/ZWUtcGhvdG8uanBn/P3c9NjAwJnF1YWxp/dHk9ODA"
  response = requests.get(URL)
  open("image1.jpg", "wb").write(response.content)
   
  return "Keshav"

  
async def function2():
  print("func 2") 
  URL = "https://imgs.search.brave.com/HrqijVB0GMB_hhrwzlcUEVO63D8tvhPzRwSJ09nJ0zI/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9jNC53/YWxscGFwZXJmbGFy/ZS5jb20vd2FsbHBh/cGVyLzcwNi8xNTcv/MTE2L2F2ZW5nZXJz/LWluZmluaXR5LXdh/ci00ay10aGFub3Mt/d2FsbHBhcGVyLXBy/ZXZpZXcuanBn"
  response = requests.get(URL)
  open("image2.jpg", "wb").write(response.content)

  
async def function3():
  print("func 3")
  URL = "https://imgs.search.brave.com/tU-_zxDar61shubtRlawupKuGcUC3_1pRBUDG09Nctw/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly90NC5m/dGNkbi5uZXQvanBn/LzA2LzIzLzUxLzY5/LzM2MF9GXzYyMzUx/Njk3M19NRlVKVkRt/Vk5oQ1RISG9VVGg4/TDJ0MzlWajRsZ2tY/cy5qcGc"
  response = requests.get(URL)
  open("image3.jpg", "wb").write(response.content)


async def main():
  # await function1()
  # await function2()
  # await function3()
  # return 3
  L = await asyncio.gather(
        function1(),
        function2(),
        function3(),
    )
  print(L)
  # task = asyncio.create_task(function1())
  # # await function1()
  # await function2()
  # await function3()


asyncio.run(main())

'''
Async IO in Python
Asynchronous I/O, or async for short, is a programming pattern that allows for high-performance I/O operations in a concurrent and non-blocking manner. In Python, async programming is achieved through the use of the asyncio module and asynchronous functions.

Syntax
Here is the basic syntax for creating an asynchronous function in Python:

import asyncio
async def my_async_function():
    # asynchronous code here
    await asyncio.sleep(1)
    return "Hello, Async World!"
async def main():
    result = await my_async_function()
    print(result)
asyncio.run(main())
Another way to schedule tasks concurrently is as follows:

L = await asyncio.gather(
        my_async_function(),
        my_async_function(),
        my_async_function(),
    )
print(L)
Async IO is a powerful programming pattern that allows for high-performance and concurrent I/O operations in Python. With the asyncio module and asynchronous functions, you can write efficient and scalable code that can handle large amounts of data and I/O operations without blocking the main thread. Whether you're working on web applications, network services, or data processing pipelines, async IO is an essential tool for any Python developer.
'''
