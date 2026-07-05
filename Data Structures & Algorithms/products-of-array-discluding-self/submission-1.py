class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sol = [0] * len(nums)
        prefix = 1
        for i, num in enumerate(nums):
            sol[i] = prefix
            prefix*=num
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            sol[i] = sol[i] * postfix
            postfix *= nums[i]
        return sol