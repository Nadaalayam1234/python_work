# int_research.py
# Research which strings int() can convert

# Predictions (in my own words):
# int(" 22 ") will work - int() ignores spaces around the number
# int("+22") will work - plus sign is allowed
# int("0022") will work - leading zeros are allowed
# int("2_2") will work - underscore is allowed as visual separator since Python 3.6

# Source: https://docs.python.org/3/library/functions.html#int

print(int(" 22 "))
print(int("+22"))
print(int("0022"))
print(int("2_2"))