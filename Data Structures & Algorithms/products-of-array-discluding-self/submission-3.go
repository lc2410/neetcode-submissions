func productExceptSelf(nums []int) []int {
	var results = make([]int, len(nums))
	for i := range results{
		results[i] = 1
	}
	var prefix = 1
	for i:=0; i<len(nums); i++{
		results[i] = prefix
		prefix *= nums[i]
	}
	var suffix = 1
	for i:=len(nums)-1; i>=0; i--{
		results[i] *= suffix
		suffix *= nums[i]
	}
	return results
}
