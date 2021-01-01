# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 22:39:41 2020

@author: pulkit
"""


# defining a class Queue
class Queue:

    def __init__(self):
        self.queue = []

    def put(self, item):
        self.queue.append(item)

    def get(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def front(self):
        return self.queue[0]

    def size(self):
        return len(self.queue)

    def empty(self):
        return not (len(self.queue))

    # Function to push element in last by popping from front until size becomes 0


def FrontToLast(q, qsize):
    # Base condition
    if qsize <= 0:
        return

    # pop front element and push this last in a queue
    q.put(q.get())

    # Recursive call for pushing element
    FrontToLast(q, qsize - 1)


# Function to push an element in the queue while maintaining the sorted order
def pushInQueue(q, temp, qsize):
    # Base condition
    if q.empty() or qsize == 0:
        q.put(temp)
        return

    # If current element is greater than the element at the front
    elif temp >= q.front():
        # Call stack with front of queue
        q.put(temp)

        # Recursive call for inserting a front
        # element of the queue to the last
        FrontToLast(q, qsize)

    else:
        # Push front element into last in a queue
        q.put(q.get())

        # Recursive call for pushing element in a queue
        pushInQueue(q, temp, qsize - 1)

    # Function - Using recursion technique to sort queue (time complexity O(n))


def sortQueue(q):
    # Nothing to do if Queue is empty
    if q.empty():
        return

    # Get the front element which will be stored in this variable throughout the recursion stack
    temp = q.get()

    # Recursive call
    sortQueue(q)

    # Push the current element into the queue according to the sorting order
    pushInQueue(q, temp, q.size())


######################################
# Actual assignment code logic

def main():
    disk_queue = Queue()  # create a new Queue object
    diskcount = int(input())
    discsizes = list(map(int, input().split()))

    # initialise the max disk size since we know from assignment requirement N is max
    max_disksize = diskcount

    # Loop once across the disc size LIST  and then use Queue data structure to perform
    # various operations as given in the assignment problem statement

    for day, size in enumerate(discsizes):
        disk_queue.put(size)
        if size == max_disksize:
            # sortQueue(disk_queue)
            # loop with specific conditions
            while (not disk_queue.empty()) and disk_queue.front() == max_disksize:
                disk = disk_queue.get()
                max_disksize -= 1
                print(disk, end=' ')
        print()


if __name__ == "__main__":
    main()
