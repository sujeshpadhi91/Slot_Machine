import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

symbol_value = {
    "A":5,
    "B":4,
    "C":3,
    "D":2
}

def check_winnings(columns,lines,bet,symbol_value):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += symbol_value[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines

def get_spin(rows,cols,symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != (len(columns) - 1):
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()
            

def deposit():
    while True:
        amount = input("Enter a valid deposit amount: $ ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                print("$",amount,"has been deposited successfully.")
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a valid number.")
    return amount

def get_number_of_lines():
   while True:
        lines = input("Enter number of lines to bet on (1 - "+str(MAX_LINES)+"): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                print("The number of lines is ",lines)
                break
            else:
                print("Lines must be within the given range.")
        else:
            print("Please enter a valid number.")
   return lines

def get_bet(balance,lines):
   while True:
        bet = input("Enter a valid bet amount for each line: $ ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= (MAX_BET/lines):
                print("$",bet,"is used for betting successfully.")
                break
            else:
                print(f"The total betting amounts to ${bet*lines} which is less than your current balance ${balance}.\nSo you can bet withing the range ${MIN_BET} and ${MAX_BET/lines}.")
        else:
            print("Please enter a valid number.")
   return bet

def spin(balance):
    lines = get_number_of_lines()
    bet = get_bet(balance,lines)
    total_bet = bet*lines
    print(f"You are betting ${bet} on {lines} lines. So the total bet = ${total_bet}")
    
    slots = get_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots,lines,bet,symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current Balance is ${balance}")
        user_input = input("Press enter to spin (q to quit).")
        if user_input == 'q':
            break
        else:
            balance += spin(balance)
    print(f"Thank you for playing. You are now left with ${balance}")

main()

            