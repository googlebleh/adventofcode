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

	part2 := 0

	scanner := bufio.NewScanner(f)
	done := false
	// loop over file
	for !done {
		group_yess := make(map[rune]bool)
		first := true

		// loop over group
		for {
			if !scanner.Scan() {
				done = true
				break
			}

			line := scanner.Text()
			if line == "" {
				// done with group
				break
			}

			person_yess := make(map[rune]bool)
			for _, question := range line {
				person_yess[question] = true
			}

			if first {
				// first person. record answers
				group_yess = person_yess
				first = false
			} else {
				// set intersection
				for question, _ := range group_yess {
					if !person_yess[question] {
						delete(group_yess, question)
					}
				}
			}
		}

		part2 += len(group_yess)
	}
	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	fmt.Println("Part 2:", part2)
}
