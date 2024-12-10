from solutions.day_seven import target_is_possible, Equation, day_seven_part_1, day_seven_part_2

def test_day_seven_equation():
    eq = Equation("123: 1 2 3")
    assert eq.items == [1, 2, 3]
    assert eq.target == 123
    assert eq.sum_of_items() == 6

def test_day_seven_target_possible():
    eq = Equation("190: 10 19")
    assert target_is_possible(eq) == True

    eq = Equation("3267: 81 40 27")
    assert target_is_possible(eq) == True
    
    eq = Equation("292: 11 6 16 20")
    assert target_is_possible(eq) == True
    
    eq = Equation("156: 15 6")
    assert target_is_possible(eq) == False
    
    eq = Equation("83: 17 5")
    assert target_is_possible(eq) == False


def test_day_seven_target_possible_or():
    eq = Equation("190: 10 19")
    assert target_is_possible(eq, True) == True

    eq = Equation("3267: 81 40 27")
    assert target_is_possible(eq, True) == True
    
    eq = Equation("292: 11 6 16 20")
    assert target_is_possible(eq, True) == True
    
    eq = Equation("156: 15 6")
    assert target_is_possible(eq, True) == True
    
    eq = Equation("83: 17 5")
    assert target_is_possible(eq, True) == True
    


def test_part_one():
    assert day_seven_part_1() == 5512534574980


def test_part_two():
    assert day_seven_part_2() == 328790210468594