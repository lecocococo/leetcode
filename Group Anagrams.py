from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)
        for i in strs:
            hm["".join(sorted(i))].append(i)
        
        result = []
        for i in hm:
            result.append(hm[i])
        
        return result
