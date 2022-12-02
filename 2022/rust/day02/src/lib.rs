pub fn process_part1(input: &str) -> String {
    let result = input
        .lines()
        .map(|line| {
            match line {
                "A X" => 4, // rock + rock, draw = 3, rock = 1
                "A Y" => 8, // rock + paper, win = 6, paper = 2
                "A Z" => 3, // rock + scissors, loss = 0, scissors = 3
                "B X" => 1, // paper + rock, loss = 0, rock = 1
                "B Y" => 5, // paper + paper, draw = 3, paper = 2
                "B Z" => 9, // paper + scissors, win = 6, scissors = 3
                "C X" => 7, // scissors + rock, win = 6, rock = 1
                "C Y" => 2, // scissors + paper, loss = 0, paper = 2
                "C Z" => 6, // scissors + scissors, draw = 3, scissors = 3
                &_ => 0,
            }
        })
        .sum::<u32>();
    result.to_string()
}

pub fn process_part2(input: &str) -> String {
    let result = input
        .lines()
        .map(|line| {
            match line {
                "A X" => 3, // loss = 0, scissors = 3
                "A Y" => 4, // draw = 3, rock = 1
                "A Z" => 8, // win = 6, paper = 2
                "B X" => 1, // loss = 0, rock = 1
                "B Y" => 5, // draw = 3, paper = 2
                "B Z" => 9, // win = 6, scissors = 3
                "C X" => 2, // loss = 0, paper = 2
                "C Y" => 6, // draw = 3, scissors = 3
                "C Z" => 7, // win = 6, rock = 1
                &_ => 0,
            }
        })
        .sum::<u32>();
    result.to_string()
}

#[cfg(test)]
mod tests {
    use super::*;

    const INPUT: &str = "A Y
B X
C Z";

    #[test]
    fn test_part1() {
        let result = process_part1(INPUT);
        assert_eq!(result, "15");
    }

    #[test]
    fn test_part2() {
        let result = process_part2(INPUT);
        assert_eq!(result, "12");
    }

}
