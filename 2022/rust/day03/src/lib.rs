use std::{collections::HashSet, hash::Hash};
use itertools::Itertools;

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

    for mut group in &input.lines().chunks(3) {

        let mut set1: HashSet<char> = HashSet::new();
        let mut set2: HashSet<char> = HashSet::new();
        let mut set3: HashSet<char> = HashSet::new();

        let line = group.next().unwrap();

        for char in line.chars() {
            set1.insert(char);
        }

        let line = group.next().unwrap();

        for char in line.chars() {
            set2.insert(char);
        }

        let line = group.next().unwrap();

        for char in line.chars() {
            set3.insert(char);
        }

        let set4 = set3.iter().map(|char| char).collect::<HashSet<&char>>();

        let common_char1 = set1.intersection(&set2).collect::<HashSet<&char>>();
        let mut common_char2 = common_char1.intersection(&set4);

        let common_char = common_char2.next().unwrap();

        if (**common_char as u32) < 91 {
            sum += **common_char as u32 - 38;
        } else {
            sum += **common_char as u32 - 96;
        }
    }
    sum
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
