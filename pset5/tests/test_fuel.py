from fuel import convert, gauge

def test_fraction():
    assert convert(5/3) == "Error"
    assert convert(1/3) == 33
    
def test_gauge():
    assert gauge(100) == "F"
    assert gauge(0) == "E"
    