import sys

for line in sys.stdin:
    line = line.strip()
    # Ignore lines starting with "#" as they are comments
    if line.startswith("#"):
        continue
    # Extract the source and target nodes from the line, and convert them to integers
    source, target = map(int, line.split("\t"))
    # Output the key-value pair with the source node as the key and the target node as the value
    print(f"{source}\t{target}")
    # Output the key-value pair with the target node as the key and the source node as the value
    print(f"{target}\t{source}")

