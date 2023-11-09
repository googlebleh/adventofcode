use std::fs::File;
use std::io::{self, prelude::*, BufReader};

fn main() -> io::Result<()>
{
    let file = File::open("foo.txt")?;
    let reader = BufReader::new(file);

    for line in reader.lines() {
        let depth: u32 = line?.parse().unwrap();
        println!("{}", depth);
    }

    Ok(())
}
