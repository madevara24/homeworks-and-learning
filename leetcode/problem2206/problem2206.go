package problem2206

func DivideArray(nums []int) bool {

	pairs := make(map[int]int)

	for i := 0; i < len(nums); i++ {
		pairs[nums[i]]++
	}

	for _, v := range pairs {
		if v%2 != 0 {
			return false
		}
	}

	return true
}
