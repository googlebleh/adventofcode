package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

// positive x goes right, positive y goes down
func solve(x_delta, y_delta int) int {
	f, err := os.Open("input")
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()

	num_trees := 0
	x_pos := 0

	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		line := scanner.Text()
		width := len(strings.TrimSpace(line))

		if line[x_pos % width] == '#' {
			num_trees++
		}

		// move horizontally
		x_pos += x_delta
		for i := 1; i < y_delta; i++ {
			// move vertically
			scanner.Scan()
		}
	}
	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	return num_trees
}

func main() {
	fmt.Println("Part 1:", solve(3, 1))

	part2 := solve(1, 1) * solve(3, 1) * solve(5, 1) * solve(7, 1) * solve(1, 2)
	fmt.Println("Part 2:", part2)
}
