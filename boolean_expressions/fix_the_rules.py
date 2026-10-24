# fix_the_rules.py
# This program checks a connection against three rules.
role = input("Role: ")
# runtime error - input returns string, need int for comparison
port = int(input("Port: "))
# semantic error - used = instead of == for comparison
is_admin = role == "admin"
# syntax error - operator was reversed =< should be <=
is_system_port = port <= 1023
# semantic error - or needs full comparison on both sides
is_web_port = port == 80 or port == 443
print(f"Admin: {is_admin}")
print(f"System port: {is_system_port}")
print(f"Web port: {is_web_port}")