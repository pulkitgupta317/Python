# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 22:39:41 2020

@author: pulkit
"""

from os import path

# Constants
inputFile = 'inputPS3.txt'
outputFile = 'outputPS3.txt'


# Queue class for handling operations of a queue
class Queue:
    def __init__(self):
        self.queue = []

    # append an element in the queue at the end
    def enqueue(self, item):
        self.queue.append(item)

    # remove an element from the front of the queue
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    # return whether the queue is empty or not
    def empty(self):
        return not (len(self.queue))

    # check if the item is present in the queue or not. dequeue and enqueue the elements till either the element found
    # or the whole queue is traversed
    def present(self, item):
        if not self.empty():
            i = 0
            while i < len(self.queue):
                if self.queue[0] == item:
                    return True
                else:
                    self.enqueue(self.dequeue())
                i += 1
        return False

    # generate string from the queue elements
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])


# Construct a tower in N days with N disks
def diskTower(disks, countOfDays):
    buffer_list = Queue()
    out_list = Queue()
    # traverse through the disks
    for disk_size in disks:
        # add the disk to the list
        buffer_list.enqueue(disk_size)
        # if we are on the biggest disk
        if disk_size == countOfDays:
            temp_list = Queue()
            # run the loop while the countOfDays ( biggest disk ) present in the buffer list
            while buffer_list.present(countOfDays):
                # dequeue the disk and enqueue it in the temp list
                buffer_list.dequeue()
                temp_list.enqueue(countOfDays)
                # reduce the biggest disk by 1 since it has been processed
                countOfDays -= 1
            out_list.enqueue(temp_list)
        else:
            out_list.enqueue(Queue())
    return out_list


# DiskTowerModel class is used for handling and validating the input data
class DiskTowerModel:
    def __init__(self):
        self.countOfDays = None
        self.discSizes = None
        self.error = None
        self.errorMessage = None

    def set(self, countOfDays, discSizes):
        self.discSizes = discSizes
        self.countOfDays = countOfDays
        self.error = False

    def setErrorMessage(self, message):
        self.error = True
        self.errorMessage = message

    def setValues(self, lines):
        # At least 2 lines should be there to process the input
        if lines is None or len(lines) < 2:
            self.setErrorMessage('Please enter 2 lines')
        else:
            countOfDays = lines[0].strip()
            # First line should be a digit only
            if not countOfDays.isdigit():
                self.setErrorMessage('Invalid count of days')
            else:
                countOfDays = int(countOfDays)
                discSizes = lines[1].strip()
                try:
                    # 2nd line should have values ranging from 1 to CountOfDays, all digits
                    discSizes = list(map(int, discSizes.split()))
                    res = all(0 < ele <= countOfDays for ele in discSizes)
                    # Check if there is any disc size which is not in the range mentioned in above comment
                    if not res:
                        self.setErrorMessage('One or many disc are not in the range')
                    # Check if the disc size list having the count same as the countOfDays
                    elif len(discSizes) < countOfDays:
                        self.setErrorMessage('Disc size mentioned are less than N')
                    else:
                        # Check if the disc size mentioned are more than the countOfDays
                        if len(discSizes) > countOfDays:
                            # remove the other elements
                            discSizes = discSizes[:countOfDays]
                        self.set(countOfDays, discSizes)
                except:
                    self.setErrorMessage('Invalid disc sizes')

# Write the data into the output file
def writeIntoFile(data):
    try:
        # open the connection for the file
        f = open(outputFile, "w")
        # calling the
        f.write(data)
        f.close()
    except:
        print('Error occurred in writing the data into the file')

def readFromFile():
    obj = DiskTowerModel()
    if path.exists(inputFile):
        try:
            f = open(inputFile, 'r')
            lines = f.readlines()
            f.close()
            obj.setValues(lines)
        except:
            obj.setErrorMessage('Error occurred in reading the data from the file')
    else:
        obj.setErrorMessage('File does not exist')
    return obj


data = readFromFile()
if data.error:
    writeIntoFile(data.errorMessage)
else:
    out_ = diskTower(data.discSizes, data.countOfDays)
    listOfString = []
    while not out_.empty():
        listOfString.append(str(out_.dequeue()))
    writeIntoFile('\n'.join(listOfString))
