use std::io::BufRead;

fn main() -> anyhow::Result<()>
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
