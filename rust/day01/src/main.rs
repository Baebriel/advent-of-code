use std::{fs, vec};

fn main() {

    let filename = "input.txt";

    let input = parse_input(&filename);

    let most_calories = find_most_calories(&input);

    println!("Using: {filename}");
    println!("Part 1: {}", &most_calories);

    let top_three = find_top_three(&input);

    println!("Part 2: {}", top_three.iter().sum::<u32>())
}

fn parse_input(filename: &str) -> Vec<u32> {

    let input = fs::read_to_string(filename).unwrap();
    
    input
        .lines()
        .map(|x| -> u32 {
            if x.is_empty() {
                0
            } else {
                x.parse().unwrap()
            }
        })
        .collect::<Vec<u32>>()
}

fn find_most_calories(input: &Vec<u32>) -> u32 {

    let mut largest = 0;
    let mut sum = 0;

    for num in input {
        if *num == 0 {
            if sum > largest {
                largest = sum;
            }
            sum = 0;
        } else {
            sum += num;
        }
    }

    largest
}

fn find_top_three(input: &Vec<u32>) -> Vec<u32> {

    let mut sums: Vec<u32> = vec![];
    let mut sum = 0;

    for num in input {
        if *num == 0 {
            sums.push(sum);
            sum = 0;
        } else {
            sum += num;
        }
    }

    sums.sort_by(|a,b| b.partial_cmp(a).unwrap());

    sums[..3].to_vec()
}