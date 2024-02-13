"""
Rotate Matrix/ Image - LeetCode 48
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.

DO NOT allocate another 2D matrix and do the rotation.

Example:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
"""

def Rotate_Matrix(l):
    
    for i in range(len(l)):
        for j in range(i,len(l)):
            l[i][j],l[j][i]=l[j][i],l[i][j]

    for i in l:
        i.reverse()
        
    return l

print(Rotate_Matrix([[1,2,3],[4,5,6],[7,8,9]]))
