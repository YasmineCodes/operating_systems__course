"""Module utilizing disk scheduling algorithms and writing out algorithm output.
    """
from fcfs import fcfs
from sstf import sstf
from scan import scan
import collections
START = 100
DIRECTION = 1  # -1 for left/down
DISK_Q = collections.deque([4078, 153, 2819, 3294, 1433, 211, 1594, 2004, 2335, 2007, 771, 1043, 3950, 2784, 1881, 2931, 3599, 1245, 4086, 520, 3901, 2866, 947, 3794,
                            2353, 3970, 3948, 1815, 4621, 372, 2684, 3088, 827, 3126, 2083, 584, 4420, 1294, 917, 2881, 3659, 2868, 100, 1581, 4581, 1664, 1001, 1213, 3439, 4706])

OUTPUT = open("./disk_scheduling_output.txt", 'w')


def main():
    OUTPUT.write(f"{fcfs(collections.deque(DISK_Q), START)} \n")
    OUTPUT.write(f"{sstf(list(DISK_Q), START)} \n")
    OUTPUT.write(f"{scan(list(DISK_Q), DIRECTION, START)} \n")


if __name__ == "__main__":
    main()
