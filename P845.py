from typing import List

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 3:
            return 0
        
        max_len = 0
        up = 0
        down = 0
        
        for i in range(1, n):
            if arr[i] > arr[i-1]:
                up += 1
                down = 0
            elif arr[i] < arr[i-1]:
                down += 1
                if up > 0:
                    max_len = max(max_len, up + down + 1)
            else:
                up = 0
                down = 0
        
        return max_len