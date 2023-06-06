#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_dictionary = {'I': 1, 'V': 5, 'X': 10,
                        'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for index, searched in enumerate(roman_string):
        # Check if the next value is greater than the current value
        if ((index+1) == len(roman_string) or roman_dictionary[searched]
                >= roman_dictionary[roman_string[index+1]]):
            # If is true add the sum in the result variable
            result += roman_dictionary[searched]
        else:
            # If is false subtract in the result
            result -= roman_dictionary[searched]
    return result
