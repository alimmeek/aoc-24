token_buffer = []
running_total = 0
running_total_2 = 0

def process_file(file):
    global token_buffer

    tmp = []

    with open(file, "r") as f:
        for line in f:
            tmp.append(line.strip("\n").split("mul"))
    
    token_buffer = [el for line in tmp for el in line]

def process_tokens():
    global running_total

    for token in token_buffer:
        if token[0] != '(':
            continue

        tmp = token[1:].split(',')
        
        l_num = 0

        try:
            l_num = int(tmp[0])
        except Exception:
            continue

        tmp_2 = tmp[1].split(')')[0:-1]
        
        r_num = 0

        try:
            r_num = int(tmp_2[0])
        except Exception:
            continue
        
        running_total += l_num * r_num

def process_tokens_2():
    global running_total_2

    do = True

    for token in token_buffer:
        if do:
            if token[0] == '(':
                tmp = token[1:].split(',')
                
                l_num = 0

                try:
                    l_num = int(tmp[0])
                except Exception:
                    pass
                
                if len(tmp) > 1:
                    tmp_2 = tmp[1].split(')')[0:-1]
                    
                    r_num = 0

                    try:
                        r_num = int(tmp_2[0])
                    except Exception:
                        pass
                    
                    running_total_2 += l_num * r_num
        
        dont_position = token.find("don't()")
        do_position = token.find("do()")

        if dont_position > -1:
            print("Don't", token, dont_position)
        
        if do_position > -1:
            print("Do", token, do_position)

        if dont_position > -1 and do_position > -1:
            do = True if do_position > dont_position else False
        elif dont_position > -1:
            do = False
        elif do_position > -1:
            do = True


if __name__ == "__main__":
    process_file("day3.txt")

    process_tokens()

    process_tokens_2()

    print(f"Part 1: {running_total}")
    print(f"Part 2: {running_total_2}")