"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

def findMedian(list):
    list.sort()
    length = len(list)

    if length%2 != 0:
        median = list[length//2]
    else:
        median = (list[int(length/2)]+list[int((length/2))-1])/2

    print(f'Median value is --> {median}')


while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        findMedian(numbers)
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

