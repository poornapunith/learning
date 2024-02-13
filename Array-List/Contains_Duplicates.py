"""
Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example :

Input: nums = [1,2,3,1]
Output: true

"""

def contains_duplicates(nums):
    s=[]
    for i in nums:
        if i in s:
            return True
        else:
            s.append(i)
    return False

print(contains_duplicates([1,2,3,1]))