from typing import List
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        max_index = arr.index(max(arr))
        if max_index == len(arr)-1 or max_index ==0:
            return False
            
        ascending = all(arr[j]< arr[j+1] for j in range(max_index-1))
        descending = all(arr[j] > arr[j+1] for j in range(max_index, len(arr)-1))
        if (ascending and descending) :
            return True
        else:
            return  False