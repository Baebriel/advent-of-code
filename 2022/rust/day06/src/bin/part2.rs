use day06::process_both_parts;
use std::fs;

fn main() {
    let file = fs::read_to_string("./input.txt").unwrap();
    println!("{}", process_both_parts(&file, 14));
}