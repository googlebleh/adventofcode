use std::io::BufRead;

fn part1() -> anyhow::Result<()>
{
    let mut max_load = -1;
    let mut curr_load = 0;

    let stdin = std::io::stdin();
    for line in stdin.lock().lines() {
        let line = line?;

        if line == "" {
            if curr_load > max_load {
                max_load = curr_load;
            }
            curr_load = 0;

        } else {
            let calories = line.parse::<i32>()?;
            curr_load += calories;
        }
    }

    if curr_load > max_load {
        println!("{}", curr_load);
    } else {
        println!("{}", max_load);
    }

    return Ok(());
}

fn part2() -> anyhow::Result<()>
{
    let mut all_loads = std::vec::Vec::new();
    let mut curr_load = 0;

    let stdin = std::io::stdin();
    for line in stdin.lock().lines() {
        let line = line?;

        if line == "" {
            all_loads.push(curr_load);
            curr_load = 0;

        } else {
            let calories = line.parse::<i32>()?;
            curr_load += calories;
        }
    }
    all_loads.push(curr_load);

    all_loads.sort();
    all_loads.reverse();
    let top3 = &all_loads[..3];
    println!("{:?}", top3);
    println!("{:?}", top3.iter().sum::<i32>());

    return Ok(());
}

fn main() -> anyhow::Result<()>
{
    // return part1();
    return part2();
}
