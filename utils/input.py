class InputFile:
    file_name: str
    lines: list[str]

    def __init__(self, file_name: str, lines: list[str]):
        self.file_name = file_name
        self.lines = lines
    
    def graph(self) -> list[list[str]]:
        return [list(s.replace("\n", "")) for s in self.lines]


def read_input_file(file_name: str) -> InputFile:
    lines: list[str] = []
    with open(file_name, 'r') as file:
        lines = file.readlines()

    if len(lines) < 1:
        raise Exception("input file has no lines read, check file name and content")

    return InputFile(file_name=file_name, lines=lines)