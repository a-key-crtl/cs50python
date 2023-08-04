from numb3rs import validate

def main():
    test_format_ip()
    test_range_ip()
    
# Test correct IP address
def test_format_ip():
    assert validate("255.2.32.12") is True
    assert validate("0.1.2.3.5") is False
    assert validate("1") is False
    assert validate("1.3") is False
    assert validate("cat") is False

# Test incorrect output
def test_range_ip():
    assert validate("200.2.102.46") is True
    assert validate("1.2.3.678") is False
    assert validate("2000.999.999.1234") is False
    assert validate("256.256.256.256") is False