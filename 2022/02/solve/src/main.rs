use std::io::BufRead;


fn get_score_part1(their_move: &str, your_move: &str) -> i32
{
    return if their_move == "A" {
        match your_move {
            "X" => 3 + 1,
            "Y" => 6 + 2,
            "Z" => 0 + 3,
            _ => panic!("oo"),
        }
    } else if their_move == "B" {
        match your_move {
            "X" => 0 + 1,
            "Y" => 3 + 2,
            "Z" => 6 + 3,
            _ => panic!("oo"),
        }
    } else if their_move == "C" {
        match your_move {
            "X" => 6 + 1,
            "Y" => 0 + 2,
            "Z" => 3 + 3,
            _ => panic!("oo"),
        }
    } else {
        panic!("ee");
    }
}


fn part1() -> anyhow::Result<()>
{
    // A for Rock, B for Paper, and C for Scissors
    // X for Rock, Y for Paper, and Z for Scissors

    let mut total_score = 0;

    let stdin = std::io::stdin();
    for line in stdin.lock().lines() {
        let line = line?;
        
        let mut t = line.split(" ");
        let their_move = t.next().unwrap();
        let your_move = t.next().unwrap();

        let score = get_score_part1(their_move, your_move);

        println!("{their_move} {your_move} {score}");
        total_score += score;
    }

    println!("{total_score}");
    return Ok(());
}


fn get_score_part2(their_move: &str, your_move: &str) -> i32
{
    return if their_move == "A" {
        match your_move {
            "X" => 0 + 3,
            "Y" => 3 + 1,
            "Z" => 6 + 2,
            _ => panic!("oo"),
        }
    } else if their_move == "B" {
        match your_move {
            "X" => 0 + 1,
            "Y" => 3 + 2,
            "Z" => 6 + 3,
            _ => panic!("oo"),
        }
    } else if their_move == "C" {
        match your_move {
            "X" => 0 + 2,
            "Y" => 3 + 3,
            "Z" => 6 + 1,
            _ => panic!("oo"),
        }
    } else {
        panic!("ee");
    }
}


fn part2() -> anyhow::Result<()>
{
    // A for Rock, B for Paper, and C for Scissors
    // X means lose, Y means end the round in a draw, and Z means win

    let mut total_score = 0;

    let stdin = std::io::stdin();
    for line in stdin.lock().lines() {
        let line = line?;
        
        let mut t = line.split(" ");
        let their_move = t.next().unwrap();
        let your_move = t.next().unwrap();

        let score = get_score_part2(their_move, your_move);

        println!("{} {} {}", their_move, your_move, score);
        total_score += score;
    }

    println!("{total_score}");
    return Ok(());
}


fn main() -> anyhow::Result<()>
{
    return part2();
}
