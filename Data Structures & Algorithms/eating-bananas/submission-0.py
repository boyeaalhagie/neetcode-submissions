from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Helper to check if Koko can finish with speed k in at most h hours
        def can_finish(k: int) -> bool:
            # Use integer math for ceil(p/k): (p + k - 1) // k
            hours = 0
            for p in piles:
                hours += (p + k - 1) // k
                if hours > h:  # early exit if already too many hours
                    return False
            return hours <= h

        left, right = 1, max(piles)
        ans = right
        while left <= right:
            mid = (left + right) // 2  # candidate speed
            if can_finish(mid):
                ans = mid            # mid works; try smaller speed
                right = mid - 1
            else:
                left = mid + 1       # mid too slow; need faster speed
        return ans
