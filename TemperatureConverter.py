def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def convert_temperature(value, from_scale, to_scale):
    from_scale = from_scale.lower()
    to_scale = to_scale.lower()

    if from_scale == "celsius":
        if to_scale == "fahrenheit":
            return celsius_to_fahrenheit(value)
        elif to_scale == "kelvin":
            return celsius_to_kelvin(value)
    elif from_scale == "fahrenheit":
        if to_scale == "celsius":
            return fahrenheit_to_celsius(value)
        elif to_scale == "kelvin":
            return fahrenheit_to_kelvin(value)
    elif from_scale == "kelvin":
        if to_scale == "celsius":
            return kelvin_to_celsius(value)
        elif to_scale == "fahrenheit":
            return kelvin_to_fahrenheit(value)
    
    return None  # If conversion is not possible

# Example usage:
value = 25  # Example temperature
from_scale = "Celsius"  # Example source scale
to_scale = "Fahrenheit"  # Example target scale

converted_value = convert_temperature(value, from_scale, to_scale)
print(f"{value} {from_scale} is {converted_value:.2f} {to_scale}")
