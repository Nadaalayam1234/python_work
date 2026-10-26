# risk_score.py - calculates login risk
score = 0

failed = int(input("Failed attempts: "))
hour = int(input("Login hour: "))
new_device = input("New device: ")

if failed >= 3:
    score = score + 40

if hour < 6:
    score = score + 30

if new_device == "yes":
    score = score + 30

if score >= 70:
    level = "HIGH"
elif score >= 30:
    level = "MEDIUM"
else:
    level = "LOW"

print(f"Risk score: {score} ({level})")