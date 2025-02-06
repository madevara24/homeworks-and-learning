package problem2032

// https://leetcode.com/problems/two-out-of-three/description/

func TwoOutOfThree(nums1 []int, nums2 []int, nums3 []int) []int {
	var res []int

	set := make(map[int]int)

	for i := 0; i < len(nums1); i++ {
		if _, ok := set[nums1[i]]; !ok {
			set[nums1[i]] = 0
		}
	}

	for i := 0; i < len(nums2); i++ {
		if _, ok := set[nums2[i]]; !ok {
			set[nums2[i]] = 0
		}
	}

	for i := 0; i < len(nums3); i++ {
		if _, ok := set[nums3[i]]; !ok {
			set[nums3[i]] = 0
		}
	}

	for k, _ := range set {
		for i := 0; i < len(nums1); i++ {
			if nums1[i] == k {
				set[k]++
				break
			}
		}

		for j := 0; j < len(nums2); j++ {
			if nums2[j] == k {
				set[k]++
				break
			}
		}

		for l := 0; l < len(nums3); l++ {
			if nums3[l] == k {
				set[k]++
				break
			}
		}

		if set[k] >= 2 {
			res = append(res, k)
		}
	}

	return res

}

// nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3]
