# ask the user about the weather condition
weather = input("What's the weather like today? (sunny/rainy/cold): ")

# provide advice based on the weather condition
if weather == "sunny":
    print("wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")