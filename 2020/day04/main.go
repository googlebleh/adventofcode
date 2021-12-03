package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"strings"
	"strconv"
)

func part1_passport_valid(p map[string]string) bool {
	rv := true
	for _, value := range p {
		if value == "" {
			rv = false
		}
	}
	return rv
}

func part2_passport_valid(p map[string]string) bool {
	// byr (Birth Year) - four digits; at least 1920 and at most 2002.
	byr, err := strconv.Atoi(p["byr"])
	if !(err == nil && (1920 <= byr && byr <= 2002)) {
		return false
	}

	// iyr (Issue Year) - four digits; at least 2010 and at most 2020.
	iyr, err := strconv.Atoi(p["iyr"])
	if !(err == nil && (2010 <= iyr && iyr <= 2020)) {
		return false
	}

	// eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
	eyr, err := strconv.Atoi(p["eyr"])
	if !(err == nil && (2020 <= eyr && eyr <= 2030)) {
		return false
	}

	// hgt (Height) - a number followed by either cm or in:
	// If cm, the number must be at least 150 and at most 193.
	// If in, the number must be at least 59 and at most 76.
	hgt_str := p["hgt"]
	if len(hgt_str) < 3 {
		return false
	}
	hgt, err := strconv.Atoi(hgt_str[:len(hgt_str)-2])
	if err != nil {
		return false
	}
	if !((strings.HasSuffix(p["hgt"], "cm") && (150 <= hgt && hgt <= 193)) || (strings.HasSuffix(p["hgt"], "in") && (59 <= hgt && hgt <= 76))) {
		return false
	}

	// hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
	hcl_regex := regexp.MustCompile(`#[0-9a-f]{6}`)
	if !hcl_regex.MatchString(p["hcl"]) {
		return false
	}

	// ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
	allowed_ecl := map[string]interface{}{
		"amb": nil,
		"blu": nil,
		"brn": nil,
		"gry": nil,
		"grn": nil,
		"hzl": nil,
		"oth": nil,
	}
	_, ok := allowed_ecl[p["ecl"]]
	if !ok {
		return false
	}

	// pid (Passport ID) - a nine-digit number, including leading zeroes.
	pid_regex := regexp.MustCompile(`^\d{9}$`)
	if !pid_regex.MatchString(p["pid"]) {
		return false
	}

	// cid (Country ID) - ignored, missing or not.

	return true
}

func main() {
	f, err := os.Open("input")
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()

	part1_num_valid := 0
	part2_num_valid := 0

	scanner := bufio.NewScanner(f)
	func () {
		done := false
		for !done { // loop over file
			p := map[string]string{
				"byr": "",
				"iyr": "",
				"eyr": "",
				"hgt": "",
				"hcl": "",
				"ecl": "",
				"pid": "",
				// "cid": "",
			}

			for { // loop over passport
				if !scanner.Scan() {
					done = true
					break
				}
				line := scanner.Text()

				if line == "" {
					// done with this passport
					break
				}

				for _, field := range strings.Split(line, " ") {
					k_v := strings.Split(field, ":")
					key, value := k_v[0], k_v[1]
					p[key] = value
				}
			}

			if part1_passport_valid(p) {
				part1_num_valid++
			}
			if part2_passport_valid(p) {
				part2_num_valid++
			}
		}
	}()
	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	fmt.Println("Part 1:", part1_num_valid)
	fmt.Println("Part 2:", part2_num_valid)
}
