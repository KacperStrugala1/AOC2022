with open("calories.txt", 'r')as f:

    read_file = f.read()
    largest = 0
    elves = read_file.split("\n\n")
    total = 0

    for elf in elves:
        x = elf.split()
        for x in elf.split():
            total += int(x)

        if total > largest:
            largest = total

        if x != int:
            total = 0
print(f"The largest amount of calories is {largest}")

