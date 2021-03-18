The `thread_main.py` module utilizes the `pid_map` module by creating execution threads, each of which is allocated a PID using the `pid_map` module. Upon the conslusion of the execution of the thread, the allocated PID is released.

- `thread_main` script design:
  - Creates `pid_map` using `PIDMap()` initializer
  - `waiting_function` takes one parameter -- the number of seconds to wait -- gets a PID for it's current thread using `PIDMap.allocate_pid()`, outputs the allocated PID, uses the standard python library `time` to wait the given number of seconds, then uses `PIDMap.release_pid()` to release the PID, and outputs that it's finishing execution.
  - `durations` list contains 100 randomely generated durations in seconds, ranging from 1 to 60 seconds
  - A for loop creates a thread that calls the `waiting_function` for each value in the `durations` list, starts each thread, and appends each thread to a `threads` list.
  - A for loop iterates through the `threads` list and joins them to ensure that the script does not continue to execute until the threads are finished executing
  - The script outputs the time duration of the script's execution
  - `thread_main.md` contains `thread_main.py` output including a description of the input to the `waiting_function`, output from the function, as well as a tally of the time spent on script execution.
