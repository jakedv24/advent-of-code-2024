from utils.input import read_input_file, InputFile

def day_five_part_1():
    inp: InputFile = read_input_file("input_files/day_five.txt")
    ordering, commands = split_list(inp.lines, '\n')
    
    pageToInvalids: dict[int, set[int]] = {}
    for order in ordering:
        page, after = order.split("|")
        pageToInvalids.setdefault(int(page), set()).add(int(after))

    validCmds: list[list[int]] = []
    for cmd in commands:
        cmdInts: list[int] = list(map(int, cmd.split(',')))
        invalidPages: set[int] = set()
        
        valid = True
        for page in reversed(cmdInts):
            if page in invalidPages:
                valid = False
                break
            
            if page in pageToInvalids:
                invalidPages.update(pageToInvalids[page])
        
        if valid:
            validCmds.append(cmdInts)
    
    sum: int = 0
    for cmd in validCmds:
        sum += get_middle_number(cmd)
        
    print(sum)


def day_five_part_2():
    inp: InputFile = read_input_file("input_files/day_five.txt")
    ordering, commands = split_list(inp.lines, '\n')
    
    pageToInvalids: dict[int, set[int]] = {}
    for order in ordering:
        page, after = order.split("|")
        pageToInvalids.setdefault(int(page), set()).add(int(after))

    validCmds: list[list[int]] = []
    for cmd in commands:
        cmdInts: list[int] = list(map(int, cmd.split(',')))
        invalidPages: set[int] = set()

        wasInvalid = False
        corrected: list[int] = []
        for page in reversed(cmdInts):
            if page in invalidPages:
                wasInvalid = True
                
                # add bubbled down in front of issue
                for i, c in enumerate(corrected):
                    invalidSet = pageToInvalids.get(c)
                    if invalidSet != None and page in invalidSet:
                        corrected.insert(i, page)
                        break
            else:
                # add at this spot
                corrected.append(page)
            
            if page in pageToInvalids:
                invalidPages.update(pageToInvalids[page])
        
        if wasInvalid:
            validCmds.append(corrected)
        
    sum: int = 0
    for cmd in validCmds:
        sum += get_middle_number(cmd)
        
    print(sum)


def split_list(lst, element):
    if element in lst:
        index = lst.index(element)
        return lst[:index], lst[index+1:]
    else:
        return lst, []


def get_middle_number(list: list) -> int:
    return list[len(list) // 2] 