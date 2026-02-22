#without westing time how do we run two process at the same time
import multiprocessing
import time
import os
def square_numbers(numbers):
    for i in numbers:
        time.sleep(1.5)
        print(f"the square of {i} is {i*i}", flush=True)
def cube_numbers(numbers):
    for i in numbers:
        time.sleep(2.5)
        print(f"the cube of {i} is {i*i*i}", flush=True)
 
if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    p1 = multiprocessing.Process(target=square_numbers, args=(numbers,))
    p2 = multiprocessing.Process(target=cube_numbers, args=(numbers,))
    t = time.time()
    # Run both processes simultaneously
    p1.start()
    p2.start()
    
    # Wait for both processes to complete
    p1.join()
    p2.join()
    
    finished=time.time()-t
    print(f"finished in {finished} seconds", flush=True)