#!/usr/bin/env bash

set -x


# get_day_number ()
# {
# 	bc -l <<< "((`date +%s` - `date -d 'dec 1' +%s`) / (24*3600)) + 1"
# 		| LC_ALL=C xargs printf "%.*f\n" "$p"
# }

curl \
	--cookie "session=53616c7465645f5f54ac5803c4aa115c0d15e37ebab4d2453350d5028b7271c91c1c774711ca49de01f83a9c140aebc4" \
	-LORJ \
	"https://adventofcode.com/2020/day/$1/input"
