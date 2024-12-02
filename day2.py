def process_file(file):
    txt = []
    with open(file, "r") as f:
        for line in f:
            txt.append(line.strip("\n").split(" "))
    return [[int(txt[i][j]) for j in range(len(txt[i]))] for i in range(len(txt))]

def is_safe(readings):
    safe = 0
    for line in readings:
        if line != sorted(line) and line != sorted(line, reverse=True):
            continue

        for x, y in zip(line[:-1], line[1:]):
            unsafe = False
            if abs(x - y) < 1 or abs(x - y) > 3:
                unsafe = True
                break
        
        if not unsafe:
            safe += 1
    return safe


if __name__ == "__main__":
    txt = process_file("day2.txt")

    print("Part 1: " + str(is_safe(txt)))
    # print("Part 2: " + str(calculate_similarity(left, right)))