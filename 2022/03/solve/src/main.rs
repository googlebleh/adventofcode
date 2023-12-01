use std::io::BufRead;


fn part1() -> anyhow::Result<()>
{
    let mut total_priority = 0;
    let a_val = 'a' as u32 - 1;
    let A_val = 'A' as u32 - 1;

    let stdin = std::io::stdin();
    for line in stdin.lock().lines() {
        let line = line?;

        let half_i = line.len() / 2;

        let first = &line[..half_i];
        let second = &line[half_i..];

        // let mut first_com = std::collections::HashSet::from(first.as_bytes().to_vec());
        // let mut second_com = std::collections::HashSet::from(second.as_bytes().to_vec());
        //
        // let intersection = first_com.intersection(&second_com);
        // println!("{:#?}", intersection);

        for e in first.chars() {
            if second.contains(e) {
                let value = e as u32;
                println!("{e} {value}");
                total_priority += match e.is_uppercase() {
                    true => value - A_val + 26,
                    false => value - a_val,
                };
                break;
            }
        }
    }

    println!("{total_priority}");

    return Ok(());
}


fn main() -> anyhow::Result<()>
{
    return part1();
}
