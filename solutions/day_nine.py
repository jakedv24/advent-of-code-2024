from utils.input import read_input_file, InputFile

def day_nine_part_1() -> int:
    inp: InputFile = read_input_file("input_files/day_nine.txt")
    raw = inp.raw()
    
    disk = construct_disk_from_map(raw)
    return checksum(disk)

def day_nine_part_2():
    inp: InputFile = read_input_file("input_files/day_nine.txt")
    

def checksum(disk: list):
    sum = 0
    for i, item in enumerate(disk):
        if isinstance(item, int) or item.isdigit():
           sum += i * int(item)
    
    return sum 


def construct_disk_from_map(disk_map: str) -> list[int]:
    slots = list(disk_map)
    left_ptr = 0
    right_ptr = len(slots) - 1
    right_size = int(slots[right_ptr])
    
    disk: list[int] = []
    print(slots)
    while (left_ptr < right_ptr):
        block_size = int(slots[left_ptr])
        if left_ptr % 2 == 0: # is a file slot
            for _ in range(0, block_size):
                disk.append(left_ptr // 2) # file id is based on file number
        else: # file is an empty space
            for _ in range(0, block_size):
                if right_size < 1:
                    right_ptr -= 2
                    right_size = int(slots[right_ptr])
                
                if right_ptr > left_ptr:
                    right_size -= 1
                    disk.append(right_ptr // 2)
        
        left_ptr += 1
    
    if right_ptr >= left_ptr and right_size > 0:
        for _ in range(0, right_size):
            disk.append(right_ptr // 2)
    
    return disk
