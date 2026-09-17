class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sortNums = []
        for i, num in enumerate(nums):
            sortNums.append([num, i])

        sortNums.sort()
        i, j = 0, len(nums) -1
        while i < j:
            current = sortNums[i][0] + sortNums[j][0]
            if current == target:
                return [min(sortNums[i][1], sortNums[j][1]), 
                        max(sortNums[i][1], sortNums[j][1])]
            elif current < target:
                i+= 1
            else:
                j-= 1  
        return []