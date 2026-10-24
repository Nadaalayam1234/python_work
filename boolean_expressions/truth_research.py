# I predict bool("") will be False because empty string is considered False
# I predict bool("0") will be True because non-empty string even if it looks like zero
# I predict bool(0) will be False because zero number is False
# I predict bool(0.0) will be False because 0.0 is also zero
# I predict bool("False") will be True because it's a non-empty string, content doesn't matter

print(bool(""))
print(bool("0"))
print(bool(0))
print(bool(0.0))
print(bool("False"))

# Source: https://docs.python.org/3/library/stdtypes.html#truth-value-testing