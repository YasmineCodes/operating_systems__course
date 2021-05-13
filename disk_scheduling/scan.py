"""This module implements the scan disk-scheduling algorithm.
    """
TRACKS = range(200)


def scan(q, direction, head=100):
    if direction > 0:
        return f'Scan algorithm: Total head movement of {scan_up(q, head)} cylinders'
    return scan_down(q, head)


def scan_up(q, head):
    total_cylinders = 0
    start = head
    while q:
        for address in TRACKS[start+1:]:
            total_cylinders += 1
            head = address
            if address in q:
                q.remove(address)
        start = head
        for address in TRACKS[start-1:max(min(q)-1, min(TRACKS)):-1]:
            total_cylinders += 1
            head = address
            if address in q:
                q.remove(address)
    return total_cylinders


def scan_down(q, head):
    return
