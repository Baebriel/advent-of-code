use std::{fs};

fn main() {
    let filename = "input.txt";

    println!("Using: {filename}");

    let report: SweepReport = SweepReport::from_file(filename);
    let increases: u32 = SweepReport::count_depth_increases(&report);

    println!("Part 1: {increases}");

    let window_increases: u32 = SweepReport::count_window_increases(&report);

    println!("Part 2: {window_increases}");
}

struct SweepReport {
    measurements: Vec<u32>
}

impl SweepReport {
    fn from_file(filename: &str) -> SweepReport {
        let input = fs::read_to_string(&filename).expect("Unable to read text file");
    
        let measurements = input
            .lines()
            .map(|line| line.parse::<u32>().unwrap())
            .collect::<Vec<u32>>();

            SweepReport { measurements }
    }

    fn count_depth_increases(&self) -> u32 {
        let mut prev = &self.measurements[0];
        let mut count: u32 = 0;
    
        for depth in &self.measurements[1..] {
            if depth > prev {
                count += 1;
            }
            prev = depth;
        }
    
        count
    }

    fn count_window_increases(&self) -> u32 {
        let mut windows = self.measurements.windows(3);

        let first_window = windows.next();
        let mut prev_sum: u32 = first_window.unwrap().iter().sum();
        let mut count: u32 = 0;

        for window in windows {
            let sum: u32 = window.iter().sum();

            if sum > prev_sum {
                count += 1;
            }

            prev_sum = sum;
        }

        count
    }
}
