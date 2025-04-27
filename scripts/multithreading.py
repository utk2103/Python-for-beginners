import time  # Why: To measure time and add delays
import threading  # Why: To run code in parallel threads

def calculate_square(numbers):
    print("calculate square numbers")
    for n in numbers:
        time.sleep(1)  # Why: Simulate heavy work
        print('square:', n*n)

def calculate_cube(numbers):
    print("calculate cube of numbers")
    for n in numbers:
        time.sleep(1)
        print('cube:', n*n*n)

arr = [2,3,8,9]  # Why: Example data

t = time.time()  # Why: Track elapsed time

t1 = threading.Thread(target=calculate_square, args=(arr,))  # Why: Run square in parallel
t2 = threading.Thread(target=calculate_cube, args=(arr,))    # Why: Run cube in parallel

t1.start()
t2.start()

t1.join()
t2.join()

print("done in : ", time.time()-t)  # Why: Show speedup from threads
