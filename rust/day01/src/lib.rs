pub fn process_part1(input: &str) -> String {
    let result = input
        .split("\n\n")
        .map(|elf| {
            elf
                .split("\n")
                .map(|item| item.parse::<u32>().unwrap())
                .sum::<u32>()
        })
        .max()
        .unwrap();
    result.to_string()
}

pub fn process_part2(input: &str) -> String {
    let mut result = input
        .split("\n\n")
        .map(|elf| {
            elf
                .split("\n")
                .map(|item| item.parse::<u32>().unwrap())
                .sum::<u32>()
        })
        .collect::<Vec<u32>>();

    result.sort_by(|a,b| b.cmp(a));
    result.iter().take(3).sum::<u32>().to_string()
}

#[cfg(test)]
mod tests {
    use super::*;

    const INPUT: &str = "1000
2000
3000

4000

5000
6000

7000
8000
9000

10000";

    #[test]
    fn test_part1() {
        let result = process_part1(INPUT);
        assert_eq!(result, "24000");
    }

    #[test]
    fn test_part2() {
        let result = process_part2(INPUT);
        assert_eq!(result, "45000");
    }
}
