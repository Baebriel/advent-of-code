use regex::Regex;

pub fn process_part1(input: &str) -> String {
    // split input on \n\n to get stacks and instructions
    let mut input = input.split("\n\n");

    let stacks = input.next().unwrap();
    let mut stacks: Vec<Vec<char>> = parse_initial_state(stacks);

    let instructions = input.next().unwrap();
    for line in instructions.lines() {
        process_instruction1(&mut stacks, line);
    }

    stacks
        .iter()
        .map(|stack| stack.iter().rev().next().unwrap())
        .collect::<String>()
}

fn parse_initial_state(text_input: &str) -> Vec<Vec<char>> {
    // count characters in line to get number of stacks
    let length = text_input.lines().next().unwrap().len();
    let num_stacks = (length + 1) / 4;

    // create empty stacks and parse text input into them
    let mut stacks: Vec<Vec<char>> = vec![Vec::new(); num_stacks];
    let lines = text_input.lines().take_while(|line| line.contains('['));
    for line in lines {
        let result = parse_stack_line(&line, num_stacks as u32);
        add_to_stack(&mut stacks, &result);
    }
    stacks
}

fn parse_stack_line(line: &str, n: u32) -> Vec<Option<char>> {
    let mut items: Vec<Option<char>> = Vec::new();

    let mut chars = line.chars().peekable();

    for _ in 1..=n {
        if chars.next().unwrap() == '[' {
            items.push(Some(chars.next().unwrap()));
            chars.next();
            chars.next();
        } else {
            items.push(None);
            chars.next();
            chars.next();
            chars.next();
        }
    }
    items
}

fn add_to_stack(stacks: &mut Vec<Vec<char>>, line: &Vec<Option<char>>) -> () {
    for (i, item) in line.iter().enumerate() {
        if let Some(letter) = item {
            stacks[i].insert(0, *letter);
        }
    }
}

fn process_instruction1(stacks: &mut Vec<Vec<char>>, line: &str) -> () {
    let re = Regex::new(r"move\s(\d+)\sfrom\s(\d)\sto\s(\d)").unwrap();
    let caps = re.captures(line).unwrap();

    let num_moves = caps.get(1).unwrap().as_str().parse::<usize>().unwrap();
    let from = caps.get(2).unwrap().as_str().parse::<usize>().unwrap();
    let to = caps.get(3).unwrap().as_str().parse::<usize>().unwrap();

    for _ in 1..=num_moves {
        let item = stacks[from - 1].pop().unwrap();
        stacks[to - 1].push(item);
    }
}

pub fn process_part2(input: &str) -> String {
    // split input on \n\n to get stacks and instructions
    let mut input = input.split("\n\n");

    let stacks = input.next().unwrap();
    let mut stacks: Vec<Vec<char>> = parse_initial_state(stacks);

    let instructions = input.next().unwrap();
    for line in instructions.lines() {
        process_instruction2(&mut stacks, line);
    }

    stacks
        .iter()
        .map(|stack| stack.iter().rev().next().unwrap())
        .collect::<String>()
}

fn process_instruction2(stacks: &mut Vec<Vec<char>>, line: &str) -> () {
    let re = Regex::new(r"move\s(\d+)\sfrom\s(\d)\sto\s(\d)").unwrap();
    let caps = re.captures(line).unwrap();

    let num_moves = caps.get(1).unwrap().as_str().parse::<usize>().unwrap();
    let from = caps.get(2).unwrap().as_str().parse::<usize>().unwrap();
    let to = caps.get(3).unwrap().as_str().parse::<usize>().unwrap();

    let length = stacks[from - 1].iter().len();
    let moved: Vec<char> = stacks[from - 1].drain((length - num_moves)..).collect();
    stacks[to - 1].extend(moved);
}

#[cfg(test)]
mod tests {
    use super::*;

    const INPUT: &str = "    [D]    
[N] [C]    
[Z] [M] [P]
    1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2";

    #[test]
    fn test_part1() {
        let result: String = process_part1(INPUT);
        assert_eq!(result, "CMZ");
    }

    #[test]
    fn test_part2() {
        let result: String = process_part2(INPUT);
        assert_eq!(result, "MCD");
    }
}
