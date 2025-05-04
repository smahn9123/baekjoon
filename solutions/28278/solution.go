package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)

	var n int
	fmt.Fscan(in, &n)

	stack := make([]int, 0, n)
	output := make([]int, 0, 0)

	for i := 0; i < n; i++ {
		var cmd int
		fmt.Fscan(in, &cmd)

		switch cmd {
		case 1:
			var x int
			fmt.Fscan(in, &x)
			stack = append(stack, x)
		case 2:
			if len(stack) > 0 {
				top := stack[len(stack)-1]
				stack = stack[:len(stack)-1]
				output = append(output, top)
			} else {
				output = append(output, -1)
			}
		case 3:
			output = append(output, len(stack))
		case 4:
			if len(stack) == 0 {
				output = append(output, 1)
			} else {
				output = append(output, 0)
			}
		case 5:
			if len(stack) > 0 {
				output = append(output, stack[len(stack)-1])
			} else {
				output = append(output, -1)
			}
		}
	}

	for _, val := range output {
		fmt.Println(val)
	}
}
