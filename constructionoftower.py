# numberOfDisk = int(input("Enter the number of disk"))
# tempDiskOfDaysStringArray = input("Enter the size of disk by days").split(' ')

numberOfDisk = 6
tempDiskOfDaysStringArray = ['4', '13', '5', '1', '2', '3']

sizeOfDisk = []
for i in range(0, len(tempDiskOfDaysStringArray)):
    sizeOfDisk.append(int(tempDiskOfDaysStringArray[i].strip()))

def isAnyGreaterDiskPresent(sizeOfDisk, index, item):
    isGreaterDiskPresent = False
    diskSize = -1
    for i in range(index, numberOfDisk):
        if sizeOfDisk[i] >= item:
            isGreaterDiskPresent = True
            diskSize = sizeOfDisk[i]
            break
    return isGreaterDiskPresent, diskSize

queue = list()
for i in range(0, numberOfDisk):
    queue.append(sizeOfDisk[i])
    isGreaterDiskPresent, diskSize = isAnyGreaterDiskPresent(sizeOfDisk, i + 1, sizeOfDisk[i])
    if not isGreaterDiskPresent:
        queue.sort(reverse=True)
        print(queue)
        queue.clear()


