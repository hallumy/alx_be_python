#!/usr/bin/env python


# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """
    Converts Fahrenheit to Celsius using the global conversion factor.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Converts Celsius to Fahrenheit using the global conversion factor.
    """
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def prompt_and_convert_temperature():
    """
    Prompts the user for a temperature and its unit, performs conversion, and displays the result.
    """
    temperature_input = input("Enter the temperature to convert: ").strip()
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F) ").strip().lower()

    # Validate numeric input using float conversion
    try:
        temperature = float(temperature_input)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    # Conversion logic
    if unit == 'f':
        celsius = convert_to_celsius(temperature)
        print(f"{temperature}°F is {celsius:.2f}°C.")
    elif unit == 'c':
        fahrenheit = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {fahrenheit:.2f}°F.")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

def main():
    # Call the prompt function to handle user interaction and conversion
    prompt_and_convert_temperature()

if __name__ == "__main__":
    main()

