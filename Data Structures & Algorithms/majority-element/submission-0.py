class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        major = maxCount = 0

        for num in nums:
            counter[num] += 1
            if maxCount < counter[num]:
                major = num
                maxCount = counter[num]
        return major