class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        cur_sol = 0
        sol = 0
        last_num = 0
        for num in nums:
            if num <= last_num:
                cur_sol = 0
                last_num = 0

            cur_sol += num
            sol = max(sol, cur_sol)
            last_num = num




        return sol