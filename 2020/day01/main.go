package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func main() {
	f, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()

	nums := make([]int, 1)
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		line := scanner.Text()

		n, err := strconv.Atoi(line)
		if err != nil {
			log.Fatal("Couldn't convert " + line)
		}

		nums = append(nums, n)
	}
	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
	nums = nums[1:]

	target := 2020
	func () {
		fmt.Println("Part 1")
		for i, x := range nums {
			for _, y := range nums[i+1:] {
				if x + y == target {
					fmt.Println(x * y)
					return
				}
			}
		}
	}()

	fmt.Println()

	func () {
		fmt.Println("Part 2")
		for i, x := range nums {
			for j, y := range nums[i+1:] {
				for _, z := range nums[j+1:] {
					if x + y + z == target {
						fmt.Println(x * y * z)
						return
					}
				}
			}
		}
	}()
}
