with open("2022/Day1/puzzle.txt") as f:
    elfs = f.read().split("\n\n")
    max_calory = 0
    for elf in elfs:
        total_calory = 0
        for calory in elf.split("\n"):
            total_calory += int(calory)
        max_calory = max(total_calory, max_calory)

    print(max_calory)