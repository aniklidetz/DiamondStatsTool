# menu.py
from enum import Enum
import os
from helper import (
    MaxDiamondPrice,
    AvgDiamondPrice,
    CountIdealCutDiamonds,
    UniqDiamondColors,
    AvgPricePerColor,
    MedianCaratPremDiamonds,
    AvgCaratPerCut
)

# Enum to define menu options
class MenuOption(Enum):
    MAX_PRICE = '1'
    AVG_PRICE = '2'
    COUNT_IDEAL = '3'
    UNIQUE_COLORS = '4'
    AVG_PRICE_PER_COLOR = '5'
    MEDIAN_CARAT_PREMIUM = '6'
    AVG_CARAT_PER_CUT = '7'
    CLEAR_SCREEN = '8'
    EXIT = '9'

# Function to clear the terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to display the menu options
def display_menu():
    print("Select an option:")
    print("1. The highest diamond price")
    print("2. The average price of a diamond")
    print("3. Number of diamonds with Ideal cut")
    print("4. Number of different colors and list of colors")
    print("5. Average price per color")
    print("6. The median carat of Premium diamonds")
    print("7. Average carat for each cut type")
    print("8. Clear screen")
    print("9. Exit")

# Function to print a divider line for better readability
def print_divider():
    print("\n" + "*" * 50 + "\n")

# Function to handle user choice and call the appropriate function
def handle_choice(choice, file_path):
    print_divider()
    
    # Handle each menu choice and call the corresponding function
    if choice == MenuOption.MAX_PRICE.value:
        max_price = MaxDiamondPrice(file_path)
        print(f"The highest diamond price: {max_price}")

    elif choice == MenuOption.AVG_PRICE.value:
        average_price = AvgDiamondPrice(file_path)
        print(f"The average price of a diamond: {average_price:.2f}")

    elif choice == MenuOption.COUNT_IDEAL.value:
        count_idel = CountIdealCutDiamonds(file_path)
        print(f"Number of diamonds with Ideal cut: {count_idel}")

    elif choice == MenuOption.UNIQUE_COLORS.value:
        num_colors, colors = UniqDiamondColors(file_path)
        print(f"Number of different colors: {num_colors}")
        print(f"Colors: {colors}")

    elif choice == MenuOption.AVG_PRICE_PER_COLOR.value:
        average_prices_color = AvgPricePerColor(file_path)
        print("Average price per color:")
        for color, price in average_prices_color.items():
            print(f"Color: {color}, Average Price: {price:.2f}")

    elif choice == MenuOption.MEDIAN_CARAT_PREMIUM.value:
        median_carat = MedianCaratPremDiamonds(file_path)
        print(f"The median carat of Premium diamonds: {median_carat}")

    elif choice == MenuOption.AVG_CARAT_PER_CUT.value:
        avg_carat_per_cut = AvgCaratPerCut(file_path)
        print("Average carat for each cut type:")
        for cut_type, carat in avg_carat_per_cut.items():
            print(f"Cut Type: {cut_type}, Average Carat: {carat:.2f}")

    elif choice == MenuOption.CLEAR_SCREEN.value:
        clear_screen()

    elif choice == MenuOption.EXIT.value:
        print("Exiting...")
        return False

    else:
        print("Invalid choice. Please try again.")
    
    print_divider()
    return True

# Main function to run the menu and handle user input
def main():
    file_path = 'diamonds.csv'
    running = True

    while running:
        display_menu()
        user_choice = input("Enter your choice: ")
        running = handle_choice(user_choice, file_path)

if __name__ == "__main__":
    main()
