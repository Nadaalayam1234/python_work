# fix_the_functions.py

def print_header():
    """Display the report header."""
    print("=" * 30)
    print("LOGIN REPORT")
    print("=" * 30)

def lock_minutes(failed, minutes=15):
    """Return failed * minutes if failed >= 3, else 0."""
    # semantic: old code always returned 0
    if failed >= 3:
        return failed * minutes
    return 0

def login_line(username, failed):
    """Return one line of the report."""
    minutes = lock_minutes(failed)
    return f"{username}: {failed} failed, locked {minutes} min"

# runtime: print_header was called before it was defined
print_header()
# runtime: wrong keyword user, it should be username
print(login_line(username="sara", failed=4))
# semantic: print was missing, so omar line never showed
print(login_line("omar", 1))