import re


def main():
    dial_numbers = []
    with open("puzzle.txt", "r") as f:
        dial_numbers = list(f.read().strip().split("\n"))
    
    part_one(dial_numbers)


def part_one(dial_numbers):
    dial_position = 50
    password_number = 0

    for dial in dial_numbers:
        parts = re.findall(r'[a-zA-Z]+|\d+', dial)
        direction = parts[0]
        number = int(parts[1])

        if direction == "L":
            dial_position = dial_position - number
        if direction == "R":
            dial_position = dial_position + number
        
        if dial_position < 0:
            dial_position = (dial_position + 100) % 100
        if dial_position >= 100:
            dial_position = (dial_position - 100) % 100
        
        if dial_position == 0:
            password_number += 1


    print(f"Password: {password_number}")


if __name__ == "__main__":
    main()
