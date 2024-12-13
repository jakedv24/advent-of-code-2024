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

class File:
    file_id: int
    size: int
    
    def __init__(self, file_id, size):
        self.file_id = file_id
        self.size = size
    
    def __str__(self):
        s = ""
        for i in range(0, self.size):
            s += str(self.file_id)
        return s

    def __repr__(self):
        return self.__str__()


def construct_disk_from_map_pt_2(disk_map: str) -> list[int]:
    slots = list(disk_map)
    files: list[File] = []
    spaces: list[int] = []
    
    # Step 1: Parse the disk_map and categorize into files and spaces
    for i, slot in enumerate(slots):
        if i % 2 == 0:  # Even index is a file
            files.append(File(file_id=(i // 2), size=int(slot)))
        else:  # Odd index is a space
            spaces.append(int(slot))
    
    # Step 2: Process files in reverse order (largest file ID first)
    resulting_files = deepcopy(files)
    for i, file in enumerate(reversed(files)):
        print(f"Checking file {file.file_id}, size {file.size}")
        
        # Step 3: Find the left-most space strictly to the left of the current file
        space_with_room = -1
        for j in range(file.file_id):  # Only check spaces strictly to the left
            if spaces[j] >= file.size:  # Space can fit the file
                space_with_room = j
                break
        
        print(f"Space found? {space_with_room}")
        
        # Step 4: If a valid space is found, move the file
        if space_with_room != -1:
            print(f"Before move spaces: {spaces}, files: {resulting_files}")
            
            # Update the space by reducing the available space
            spaces[space_with_room] -= file.size  # Reduce the space by file size
            
            # Insert a zero to simulate the "compaction"
            spaces.insert(space_with_room, 0)
            
            # Move the file to the found space position
            file_index = len(files) - i - 1  # Reverse index to access the original files
            to_move = resulting_files.pop(file_index)
            resulting_files.insert(space_with_room, to_move)
            
            print(f"Moving file {to_move.file_id} to space {space_with_room}")
            print(f"After move spaces: {spaces}, files: {resulting_files}")
    
    # Step 5: Rebuild the disk from the resulting files and spaces
    disk: list[int] = []
    for i in range(len(slots)):
        if i % 2 == 0:
            file = resulting_files[i // 2]
            for j in range(file.size):
                disk.append(file.file_id)
        else:
            for j in range(spaces[i // 2]):
                disk.append(0)
    
    print(f"Final disk: {disk}")
    return disk