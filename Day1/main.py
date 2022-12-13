with open("calories.txt", 'r')as f:

    read_file = f.read()

    elves = read_file.split("\n\n")
    total = 0
    largest = [0,0,0]
    for elf in elves:
        x = elf.split()
        for x in elf.split():
            total += int(x)

        #if total > largest:
            #largest = total
        largest = sorted(largest + [total], reverse=True)[:3]

        if x != int:
            total = 0
#print(f"The largest amount of calories is {largest}")

print(f"Sum of highest three elves: {sum(largest)}")
