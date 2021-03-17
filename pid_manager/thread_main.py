import random
import threading
import time
from pid_map import PIDMap

start = time.perf_counter()  # To keep track of the time used to run this script

# Create PID map for this script
pids = PIDMap()


def waiting_function(duration):
    '''Function that waits the given number of seconds'''
    x = pids.allocate_pid()

    if x != -1:
        my_key = x[0]
        print(f'Sleeping {duration} second(s)..., PID: {my_key}')
        time.sleep(duration)
        pids.release_pid(my_key)
        return f'Done sleeping...for {duration} second(s), released PID: {my_key}'


# List containing 100 random time durations in seconds between 1 and 60 seconds
durations = [random.randint(1, 60) for _ in range(100)]

# List to store threads
threads = []

# loop through list with random durations creating a thread with each
for dur in durations:
    t = threading.Thread(target=waiting_function, args=[dur])
    t.start()
    threads.append(t)

# Join threads so program doesn't conclue befor they're done
for thread in threads:
    thread.join()

# Calc and print execution time of this script
finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)')
