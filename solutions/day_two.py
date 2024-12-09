from input import read_input_file, InputFile

def day_two_part_one() -> int :
    inp: InputFile = read_input_file("input_files/day_two.txt")
    
    sum: int = 0
    for report in inp.lines:
        if is_report_safe(report.split()):
            sum += 1
    
    return sum


def is_report_safe(levels: list[str]) -> bool:
    print(f"checking report safe: {levels}")
    
    # set all as decreasing based on first and last vals
    if int(levels[0]) < int(levels[-1]):
        levels.reverse()
    
    for i, lvl in enumerate(levels):
        if i == 0:
            continue
        
        prev, here = int(levels[i - 1]), int(lvl)
        if not step_is_valid(prev - here):
            return False
    
    return True


def step_is_valid(distance: int) -> bool:
    return 3 >= distance >= 1

def day_two_part_two():
    data = [[*map(int, l.split())] for l in open("input_files/day_two.txt")]
    for s in 0, 1: print(sum(good(d, s) or good(d[::-1], s) for d in data))


def is_report_safe_dampener(levels: list[str]) -> bool:
    # set all as decreasing based on first and last vals
    if int(levels[0]) < int(levels[-1]):
        levels.reverse()
    
    for i, lvl in enumerate(levels):
        if i == 0:
            continue
        
        prev, here = int(levels[i - 1]), int(lvl)
        if not step_is_valid(prev - here):
            # re-attempt removing this item
            # if at first element, also attempt removal of zeroth elmt
            if i == 1 and is_report_safe(remove_element(levels, 0)):
                return True
            elif is_report_safe(remove_element(levels, i)):
                return True
            
            return False
    
    return True


def remove_element(original_list: list[str], index) -> list[str]:
    if 0 <= index < len(original_list):
        return original_list[:index] + original_list[index+1:]
    else:
        raise IndexError("Index out of range")
    
def good(d, s=0):    
    for i in range(len(d)-1):
        if not 1 <= d[i]-d[i+1] <= 3:
            return s and any(good(d[j-1:j] + d[j+1:]) for j in (i,i+1))
    return True