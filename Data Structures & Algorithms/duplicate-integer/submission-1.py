class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniques = list(set(nums))
        if len(uniques) != len(nums):
            return True
        return False