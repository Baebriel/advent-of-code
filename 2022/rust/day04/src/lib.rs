pub fn process_part1(input: &str) -> u32 {
    input
        .lines()
        .map(|line| {
            line.split(',')
                .map(|range| {
                    range
                        .split('-')
                        .map(|bound| bound.parse::<u32>().unwrap())
                        .collect::<Vec<u32>>()
                })
                .flatten()
                .collect::<Vec<u32>>()
        })
        .filter(|bounds| {
            ((bounds[0] <= bounds[2]) && (bounds[1] >= bounds[3]))
                || ((bounds[0] >= bounds[2]) && (bounds[1] <= bounds[3]))
        })
        .count() as u32
}

pub fn process_part2(input: &str) -> u32 {
    input
        .lines()
        .map(|line| {
            line.split(',')
                .map(|range| {
                    range
                        .split('-')
                        .map(|bound| bound.parse::<u32>().unwrap())
                        .collect::<Vec<u32>>()
                })
                .flatten()
                .collect::<Vec<u32>>()
        })
        .filter(|bounds| (bounds[0] <= bounds[3]) && (bounds[2] <= bounds[1]))
        .count() as u32
}

#[cfg(test)]
mod tests {
    use super::*;

    const INPUT: &str = "2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8";

    #[test]
    fn test_part1() {
        let result: u32 = process_part1(INPUT);
        assert_eq!(result, 2);
    }

    #[test]
    fn test_part2() {
        let result: u32 = process_part2(INPUT);
        assert_eq!(result, 4);
    }
}
