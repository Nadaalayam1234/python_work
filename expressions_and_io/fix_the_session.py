# fix_the_session.py - fixed version
# RFCs not needed here

username = input("Username: ")
# runtime bug: input returns string, need int for math
total_seconds = int(input("Session length in seconds: "))

# semantic bug: / gives float (15.08), we need // for whole minutes
minutes = total_seconds // 60
seconds = total_seconds % 60

print("=" * 30)
# semantic bug: missing f before string, so {username} won't print
print(f"User: {username}")
# runtime bug: can't concatenate int + str, use f-string
print(f"Session: {minutes} min {seconds} s")
print("=" * 30)