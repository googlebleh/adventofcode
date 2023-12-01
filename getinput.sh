#!/usr/bin/env bash

git_rootdir="$(git rev-parse --show-toplevel)"
if [ ! -d "$git_rootdir" ]; then
	echo "error: run from AoC repo"
	exit 1
fi

print_usage ()
{
	echo "usage: $0 <day number> <year>"
}

if [ $# -lt 1 ]; then
	echo $#
	print_usage
	exit 2
fi
day="$1"
year="${2:-2023}"

# get_day_number ()
# {
# 	bc -l <<< "((`date +%s` - `date -d 'dec 1' +%s`) / (24*3600)) + 1"
# 		| LC_ALL=C xargs printf "%.*f\n" "$p"
# }

read -r aoc_session < "$git_rootdir/session_cookie.txt"
curl -LORJ --cookie "session=$aoc_session" "https://adventofcode.com/$year/day/$1/input"
