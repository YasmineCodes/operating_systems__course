### Disk Scheduling

Disk scheduling algorithms enable the operating system to manage disk resources. Disk scheduling algorithms are optimize to address the following goals:

- Minimize seeks time
- Maximize disk bandwidth

These python module simulate and implement common disk scheduling algorithms.The following implementations assume available disk addresses in `0-4999`.

The `fcfs` python file contains an implementation of the _first come first serve_ disk shceduling algorithm. The function receives a queue containing the addresses of disk locations to be visited by the read/write head and it receives the address of the starting position of the read/write head. The function then "visits" each location listed in the queue on a first come first serve basis, while keeping track of the total distance traveled by the read/write head in the process. The total distance (i.e. number of tracks traversed) is returned to the caller.

The `sstf` module contains an implementation of the _Shortest Seek Time First_ algorithm. The `sstf` function receives a list of the addresses of disk locations to be visited by the read/write head as well as a starting location of the read/write head. The function uses a helper `find_nearest` function which returns the index of the address neares to the current location of the read/write head. This function traverses from each location to the closes listed one in the queue until they have all been visited. This function returns the total number of tracks traversed to the caller.

The `scan` module implements the _Scan_ disk scheduling algorithm. The `scan` function receives a queue containing the addresses of disk locations to be visited by the read/write head, a direction for the read/write head to travel first, and the address of the starting location of the read/write head. If the direction is a positive number, the `scan_up` function is called. While the queue of addresses has items, the function _scans_ the disk starting at the starting position of the head passed in then goin up until it reaches the highest address, visiting each address in the queue on the way. The function then traverses back in the other direction, until there are not more addresses in the queue. The function returns the total number of tracks traversed to the caller.

The `disk_scheduling_main` file contains code that utilizes the disk scheduling algorithms described above. The main function writes out the results from each function to the `disk_scheduling_output` file. All functions are passed a starting read/write head location of `100` and they're all passed the same queue of disk addresses.
