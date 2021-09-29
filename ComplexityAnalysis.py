# Discrete Structures Bubble and Selection Sort Timing
import time
from random import randint

                            # PART 1 OF TERM PROJECT#
start = time.process_time()
# Bubble Sort
list1 = []
bubbleInput = int(input("Enter the size of the array for Bubble Sort: "))
# valueArr = (random.randint(1, 100))
for _ in range(bubbleInput):
    list1.append(randint(1,100))
    def bubbleSort (list1):
        for i in range(len(list1)):
            for j in range(len(list1)-1):
                if list1[j] > list1[j+1]:
                    list1[j], list1[j+1] = list1[j+1], list1[j]
print (list1)
bubbleSort(list1)
print (list1)
print()
print("Bubble Sort took",(time.process_time()-start), " seconds to complete.")

print()
print()

                            # PART 2 OF TERM PROJECT
start = time.process_time()
# Selection Sort
list2 = []
# value2Arr = (random.randint(1,100,10))
selectionInput = int(input("Enter the size of the array for Selection Sort: "))
for _ in range(selectionInput):
    list2.append(randint(1,100))
    def selectionSort(list2):
        for i in range(len(list2)):
            minimum = i
            for j in range(i+1, len(list2)):
                if list2[minimum] > list2[j]:
                    minimum = j
            list2[i], list2[minimum] = list2[minimum], list2[i]
        
print(list2)
selectionSort(list2)
print(list2)
print()
print("Selection Sort took",(time.process_time()-start), " seconds to complete.")

print()
print()

                            # PART 3 OF TERM PROJECT
# Bubble Sort of Part 3 with Large Numbers                            
list3 = []
bubbleInputN = int(input("Enter a number to create the array size: "))
runningTime = 0
for _ in range(1000):
    list3 = [randint(1,10*bubbleInputN) for _ in range(bubbleInputN)]
    # Bubble Sort of Created Array
    def bubbleSort (list3):
        start = time.process_time()
        for i in range(len(list3)):
            for j in range(len(list3)-1):
                if list3[j] > list3[j+1]:
                    list3[j], list3[j+1] = list3[j+1], list3[j]

print(list3)
bubbleSort(list3)
print(list3)
bubbleSortTime = (time.process_time()-start)
print()
print("Bubble Sort of Large Array of Numbers took ",bubbleSortTime, " seconds to complete.")

print()
print()

# Selection Sort of Part 3 with Large numbers
list4 = []
selectionInput = int(input("Enter the size of the array for Selection Sort: "))
runningTime = 0
for _ in range(1000):
    list4 = [randint(1,10*selectionInput) for _ in range(selectionInput)]
    def selectionSort(list4):
        start = time.process_time()
        for i in range(len(list4)):
            minimum = i
            for j in range(i+1, len(list4)):
                if list4[minimum] > list4[j]:
                    minimum = j
            list4[i], list4[minimum] = list4[minimum], list4[i]
        
print(list4)
selectionSort(list4)
print(list4)
selectionSortTime = (time.process_time()-bubbleSortTime)
print()
print("Selection Sort of Large Array of Numbers took",selectionSortTime, " seconds to complete.")



