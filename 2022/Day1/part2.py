with open("2022/Day1/puzzle.txt") as f:
    elfs = f.read().split("\n\n")
    total_calories = []
    for elf in elfs:
        total_calory = 0
        for calory in elf.split("\n"):
            total_calory += int(calory)
        total_calories.append(total_calory)
    total_calories.sort()
    print(total_calories[-1] + total_calories[-2] + total_calories[-3])