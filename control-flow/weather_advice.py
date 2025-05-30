# ask the user about the weather condition
weather_condition = input("What's the weather condition like today? (sunny, rainy, cold): ")

# provide advice based on the weather condition
if weather_condition == "sunny":
    print("wear a t-shirt and sunglasses.")
elif weather_condition == "rainy":
    print("don't forget your umbrella and a raincoat.")
elif weather_condition == "cold":
    print("wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have advice for this weather.")