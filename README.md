# 25MCI10054_Suyash_25MAM_KAR_FRO_1_LABMST-CP
CP Lab MST

## 845. Longest Mountain in Array

```
class Solution(object):
    def longestMountain(self, arr):
        n = len(arr)
        if n < 3:
            return 0
        
        max_len = 0
        up = 0
        down = 0
        
        for i in range(1, n):
            
            if (down > 0 and arr[i] > arr[i-1]) or arr[i] == arr[i-1]:
                up = 0
                down = 0
            
            if arr[i] > arr[i-1]:
                up += 1
            elif arr[i] < arr[i-1]:
                if up > 0:
                    down += 1
                    max_len = max(max_len, up + down + 1)
        
        return max_len
```
<img alt="image" src="Output 845.jpg" />

## 1760. Minimum Limit of Balls in a Bag

```
class Solution(object):
    def minimumSize(self, nums, maxOperations):
        """
        :type nums: List[int]
        :type maxOperations: int
        :rtype: int
        """
        def can_achieve(penalty):
            ops = 0
            for num in nums:
                if num > penalty:
                    ops += (num + penalty - 1) // penalty - 1
            return ops <= maxOperations
        
        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2
            if can_achieve(mid):
                right = mid
            else:
                left = mid + 1
        return left
        
```
<img alt="image" src="Output 1760.jpg" />