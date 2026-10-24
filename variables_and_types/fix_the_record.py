# fix_the_record.py
# This program prints a short record about a network device.
# Fixed version with comments about errors

device_name = "edge-router"
# syntax error - variable name cannot start with a number
second_ip = "192.0.2.1"
# syntax error - 'class' is a reserved keyword in Python
device_class = "router"
# runtime error - int() cannot convert text "twenty-two" to number
port = 22
# runtime error - typo in variable name device_nam
print("Device:", device_name)
print("Backup IP:", second_ip)
# syntax error - fixed variable name
print("Type:", device_class)
print("Port:", port)

# Python reports syntax errors first because it checks the code structure
# before trying to run it. Runtime errors only appear after syntax is correct.