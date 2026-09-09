class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resStrs = defaultdict(list)
        for s in strs:
            sortedStrs = ''.join(sorted(s))
            resStrs[sortedStrs].append(s)
        return list(resStrs.values())

        
