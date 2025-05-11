from collections import deque

class Solution(object):
    def shortestSubarray(self, nums, k):
        n = len(nums)
        prefix = [0] * (n + 1)
        
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + nums[i - 1]
        
        dq = deque()
        min_len = n + 1
        
        for i in range(n + 1):
            while dq and prefix[i] - prefix[dq[0]] >= k:
                min_len = min(min_len, i - dq.popleft())
            
            while dq and prefix[i] <= prefix[dq[-1]]:
                dq.pop()
            
            dq.append(i)
        
        return min_len if min_len <= n else -1
