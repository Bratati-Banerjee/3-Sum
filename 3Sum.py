class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:  # Base case
            return []
        if len(nums) == 3:
            if (nums[0] + nums[1] + nums[2]) == 0:
                return [nums]
            else:
                return []

        sol = {}  # The solution set must not contain duplicate triplets, so we take hash having triplet as key
        nums = sorted(nums)

        for i in range(len(nums) - 3):
            a = nums[i]
            start = i + 1
            end = len(nums) - 1

            while (start < end):
                b = nums[start]
                c = nums[end]
                if (a + b + c) == 0:
                    sol[a, b, c] = [a, b, c]
                    end = end - 1
                elif (a + b + c) > 0:
                    end = end - 1
                else:
                    start = start + 1

        return sol.values()
