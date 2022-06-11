// Created by: Paydhi
package main

import "fmt"

func main() {
	x := 0
	i := 1
	for i < 1000 {
		i = i + 1
		if (i%3 == 0 || i%5 == 0) {
			x = x + i
		}
	}
	fmt.Println(x)
}

