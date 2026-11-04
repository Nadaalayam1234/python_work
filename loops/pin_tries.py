# pin_tries.py
MAX_TRIES = 3
CORRECT_PIN = "2580"

tries = 0
while tries < MAX_TRIES:
    pin = input("PIN: ")
    if pin == CORRECT_PIN:
        print("Access granted.")
        break
    tries += 1
    print(f"Wrong PIN. Tries left: {MAX_TRIES - tries}")
    if tries == MAX_TRIES:
        print("Card blocked.")