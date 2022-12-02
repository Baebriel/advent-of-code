pub fn process_part1(input: &str) -> String {
    "".to_string()
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

}
