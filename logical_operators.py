temp = -4
is_sunny = False

if temp >= 28 and is_sunny:
    print("It is HOT outside 🫠")
    print("It is SUNNY ☀️")
elif temp <= 0 and is_sunny:
    print("It is COLD outside 🥶")
    print("It is SUNNY ☀️")
elif 28 > temp > 0 and is_sunny:
    print("It is WARM outside 🙂")
    print("It is SUNNY ☀️")
elif temp >= 28 and not is_sunny:
    print("It is HOT outside 🫠")
    print("It is CLOUDY 🌥️")
elif temp <= 0 and not is_sunny:
    print("It is COLD outside 🥶")
    print("It is CLOUDY 🌥️")
elif 28 > temp > 0 and not is_sunny:
    print("It is WARM outside 🙂")
    print("It is CLOUDY 🌥️")
"""
temp = 25
is_raining = True

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("tThe outdoor event is still scheduled")
"""
