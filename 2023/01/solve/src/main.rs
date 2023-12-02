#![allow(dead_code)]

use std::io::BufRead;

fn get_first_char(s: impl Iterator<Item = char>) -> anyhow::Result<u32>
{
    for c in s {
        if let Some(r) = c.to_digit(10) {
            return Ok(r);
        }
    }
    anyhow::bail!("no int found");
}

fn part1() -> anyhow::Result<()>
{
    let stdin = std::io::stdin();
    let mut cumulative_sum = 0;
    for line in stdin.lock().lines() {
        let line = line?;

        let first = get_first_char(line.chars())?;
        let last = get_first_char(line.chars().rev())?;
        cumulative_sum += (first * 10) + last;
    }
    println!("{cumulative_sum}");
    return Ok(());
}

fn parse_digit(s: &str, i: usize) -> Option<u32>
{
    if let Some(d) = s.chars().nth(i).unwrap().to_digit(10) {
        return Some(d);
    }

    let lut = [
        ("zero", 0),
        ("one", 1),
        ("two", 2),
        ("three", 3),
        ("four", 4),
        ("five", 5),
        ("six", 6),
        ("seven", 7),
        ("eight", 8),
        ("nine", 9),
    ];
    for (name, val) in lut {
        if s[i..].starts_with(name) {
            return Some(val);
        }
    }
    return None;
}

fn find_digit(s: &str, it: impl Iterator<Item = usize>) -> anyhow::Result<u32>
{
    for i in it {
        if let Some(d) = parse_digit(&s, i) {
            return Ok(d);
        }
    }
    anyhow::bail!("no digit!");
}

fn part2() -> anyhow::Result<()>
{
    let stdin = std::io::stdin();
    let mut cumulative_sum = 0;
    for line in stdin.lock().lines() {
        let line = line?;

        let first = find_digit(&line, 0..line.len())?;
        let last = find_digit(&line, (0..line.len()).rev())?;
        cumulative_sum += (first * 10) + last;
    }
    println!("{cumulative_sum}");
    return Ok(());
}

fn main() -> anyhow::Result<()>
{
    return part2();
}
