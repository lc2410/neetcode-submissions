func isAnagram(s string, t string) bool {
	if len(s) != len(t){
		return false
	}
	var counts [26]int

	for i := 0; i<len(s); i++{
		counts[s[i]-'a'] += 1
		counts[t[i]-'a'] -= 1
	}

	for _, count := range counts{
		if count != 0{
			return false
		}
	}

	return true

}
