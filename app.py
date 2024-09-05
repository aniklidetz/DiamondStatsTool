# main.py
from menu import display_menu, handle_choice

def main():
    # Path to the CSV file
    file_path = 'diamonds.csv'

    while True:
        # Display the menu to the user
        display_menu()
        
        # Get user choice
        choice = input("Enter the number of your choice: ")
        
        # Handle user choice
        if not handle_choice(choice, file_path):
            break

if __name__ == "__main__":
    main()
