from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []

if __name__ == "__main__":
    nums = [2,11,15, 7]
    target = 13
    print(Solution().twoSum(nums, target))
