use std::env;
use std::io::{self, prelude::*, BufReader};

use fileinput::FileInput;

fn main() -> io::Result<()>
{
    let args: Vec<String> = env::args().collect();
    let fileinput = FileInput::new(&args[1..]);
    let reader = BufReader::new(fileinput);

    for line in reader.lines() {
        let line_str = line?;
        let depth: u32 = line_str.parse().unwrap();
    }

    Ok(())
}
