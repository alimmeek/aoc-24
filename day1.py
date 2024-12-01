def process_file(file: str):
    split_list = []
    with open(file, "r") as f:
        for line in f:
            split_list.append(line.strip("\n").split("   "))
    return [int(split_list[i][0]) for i in range(len(split_list))], [int(split_list[i][1]) for i in range(len(split_list))]

def calculate_distance(left, right):
    left.sort()
    right.sort()

    distance = 0

    for l_num, r_num in zip(left, right):
        distance += abs(r_num - l_num)

    return distance

if __name__ == "__main__":
    left, right = process_file("day1.txt")

    print(calculate_distance(left, right))
    