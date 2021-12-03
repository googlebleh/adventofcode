package main

import (
	"io"
	"fmt"
	"os"
	"bufio"
	"log"
	"strings"
)

func password_valid_part1(pw, c string, min, max int) bool {
	count := strings.Count(pw, c)
	return (min <= count && count <= max)
}

func password_valid_part2(pw, c string, pos1, pos2 int) bool {
	// the following is a boolean xor
	return (pw[pos1-1] == c[0]) != (pw[pos2-1] == c[0])
}

func main() {
	f, err := os.Open("input")
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()

	num_valid_pws_part1 := 0
	num_valid_pws_part2 := 0
	reader := bufio.NewReader(f)
	var a, b int
	var c, pw string
	for {
		_, err := fmt.Fscanf(reader, "%d-%d %1s: %s\n", &a, &b, &c, &pw)
		if err == io.EOF {
			break
		} else if err != nil {
			log.Fatal(err)
		} else {
			if password_valid_part1(pw, c, a, b) {
				num_valid_pws_part1++
			}
			if password_valid_part2(pw, c, a, b) {
				num_valid_pws_part2++
			}
		}
	}

	fmt.Println("Part 1: found", num_valid_pws_part1, "valid passwords")
	fmt.Println("Part 2: found", num_valid_pws_part2, "valid passwords")
}
