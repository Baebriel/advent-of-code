use std::collections::HashSet;

pub fn process_part1(input: &str) -> u32 {

    let mut sum = 0;

    for line in input.lines() {

        let mut left_chars: HashSet<char> = HashSet::new();
        let mut right_chars: HashSet<char> = HashSet::new();

        let left_slice = &line[..line.len()/2];
        let right_slice = &line[line.len()/2..];

        for char in left_slice.chars() {
            left_chars.insert(char);
        }

        for char in right_slice.chars() {
            right_chars.insert(char);
        }

        let common_char = left_chars.intersection(&right_chars).next().unwrap();

        if (*common_char as u32) < 91 {
            sum += *common_char as u32 - 38;
        } else {
            sum += *common_char as u32 - 96;
        }
    }
    sum
}

pub fn process_part2(input: &str) -> u32 {

    let mut sum = 0;

    let lines = input.lines();

    0
}

#[cfg(test)]
mod tests {
    use super::*;

    const INPUT: &str = "vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw";

    #[test]
    fn test_part1() {
        let result: u32 = process_part1(INPUT);
        assert_eq!(result, 157);
    }

    #[test]
    fn test_part2() {
        let result: u32 = process_part2(INPUT);
        assert_eq!(result, 70);
    }
}
