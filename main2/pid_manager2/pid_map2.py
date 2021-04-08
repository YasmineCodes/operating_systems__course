from threading import Lock
MIN_PID = 300
MAX_PID = 5000


class PIDMap():
    min_pid = None
    max_pid = None
    available_pids = None
    # Mutex lock to protect available pids
    av_mutex = Lock()
    pids = None
    # Mutex to proct pids map
    pids_mutex = Lock()

    def __init__(self, min_pid=MIN_PID, max_pid=MAX_PID):
        print("pid_manager_2")
        self.min_pid = min_pid
        self.max_pid = max_pid
        self.available_pids = []  # To improve time complexity of searching for availalb_pid
        self.pids = {}
        self.allocate_map()  # create pids map upon instantiation
        # print("allocate result", x)

    def allocate_map(self):
        ''' allocate_map takes no argumens and creates a PID dictionary with keys 
            min_pid through max_pid. Value at key i equals 0 if i is an availabe PID, and 1 if i is in use. allocate_map fills initial list of available_keys
        '''
        try:
            # Create dictionary with keys in range min_pid through max pid+1, initial values 0
            pid_range = [*range(self.min_pid, self.max_pid+1)]
            self.pids = dict.fromkeys(pid_range, 0)
            # All PIDs will be initial available
            self.available_pids = pid_range
            return 1
        except:
            return -1

    def allocate_pid(self):
        '''
        allocate_pid gets an available PID from available_pids list, removes it from list,
        and updates value for PID in pids map dictionary to 1.
        '''
        try:
            # acquire available pids lock
            self.av_mutex.acquire()
            # Get first available PID and remove it from list
            pid = self.available_pids.pop(0)
            # release av_pids lock
            self.av_mutex.release()

            # acquire pids lock
            self.pids_mutex.acquire()
            self.pids[pid] = 1  # Update value in map
            # release pids locks
            self.pids_mutex.release()

            return (pid, 1)  # success
        except:
            return -1

    def release_pid(self, pid):
        '''
        release_pid accepts a PID to be released, updates the value in the pids map for that pid to 0, appends the pid to available_pids list. 
        '''
        try:
            # Check if pid is already available
            if self.pids[pid] == 0:
                return 1
            # releas_pid otherwise
            self.pids_mutex.acquire()  # aquire pids lock
            self.pids[pid] = 0
            self.pids_mutex.release()  # release pids lock
            self.av_mutex.acquire()  # acquire available pids lock
            self.available_pids.append(pid)
            self.av_mutex.release()  # release av_pids lock
            return 1
        except:
            return -1
