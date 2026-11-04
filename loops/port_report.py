# port_report.py
start = int(input("Start port: "))
end = int(input("End port: "))

for port in range(start, end + 1):
    if port <= 1023:
        print(f"{port}: system")
    elif port <= 49151:
        print(f"{port}: user")
    else:
        print(f"{port}: dynamic")

print(f"Ports checked: {end - start + 1}")