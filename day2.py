def process_file(file):
    txt = []
    with open(file, "r") as f:
        for line in f:
            txt.append(line.strip("\n").split(" "))
    return [[int(txt[i][j]) for j in range(len(txt[i]))] for i in range(len(txt))]


def check_reading(reading):
    if reading != sorted(reading) and reading != sorted(reading, reverse=True):
        return False

    for x, y in zip(reading[:-1], reading[1:]):
        if abs(x - y) < 1 or abs(x - y) > 3:
            return False
    
    return True


def is_safe(readings):
    safe = 0
    unsafe_readings = [] # Part 2

    for line in readings:        
        if check_reading(line):
            safe += 1
        else:
            unsafe_readings.append(line)
    
    return safe, unsafe_readings


def problem_dampener(readings):
    safer = 0
    for reading in readings:
        flag = False
        for i in range(len(reading)):
            tmp = [reading[j] for j in range(len(reading)) if j != i]
            if check_reading(tmp):
                safer += 1
                flag = True
                break
    return safer



if __name__ == "__main__":
    txt = process_file("day2.txt")

    safe_readings, unsafe_readings = is_safe(txt)
    print("Part 1: " + str(safe_readings))
    print("Part 2: " + str(safe_readings + problem_dampener(unsafe_readings)))