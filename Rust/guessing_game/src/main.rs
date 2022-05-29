use rand::Rng;

fn main() {
    println!("[+] Guess the number!");

    let secret_number = rand::thread_rng().gen_range(1..=100);

    loop {
        println!("[+] Enter your guess: ");

        let mut guess = String::new();

        std::io::stdin()
            .read_line(&mut guess)
            .expect("[-] Failed to read line");

        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };

        println!("[+] You guessed: {guess}");

        match guess.cmp(&secret_number) {
            std::cmp::Ordering::Equal => {
                println!("[+] You win!");
                break;
            }
            std::cmp::Ordering::Less => println!("[-] Too small"),
            std::cmp::Ordering::Greater => println!("[-] Too big"),
        }
    }
}

