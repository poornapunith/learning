"""

Duplicate Number
Write a function to remove the duplicate numbers on given integer array/list.

Example

remove_duplicates([1, 1, 2, 2, 3, 4, 5])
Output : [1, 2, 3, 4, 5]

"""

def remove_duplicates(mainList):
    outputList=[]
    for i in mainList:
        if i not in outputList:
            outputList.append(i)
    return outputList

print(remove_duplicates([1, 1, 2, 2, 3, 4, 5]))
