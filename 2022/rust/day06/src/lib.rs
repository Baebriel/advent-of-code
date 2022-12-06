use std::collections::HashSet;

pub fn process_both_parts(input: &str, size: usize) -> u32 {
    let iter = input.chars().collect::<Vec<char>>();
    let iter = iter.windows(size);

    let mut cnt = size;
    for slice in iter {
        let mut set: HashSet<&char> = HashSet::new();
        for letter in slice {set.insert(letter);}
        if set.len() == size {
            break
        }
        cnt += 1;
    }
    cnt as u32
}

#[cfg(test)]
mod tests {
    use super::*;

    const INPUT: [&str; 5] = [
        "mjqjpqmgbljsphdztnvjfqwrcgsmlb",
        "bvwbjplbgvbhsrlpgdmjqwftvncz",
        "nppdvjthqldpwncqszvftbrmjlhg",
        "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
        "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",
    ];

    #[test]
    fn test_part1() {
        assert_eq!(process_both_parts(INPUT[0], 4), 7);
        assert_eq!(process_both_parts(INPUT[1], 4), 5);
        assert_eq!(process_both_parts(INPUT[2], 4), 6);
        assert_eq!(process_both_parts(INPUT[3], 4), 10);
        assert_eq!(process_both_parts(INPUT[4], 4), 11);
    }

    #[test]
    fn test_part2() {
        assert_eq!(process_both_parts(INPUT[0], 14), 19);
        assert_eq!(process_both_parts(INPUT[1], 14), 23);
        assert_eq!(process_both_parts(INPUT[2], 14), 23);
        assert_eq!(process_both_parts(INPUT[3], 14), 29);
        assert_eq!(process_both_parts(INPUT[4], 14), 26);
    }
}
