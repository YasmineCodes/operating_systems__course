"""Module implementing First Come First Serve disk-scheduling Algorithm. 
    """


def fcfs(q, head=100):
    # Variable to track total movement in this algorithm
    total_cylinders = 0

    # Iterate through Q, updating total_cylinders
    for _ in range(len(q)):
        address = q.popleft()
        total_cylinders += abs(head-address)
        # update head location
        head = address
    return f'FCFS Algorithm: Total head movement of {total_cylinders} cylinders.'
