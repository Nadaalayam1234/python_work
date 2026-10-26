# fix_the_policy.py - checks password policy
MIN_LENGTH = 12

username = input("Username: ")
password = input("New password: ")

# Bug 1 fix: added missing colon - syntax
if len(password) < MIN_LENGTH:
    print("- Too short.")

# Bug 2 fix: changed elif to if - semantic, we need to check both errors
if password == username:
    print("- Same as the username.")

# Bug 3 fix: wrong order, 16 should be checked first - semantic
if len(password) >= 16:
    strength = "long"
elif len(password) >= MIN_LENGTH:
    strength = "acceptable"
else:
    strength = "short"

# Bug 4 fix: fixed f-string brackets - syntax
print(f"Length: {len(password)} ({strength})")