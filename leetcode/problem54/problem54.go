package problem54

import "fmt"

func SpiralOrder(matrix [][]int) []int {
	res := []int{}
	nEnd := len(matrix[0])
	mEnd := len(matrix)

	nStart := 0
	mStart := 0

	for i := mStart; i < mEnd; i++ {
		for j := nStart; j < nEnd; j++ {
			switch i {
			case mStart:
				res = append(res, matrix[i][j])
			case mEnd:
				res = append(res, matrix[i][nEnd-(j+1)])
			}

			// if i%2 == 0 {
			// 	res = append(res, matrix[i][j])
			// } else {
			// 	res = append(res, matrix[i][nEnd-(j+1)])
			// }

		}
	}

	fmt.Println(res)

	return res
}
