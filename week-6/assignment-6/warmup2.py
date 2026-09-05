# celsius to fahrenheit

# 1. Function definitions returning rounded values
def celsius_to_fahrenheit(c):
    return round((c * 9/5) + 32, 1)

def fahrenheit_to_celsius(f):
    return round((f - 32) * 5/9, 1)

# 2. Test values and print calls using f-strings
print(f"35°C = {celsius_to_fahrenheit(35)}°F")
print(f"10°C = {celsius_to_fahrenheit(10)}°F")
print(f"72°F = {fahrenheit_to_celsius(72)}°C")


