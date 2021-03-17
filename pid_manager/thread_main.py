import random
import threading
import time
from pid_map import PIDMap

start = time.perf_counter()  # To keep track of the time used to run this script

# Create PID map for this script
pids = PIDMap()
output_file = open("threads_log_file.txt", 'w')


def waiting_function(duration):
    '''Function that waits the given number of seconds'''
    x = pids.allocate_pid()

    if x != -1:
        my_key = x[0]
        output_file.write(
            f'Sleeping {duration} second(s)..., PID: {my_key} \n')
        time.sleep(duration)
        pids.release_pid(my_key)
        output_file.write(f'Done sleeping...for {duration} second(s), released PID: {my_key} \n'
                          )


# List containing 100 random time durations in seconds between 1 and 60 seconds
durations = [random.randint(1, 60) for _ in range(100)]

# print max duration and sum of durations
output_file.write(
    f'The longest duration in these threads is {max(durations)} seconds. The sum of all thread durations is {sum(durations)} seconds. The threaded calls should take {max(durations)} secondss, rather than the sum of of the durations.\n')


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
output_file.write(f'Finished in {round(finish-start, 2)} second(s) \n')
