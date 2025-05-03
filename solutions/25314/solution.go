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
	for i := 0; i < n/4; i++ {
		fmt.Print("long ")
	}
	fmt.Println("int")
}
