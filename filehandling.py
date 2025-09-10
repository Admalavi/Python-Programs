
# Step 1: Create first file and write data
with open("first.txt", "w") as f1:
    f1.write("Hello Akshu!\n")
    f1.write("This is the first file.\n")
    f1.write("Python file handling .\n")

# Step 2: Create second file and append data of first file
with open("first.txt", "r") as f1, open("second.txt", "a") as f2:
    data = f1.read()
    f2.write(data)

# Step 3: Read same file (second.txt) from 0 byte using seek()
with open("second.txt", "r") as f2:
    f2.seek(0)  # move to 0 byte
    print("Reading from start (0 byte):")
    print(f2.read())  

    
# Step 4: Read first 10 bytes using tell()
with open("second.txt", "r") as f2:
    f2.seek(0)
    first_10 = f2.read(10)
    print("\nFirst 10 bytes:", first_10)
    print("Current position using tell():", f2.tell())

# Step 5: Read 2 lines from current position using readline()
with open("second.txt", "r") as f2:
    f2.seek(0)  # reset position
    print("\nReading 2 lines using readline():")
    print(f2.readline(), end="")  # first line
    print(f2.readline(), end="")  # second line

# Step 6: Tail function to read last n lines
def tail(filename, n):
    with open(filename, "r") as f:
        lines = f.readlines()
        return lines[-n:]  # return last n lines

print("\n\nLast 2 lines using tail function:")
for line in tail("second.txt", 2):
    print(line, end="")
