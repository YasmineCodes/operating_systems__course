An operating system’s **pid manager** is responsible for managing process identifiers. Upon the creation of a process, it is assigned a unique Process ID by this proccess ID manager. The PID is returned to the PID manager, via the `release_pid` method, when the process completes execution, and the manager may later reassign this PID. Process identifiers must be unique; no two active processes may have the same pid.

This implementation of a process ID manager has the following constants to identify the range of possible PID values:

    MIN_PID = 300
    MAX_PID = 5000

This process ID manager in wraped in a class called `PIDMap` and uses the combination of two data structures, for optimization of time complexity. The first is a Python Dictionary called `pids`, which contains the keys in the range stated above. Each key/ID will have either the value 0 or 1, with 0 indicating that the key/ID is available and 1 indicating that it is in use. Additionally a list called `available_pids` contains all available PIDs, i.e. all PIDs that have a value 0 in the dictionary and are not in use. Initially the list contains all possible IDs but shrinks as PIDs are allocated. This makes the process of finding an available ID more time efficient than the alternative of searching through the `pids` dictionary for a key which has the value 0, while the `pids` dictionary still makes it possible to update the value of a PID in O(1) time and leaves the possibility of storing additional relevant details for PID if needed in the future.

- The class `PID_map` contains the following methods for creating a map containing PIDs, allocating PIDs, and tracking the availability of PIDs
  - `allocate_map(None) -> int` Takes no arguments. It creates and initializes the `pids` dictionary with keys in range 300 to 5000, inclusive. The values for all keys are initialized to 0, representing availability. The method returns -1 if unsuccessful and 1 if successful.
  - `allocate_pid(None) -> (int, int)` Takes no arguments. It allocates an available PID by popping (removing and returning) the first PID in the `available_pids` list and updating the PID's value in the `pids` dictionary to 1. It returns a tuple containing 1 if successful along with the allocated PID. It returns -1 if unsuccessful or if no PIDs are available.
  - `release_pid(pid:int) -> None` Takes a PID as an argument. It releases the given PID by changing the value of the PID in the `pids` dictionary to 0 and appending the given PID to the `available_pids` list.
