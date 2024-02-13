"""

Pairs
Write a function to find all pairs of an integer array whose sum is equal to a given number. Do not consider commutative pairs.

Example

pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7)
Output : ['2+5', '4+3', '3+4', '-2+9']


Note:

4+3 comes from second and third elements from the main list.

3+4 comes from third and seventh elements from the main list.

"""


def pair_sum(input_List, target):
    out_list=[]
    for i in range(len(input_List)):
        for j in range(i,len(input_List)):
            if (input_List[i]+input_List[j]==target):
                out_list.append(str(input_List[i])+'+'+str(input_List[j]))
    return out_list


print(pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7))
