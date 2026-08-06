func twoSum(nums []int, target int) []int {
    hashmap := make(map[int]int) // key: num array value, value: num array index

	for index, num := range nums{
		difference := target - num
		_, ok := hashmap[difference]
		if ok{
			return []int{hashmap[difference], index}
		}
		hashmap[num] = index
	}

	return []int{}
}
