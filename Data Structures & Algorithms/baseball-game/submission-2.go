func calPoints(operations []string) int {
	var stack []int
	var total int
	for _, operation := range operations{
		if operation == "+"{
			n := len(stack)
			num1 := stack[n-1]
			num2 := stack[n-2]
			stack = append(stack, num1+num2)
			total += (num1+num2)
		}else if operation == "C"{
			total -= stack[len(stack)-1]
            stack = stack[:len(stack)-1]
		}else if operation == "D"{
			num := stack[len(stack)-1]
			stack = append(stack, 2*num)
			total += 2*num
		}else{
			num, _ := strconv.Atoi(operation)
            stack = append(stack, num)
            total += num
		}
	}
	return total
}

func Pop(stack []int) int{
	topIndex := len(stack) - 1
	topElement := stack[topIndex]
	stack = stack[:topIndex]
	return topElement
}