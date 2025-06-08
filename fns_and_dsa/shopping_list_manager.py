#!/usr/bin/env python

def display_menu():
    """
    Display the main list options to the user.
    """
    print("Shopping List Manager")
    print("----------------------")
    print("1. Add item")
    print("2. Remove item")
    print("3. View List")
    print("4. Exit")

def add_item(shopping_list):
    """
    Prompts the user for an item and adds it to the list
    """
    item = input("Enter the item to add: ") 
    if item:
        shopping_list.append(item)
        print(f"'{item}' has been added to your shopping list.")
    else:
        print("Item name cannot be empty, please enter a value")

def remove_item(shopping_list):
    """
    Prompts the user for an input and removes it from the shopping list.
    """
    item = input("Enter the item to be removed: ")
    if item:
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"'{item}' has been removed from your shopping list.")
        else:
            print(f"'{item}' not found in your shopping list.")
    else:
        print(f"Item name caanot be empty, please enter a value")

def view_list(shopping_list):
    """
    Display all items currently in the shopping list.
    """
    if shopping_list:
        print("\n--- Your Shopping List ---")
        for index, item in enumerate(shopping_list):
            print(f"{index}. {item}")
    else:
        print("Your shopping list is empty.")

def main():
    """
    Main function to run the shopping list manager.
    """
    shopping_list = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            add_item(shopping_list)
        elif choice == '2':
            remove_item(shopping_list)
        elif choice == '3':
            view_list(shopping_list)
        elif choice == '4':
            print("Exiting Shopping List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
