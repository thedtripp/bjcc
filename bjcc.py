import random
import time
import sys

level_map = {
    1: {"speed": 1, "interval": 3},
    2: {"speed": 2, "interval": 5},
    3: {"speed": 3, "interval": 8},
    4: {"speed": 4, "interval": 13},
    5: {"speed": 5, "interval": 21},
    6: {"speed": 6, "interval": 21},
    7: {"speed": 7, "interval": 34},
    8: {"speed": 8, "interval": 34},
    9: {"speed": 9, "interval": 55},
    10: {"speed": 10, "interval": 55}
}

card_map = {
    1: {"value": "A", "count_delta": -1},
    2: {"value": "2", "count_delta": 1},
    3: {"value": "3", "count_delta": 1},
    4: {"value": "4", "count_delta": 1},
    5: {"value": "5", "count_delta": 1},
    6: {"value": "6", "count_delta": 1},
    7: {"value": "7", "count_delta": 0},
    8: {"value": "8", "count_delta": 0},
    9: {"value": "9", "count_delta": 0},
    10: {"value": "10", "count_delta": -1},
    11: {"value": "J", "count_delta": -1},
    12: {"value": "Q", "count_delta": -1},
    13: {"value": "K", "count_delta": -1}
}

def print_number(number):
    sys.stdout.write(f"\r > {number:>2}")
    sys.stdout.flush()

def print_countdown(number):
    for i in range(number, 0, -1):
        sys.stdout.write(f"\rGAME SART IN: {i}")
        sys.stdout.flush()
        time.sleep(1)
    print()

def main():
    print("BJCC TRAINING:")
    
    for level in range(1, 11):
        for _ in range(3):
            print(f"ROUND STARTING. LEVEL {level}.")
            time.sleep(0.5)
            print_countdown(3)
            count = 0
            for _ in range(level_map[level]["interval"]):
                number = random.randint(1, 13)
                count += card_map[number]["count_delta"]
                print_number(card_map[number]["value"])
                time.sleep(1/level_map[level]["speed"])
                print_number("")
                time.sleep(1/level_map[level]["speed"])

            print("\nWHAT IS THE COUNT???")
            user_count = input()
            try:
                if int(user_count) == count:
                    print(f"CORRECT! THE COUNT IS: {count}!\n")
                    time.sleep(0.5)
                else:
                    print(f"INCORRECT. THE COUNT IS: {count}.")
                    print("GAME OVER")
                    return
            except ValueError:
                print("Invalid input. Please enter an integer.")
                print("GAME OVER")
                return

if __name__ == "__main__":
    main()