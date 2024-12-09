from input import InputFile, read_input_file

def test_day_2023() -> int:
    inp: InputFile = read_input_file("input_files/test_file.txt")

    sum: int = 0
    for line in inp.lines:
        cmd: int = (first_digit(line) * 10) + last_digit(line)
        sum += cmd
    
    return sum


def first_digit(line: str) -> int:
    for c in line:
        if c.isdigit():
            return int(c)
        
    return -1


def last_digit(line: str) -> int:
    for c in reversed(line):
        if c.isdigit():
            return int(c)
    
    return -1

test_day_2023()