#!/usr/bin/env python

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays current date and time in 'YYYY-MM-DD HH:MM:SS' format.
    """
    current_date = datetime.now()
    print("Current Date and Time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    """
    Prompts the user for a number of days and calculates a future date.
    Arguments:
        datetime.now(): The starting datetime object from which to calculate.
    """ 

    try:
        days_to_add = int(input("Enter the number of days to add: "))
        future_date = datetime.now() + timedelta(days=days_to_add)

        print(f"Future Date:", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Invalid input. Please enter an integer for the number of days.")

def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()
