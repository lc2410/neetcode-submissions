class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        ans = [None] * k
        for num in nums:
            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1
        hashMap = dict(sorted(hashMap.items(), key=lambda item: item[1], reverse=True))
        print(hashMap)
        keys_list = list(hashMap.keys())
        print(keys_list)
        for i in range(len(ans)):
            ans[i] = keys_list[i]
        return ans