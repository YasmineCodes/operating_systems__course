import unittest
from pid_map import PIDMap


class PIDMapTest(unittest.TestCase):

    def setUp(self) -> None:
        self.pid_map = PIDMap()
        self.output_file = open('test_log_file.txt', 'a')

    def test_pid_min(self):
        self.output_file.write("Testing min PID value equals 300... \n")
        self.assertEqual(self.pid_map.min_pid, 300)

    def test_pid_max(self):
        self.output_file.write("Testing max PID value equals 5000... \n")
        self.assertEqual(self.pid_map.max_pid, 5000)

    def test_pid_map(self):
        self.output_file.write(
            "Testing to ensure all values from 300 to 5000 are in PID Map... \n")
        for i in range(300, 5001):
            self.assertTrue(i in self.pid_map.pids)

    def test_pid_map_values(self):
        self.output_file.write(
            "Testing to ensure that all PIDs are initially set to 0, i.e. available... \n")
        # if successful, non of the PIDs in the map will have value 1
        self.assertFalse(1 in self.pid_map.pids.values())

    def test_allocate_pid(self):
        self.output_file.write("Testing PID allocation: \n")
        x = self.pid_map.allocate_pid()
        if x != -1:
            self.output_file.write(
                "Allocate Map returned 1, for successful.\n")
            # if successful one of the items in the PIDS map will have 1 as a value
            # and the pid will no longer be in the available_pids list
            self.output_file.write(
                "Testing that allocation cause update in PID Map and available PIDs list...\n ")
            my_key = x[0]
            self.output_file.write(f"Allocated PID: {my_key}")
            self.assertTrue(self.pid_map.pids[my_key] == 1 and
                            my_key not in self.pid_map.available_pids)

    def test_release_pid(self):
        self.output_file.write("Testing release_pid... \n")
        x = self.pid_map.allocate_pid()
        if x != -1:
            my_key = x[0]
            self.output_file.write(
                f'Allocated PID {my_key}, releasing this PID...\n')
            y = self.pid_map.release_pid(my_key)
            if y != -1:
                self.output_file.write(
                    "Method release_pid returned 1 for success... \nTesting to ensure PID value is updated to 0 and PID is added to available_pids... \n")
                # if successful my_key should have value of 0 in pids and should be in available pids list
                self.assertTrue(self.pid_map.pids[my_key] == 0
                                and my_key in self.pid_map.available_pids)


if __name__ == '__main__':
    log_file = 'test_log_file.txt'
    with open(log_file, "a") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
