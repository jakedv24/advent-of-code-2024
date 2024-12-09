from input import read_input_file, InputFile

def day1():
    input: InputFile = read_input_file("input_files/day_one.txt")
    
    first_list: list[int] = []
    second_list: list[int] = []
    
    # split into two lists by whitespace
    for line in input.lines:
        left, right = split_line(line)
        first_list.append(left)
        second_list.append(right)
    
    # sort lists ascending
    first_list.sort()
    second_list.sort()
    
    # summate distance
    sum: int = 0
    for i, num in enumerate(first_list):
        sum += abs(num - second_list[i])
    
    return sum


def split_line(line: str) -> tuple[int, int]:
    nums: list[str] = line.split()
    
    return int(nums[0]), int(nums[1])


def day1_part2():
    input: InputFile = read_input_file("input_files/day_one.txt")
    first_list: list[int] = []
    second_list: list[int] = []
    
    # split into two lists by whitespace
    for line in input.lines:
        left, right = split_line(line)
        first_list.append(left)
        second_list.append(right)
    
    # count occurances in right list
    numToCount: dict[int, int] = {}
    for num in second_list:
        numToCount[num] = numToCount.get(num, 0) + 1
        
    
    sum: int = 0
    mem: dict[int, int] = {}
    for num in first_list:
        if num in mem:
            sum += mem[num]
        else:
            # compute
            similarity: int = num * numToCount.get(num, 0)
            mem[num] = similarity
            sum += similarity
            
    return sum


def day1_part2_no_mem():
    input: InputFile = read_input_file("input_files/day_one.txt")
    first_list: list[int] = []
    second_list: list[int] = []
    
    # split into two lists by whitespace
    for line in input.lines:
        left, right = split_line(line)
        first_list.append(left)
        second_list.append(right)
    
    # count occurances in right list
    numToCount: dict[int, int] = {}
    for num in second_list:
        numToCount[num] = numToCount.get(num, 0) + 1
    
    
    sum: int = 0
    for num in first_list:
        # compute
        similarity: int = num * numToCount.get(num, 0)
        sum += similarity
    
    return sum