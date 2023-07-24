from bank import value

def test_greet_hello():
    assert value("hello, welcome") == 0
    assert value("Hello") == 0
    
def test_greet_h():
    assert value("Hippie") == 20
    assert value("history") == 20

def test_greet_missing_h_hello():
    assert value("the Best") == 100
    assert value("Goodbye") == 100