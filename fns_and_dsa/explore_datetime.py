#!/usr/bin/env python

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays current date and time in 'YYYY-MM-DD HH:MM:SS' format.
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current Date and Time:", formatted_date)

def calculate_future_date():
    """
    Prompts the user for a number of days and calculates a future date.
    Arguments:
        datetime.now(): The starting datetime object from which to calculate.
    """ 

    try:
        number_of_days = int(input("Enter the number of days to add to the current date: "))
        future_date = datetime.now() + timedelta(days=number_of_days)

        print(f"Future Date:", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Invalid input. Please enter an integer for the number of days.")

def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()
