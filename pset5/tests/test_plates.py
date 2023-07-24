from plates import is_valid

def test_not_two_letters():
    assert is_valid("21dx") is False
   
def test_less_two_greater_six():
    assert is_valid(" ") is False
    assert is_valid("aaaaaaa898") is False
    
def test_number_at_end():
    assert is_valid("0asds") is False
    assert is_valid("ads0er") is False
    
    
def test_period_space_punctuation():
    assert is_valid("ds!f2") is False
    assert is_valid("fgv. r3") is False
    
def test_correct():
    assert is_valid("CS50") is True