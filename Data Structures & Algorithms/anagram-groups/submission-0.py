class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        ans = []
        for i, s in enumerate(strs):
            sortedString = "".join(sorted(s))
            if sortedString in hashMap:
                hashMap[sortedString].append(i)
            else:
                hashMap[sortedString] = [i]
        print(hashMap)
        for arr in hashMap.values():
            temp = []
            for index in arr:
                temp.append(strs[index])
            ans.append(temp)
        return ans
