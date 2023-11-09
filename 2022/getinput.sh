#!/usr/bin/env bash

set -x


curl \
	--cookie "session=53616c7465645f5fdd163b7e75596b7e371c5c7715037aff060ad8a1c378ad7ff90b78c22382255e95e36c4c56e2277daa8500dc37144a6ea394f668fe73dad8" \
	-LORJ \
	"https://adventofcode.com/2022/day/$1/input"
