class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sol = [0 for i in range(len(nums))]
        cur = 1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i ==j: continue
                cur *= nums[j]
            sol[i] = cur
            cur = 1
        return sol