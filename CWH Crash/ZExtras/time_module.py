import time 


def usingWhile():
    i = 0
    while i < 50000:
        i = i + 1
        print(i)


def usingFor():
    for i in range(50000):
        print(i)


init = time.time()  # time initialized
usingFor()
t1 = time.time() - init  # to get time taken to run the loop, we need to subtract the intial time with the time taken after the loop

init = time.time()
usingWhile()
t2 = time.time() - init

print(t1)
print(t2)

time.sleep(2)
print("This is printed after 2 seconds")
 
t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
print(formatted_time) 
