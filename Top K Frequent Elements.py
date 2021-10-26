from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # temp = Counter(nums).most_common(k)
        result = []
        for i in Counter(nums).most_common(k):
            result.append(i[0])
        return result
