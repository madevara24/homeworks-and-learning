package problem1266

import "math"

func MinTimeToVisitAllPoints(points [][]int) int {
	steps := 0

	prev := points[0]

	for i := 1; i < len(points); i++ {
		xDiff := math.Abs(float64(points[i][0]) - float64(prev[0]))
		yDiff := math.Abs(float64(points[i][1]) - float64(prev[1]))

		steps += int(math.Max(xDiff, yDiff))

		prev = points[i]
	}

	return steps
}
