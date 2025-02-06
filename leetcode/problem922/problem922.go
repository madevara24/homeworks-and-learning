package problem922

// https://leetcode.com/problems/sort-array-by-parity-ii/description/

func SortArrayByParityII(nums []int) []int {

	for i := 0; i < len(nums); i++ {
		if i%2 != nums[i]%2 {
			for j := i + 1; j < len(nums); j++ {
				if j%2 != nums[j]%2 && j%2 != i%2 {
					nums[i], nums[j] = nums[j], nums[i]
					break
				}
			}
		}
	}

	return nums
}
