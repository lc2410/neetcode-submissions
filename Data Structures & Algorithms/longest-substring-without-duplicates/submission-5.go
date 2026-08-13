func lengthOfLongestSubstring(s string) int {
	var left int = 0
	var res = 0
	var charSet = map[byte]bool{}
	for right:=0; right<len(s); right++{
		for charSet[s[right]] {
			delete(charSet, s[left])
			left++
		}
		charSet[s[right]] = true
		res = max(res, right-left+1)
	}
	return res
}
