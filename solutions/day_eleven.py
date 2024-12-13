from copy import deepcopy
from utils.input import read_input_file, InputFile

def day_eleven_part_1():
    inp: InputFile = read_input_file("input_files/day_eleven.txt")
    res = blink_times(25, inp.lines[0].split())
    return res

def day_eleven_part_2():
    inp: InputFile = read_input_file("input_files/day_eleven.txt")
    res = blink_times(75, inp.lines[0].split())
    return res


def blink_times(count: int, stones: list[str]) -> int:
    blink_accum = 0
    mem_cache = {}
    
    for i in range(1, count + 1):
        mem_cache[i] = {}
    
    for stone in stones:
        print(f"starting blink: {stone}")
        blink_accum += blink_recursive(stone, 0, count, mem_cache)
    
    return blink_accum


def sanitize_leading_zeroes(num: str) -> str:
    return str(int(num))


def blink_recursive(stone: str, blink_num: int, target_blinks: int, mem_cache: dict[int, dict[str, int]]) -> int:
    if blink_num == target_blinks:
        return 1
    
    remaining_blinks = target_blinks - blink_num
    if stone in mem_cache[remaining_blinks]:
        print(f"cache hit: {remaining_blinks}, {stone}")
        return mem_cache[remaining_blinks][stone]
    
    resulting: list[str] = []
    if stone == "0":
        resulting.append("1")
    elif len(stone) % 2 == 0:
        mid = len(stone) // 2
        resulting.append(sanitize_leading_zeroes(stone[:mid]))
        resulting.append(sanitize_leading_zeroes(stone[mid:]))
    else:
        computed = int(stone) * 2024
        resulting.append(str(computed))
        
    sum = 0
    for s in resulting:
        number_stones = blink_recursive(s, blink_num + 1, target_blinks, mem_cache)
        sum += number_stones
    
    mem_cache[remaining_blinks][stone] = sum
    return sum