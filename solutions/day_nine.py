from abc import ABC, abstractmethod
from copy import deepcopy
from itertools import chain
from utils.input import read_input_file, InputFile

def day_nine_part_1() -> int:
    inp: InputFile = read_input_file("input_files/day_nine.txt")
    raw = inp.raw()
    
    disk = construct_disk_from_map(raw)
    return checksum(disk)

def day_nine_part_2():
    inp: InputFile = read_input_file("input_files/day_nine.txt")
    return checksum(construct_disk_from_map_pt_2(inp.raw()))
    

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

class Slot:
    file_id: int
    size: int
    
    def __init__(self, file_id, size):
        self.file_id = file_id
        self.size = size
    
    def __str__(self):
        s = ""
        for _ in range(0, self.size):
            s += str(self.file_id) if self.is_file() else "."
        return s

    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, other):
        return self.file_id == other.file_id and self.size == other.size and self.is_file() == other.is_file()
    
    def __hash__(self):
        # Hash based on the x and y values
        return hash((self.file_id, self.size, self.is_file()))

    @abstractmethod
    def is_file(self) -> bool: pass

class File(Slot):
    def is_file(self): return True

class Space(Slot):
    def is_file(self): return False

def construct_disk_from_map_pt_2(disk_map: str) -> list[str]:
    slots = list(disk_map)
    files: list[File] = []
    
    disk_objs: list[Slot] = [] 
    for i, slot in enumerate(slots):
        if int(slot) == 0:
            continue
        
        if i % 2 == 0:
            f = File(file_id=(i // 2), size=int(slot))# Even index is a file
            files.append(f)
            disk_objs.append(f)
        else:  # Odd index is a space
            s = Space(file_id=(i // 2), size=int(slot))# Even index is a file
            disk_objs.append(s)
    
    # go backwards through all files
    for file in reversed(files):
        curr_index = disk_objs.index(file)
        
        # find slot up to this disk that can fit
        for slotI in range(0, curr_index):
            possible_space = disk_objs[slotI]
            if not possible_space.is_file() and possible_space.size >= file.size:
                possible_space.size -= file.size
                f = disk_objs.pop(curr_index)
                disk_objs.insert(slotI, f)
                
                # replace empty slot before with a prev file size
                if not disk_objs[curr_index].is_file():
                    disk_objs[curr_index].size += file.size
                else:
                    disk_objs.insert(curr_index + 1, Space(file_id=0, size=file.size))
                break
    
    resulting = "".join(str(item) for item in disk_objs)
    return list(resulting)

# credit: https://topaz.github.io/paste/#XQAAAQDqAQAAAAAAAAAxmwhIY/U//lM4LizwsCZHhiQtGTo9waX+C6ruax1N4ADYfrCEjk9rZmg5ArFObtBj1FbcHUZdJ0p4QPwS1Fc+sAZbfjzrtNe4X4W+GiJzgAx3YTsFi0en1x15bq6eX8Fg9COgvgLdnjltWrokM1yqg0TU4g5OCchD4wS5SGrKJtbPj3w7+twAINEtvzb/rtq3hQAW95ZLtaaaUsX0so2WK/lFJTZEjjlJt+jD9nrk4Pq4E5GudPAsncCjzTjefTP2RiNSPLZBP4PCe604A33MBZeI+Rr6ECyPsGN1I3pZOKAGsPEG2z6NLXn8esAY9sh8g4r9CDoMCRtQDLkR3z1mlLziGD1A/rM///JJpxs=
class Mem():
    def __init__(b, pos, len): b.pos = pos; b.len = len
    def val(b): return (2*b.pos + b.len-1) * b.len // 2

def disk_help():
    pos, mem = 0, []
    for len in map(int, read_input_file("input_files/day_nine.txt").raw()):
        mem += [Mem(pos, len)]
        pos += len

    for used in mem[::-2]:
        for free in mem[1::2]:
            if (free.pos <= used.pos
            and free.len >= used.len):
                used.pos  = free.pos
                free.pos += used.len
                free.len -= used.len

    print(sum(id*m.val() for id, m in enumerate(mem[::2])))