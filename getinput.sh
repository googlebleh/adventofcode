#!/usr/bin/env bash

set -ex

git_rootdir="$(git rev-parse --show-toplevel)"
if [ ! -d "$git_rootdir" ]; then
	echo "error: run from AoC repo"
	exit 1
fi

print_usage ()
{
	echo "usage: $0 <day number> <year>"
}

day="${1:-$(TZ=America/New_York date +%-d)}"
year="${2:-$(date +%Y)}"

day_padded="$(printf "%02d" "$day")"
read -r aoc_session < "$git_rootdir/session_cookie.txt"
curl \
	-sLORJ \
	--create-dirs \
	--output-dir "$git_rootdir/$year/$day_padded" \
	--cookie "session=$aoc_session" \
	"https://adventofcode.com/$year/day/$day/input"
