# fix_the_stats.py
# Count failed logins and the average session length.
events = ["FAILED", "SUCCESS", "FAILED", "SUCCESS", "SUCCESS"]
minutes = [0, 30, 0, 15, 45]

# Bug 1: failed was reset to 0 inside the loop, so it never counted past 1.
# Fix: initialize the counter BEFORE the loop.
failed = 0
for event in events:
    if event == "FAILED":
        failed += 1
print(f"Failed logins: {failed}")

total = 0
count = 0
for value in minutes:
    if value > 0:
        total += value
        count += 1

# Bug 2: print was inside the loop, so it printed an average every time.
# Fix: print AFTER the loop is finished.
# Bug 3: // gives an int (30), but we need a float (30.0).
# Fix: use / instead of //.
print(f"Average session: {total / count} minutes")

# Bug 4: range(1, 4) stops at 3, so Level 4 was missing.
# Fix: range(1, 5) to include 4.
for level in range(1, 5):
    print(f"Level {level}")