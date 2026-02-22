#how do single thread work?
import time 
import os
import threading

def square_numbers(numbers):
    for i in numbers:
        time.sleep(1.6)
        print(f"the square of {i} is {i*i}", flush = True)

def cube_numbers(numbers):
    for i in numbers:
        time.sleep(2.5)
        print(f"the cube of {i} is {i*i*i}", flush = True)

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    t1 = threading.Thread(target=square_numbers, args=(numbers,))
    t2 = threading.Thread(target=cube_numbers, args=(numbers,))
    t = time.time()
    # Run t1 first and wait for it to complete
    t1.start()
    t1.join()
    
    # Then run t2
    t2.start()
    t2.join()
    
    finished=time.time()-t
    print(f"finished in {finished} seconds", flush=True)