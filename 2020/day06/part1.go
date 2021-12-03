package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func main() {
	f, err := os.Open("input")
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()

	part1 := 0

	scanner := bufio.NewScanner(f)
	done := false
	for !done { // loop over file
		group_yess := make(map[rune]bool)

		for { // loop over group
			if !scanner.Scan() {
				done = true
				break
			}

			line := scanner.Text()
			if line == "" {
				break
			}

			for _, c := range line {
				group_yess[c] = true
			}
		}

		part1 += len(group_yess)
	}
	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	fmt.Println("Part 1:", part1)
}
