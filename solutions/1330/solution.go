package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)

	var a, b int
	fmt.Fscan(in, &a, &b)

	if a > b {
		fmt.Println(">")
	} else if a < b {
		fmt.Println("<")
	} else {
		fmt.Println("==")
	}
}
