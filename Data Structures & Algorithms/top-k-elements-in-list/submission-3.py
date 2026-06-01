class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = list()
        hashmap = {}
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 0
            hashmap[num] += 1
        sortedHashMap = dict(sorted(hashmap.items(), key=lambda item: item[1]))
        for i in range(k):
            topKVal = sortedHashMap.popitem()
            ans.append(topKVal[0])
        return ans
