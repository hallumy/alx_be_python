#!/usr/bin/env python3

# A script that prompts user to input the weather condition

#!/usr/bin/env python

# A script that asks the user about the current weather conditions

current_weather = input("What's the weather like today? (sunny/rainy/cold):")

if current_weather == "sunny":
   print("Wear a t-shirt and sunglasses.")
elif current_weather == "rainy":
   print("Don't forget your umbrella and a raincoat.")
elif current_weather == "cold":
   print("Make sure to wear a warm coat and a scarf")
else:
   print("Sorry, I don't have recommendations for this weather.")
