"""
This script contains functions for temperature conversion and classification.

Functions:
  - fahr_to_celsius: Converts temperature from Fahrenheit to Celsius.
  - temp_classifier: Classifies temperature based on Celsius value.
"""

def fahr_to_celsius(temp_fahrenheit):
    """
    Converts a temperature from degrees Fahrenheit to degrees Celsius.

    Args:
        temp_fahrenheit (float): The temperature in degrees Fahrenheit.
    
    Returns:
        float: The temperature in degrees Celsius.
    """
    return (temp_fahrenheit - 32) / 1.8
    
def temp_classifier(temp_celsius):
    """
    Classifies a temperature based on its value in degrees Celsius.

    Args:
        temp_celsius (float): The temperature in degrees Celsius.

    Returns:
        int: The classification value (0, 1, 2, or 3).
    """
    if temp_celsius < -2:
        return 0
    elif (temp_celsius >= -2) and (temp_celsius < 2):
        return 1
    elif (temp_celsius >= 2) and (temp_celsius < 15):
        return 2
    else:
        return 3