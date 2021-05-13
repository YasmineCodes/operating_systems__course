"""This module implements the Shortest Seek Time First disk-scheduling algorithm. 
    """


def sstf(q, head=100):
    # initialize var to track cylinders traveled in this algorithm
    total_cylinders = 0

    # iterate through q
    for _ in range(len(q)):
        next = find_nearest(q, head)
        head = q[next[0]]
        total_cylinders += next[1]
        q.pop(next[0])
    return f'SSTF Algorithm: Total head movement of {total_cylinders} cylinders.'


def find_nearest(q, head):
    """Function finds the nearest address listed in the disk-scheduling q

    Args:
        q (list or tuple): q in which to find the neares address
        head (int): current location of read/write head 

    Returns:
        Tuple: contain the index of the neares address in the q and the distanc between head location and address
    """

    # initialize nearest address
    index_nearest = 0
    # initialize distance to nearest
    dist = abs(q[index_nearest]-head)

    # return if only one element in q
    if len(q) < 2:
        return (index_nearest, dist)
    
    #otherwise finde nearest address list 
    for i in range(1, len(q)):
        if abs(q[i]-head) < dist:
            dist = abs(q[i]-head)
            index_nearest = i
    return (index_nearest, dist)
