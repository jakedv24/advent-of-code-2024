from solutions.day_nine import construct_disk_from_map, checksum


def test_compute_checksum():
    assert checksum(list("0099811188827773336446555566")) == 1928
    assert checksum(list("00992111777.44.333....5555.6666.....8888..")) == 2858


def test_sequence():
    assert construct_disk_from_map("12345") == [0, 2, 2, 1, 1, 1, 2, 2, 2]