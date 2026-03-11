from typing import List

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def can_achieve(penalty: int) -> bool:
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