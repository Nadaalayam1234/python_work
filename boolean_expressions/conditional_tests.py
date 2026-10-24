user = "analyst"
role = "viewer"
failed = 3
port = 22

print("Is failed >= 3? I predict True.")
print(failed >= 3)

print("\nIs user == 'admin'? I predict False.")
print(user == "admin")

print("\nIs role != 'admin'? I predict True.")
print(role != "admin")

print("\nIs port == 22? I predict True.")
print(port == 22)

print("\nIs failed < 2? I predict False.")
print(failed < 2)

print("\nIs port > 100? I predict False.")
print(port > 100)

print("\nIs failed <= 3 and port == 22? I predict True.")
print(failed <= 3 and port == 22)

print("\nIs user == 'analyst' or role == 'admin'? I predict True.")
print(user == "analyst" or role == "admin")

print("\nIs not failed == 3? I predict False.")
print(not failed == 3)

print("\nIs role == 'viewer' and user == 'analyst'? I predict True.")
print(role == "viewer" and user == "analyst")