# login_report.py - reports failed login attempts

MAX_LOGIN_ATTEMPTS = 5

username = input("Username: ")
failed = int(input("Failed attempts: "))

attempts_left = MAX_LOGIN_ATTEMPTS - failed

print("=" * 30)
print("LOGIN REPORT")
print("=" * 30)
print(f"User:\t\t{username}")
print(f"Failed:\t\t{failed}")
print(f"Attempts left:\t{attempts_left}")