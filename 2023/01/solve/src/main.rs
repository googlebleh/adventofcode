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

fn main() -> anyhow::Result<()>
{
    return part1();
}
