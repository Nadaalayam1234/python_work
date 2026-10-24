# type_check.py
# This program checks types and does conversions.

# My predictions before running:
# 8080 -> int, because it's a whole number without quotes
# "8080" -> str, because of quotes
# 99.5 -> float, because it has a decimal point
# "198.51.100.7" -> str, IP address in quotes
# 1_000 -> int, underscore is allowed for readability

print(type(8080))
print(type("8080"))
print(type(99.5))
print(type("198.51.100.7"))
print(type(1_000))

# Conversions
converted_1 = int("443")
converted_2 = str(8080)
converted_3 = float("2.5")

print(converted_1, type(converted_1))
print(converted_2, type(converted_2))
print(converted_3, type(converted_3))