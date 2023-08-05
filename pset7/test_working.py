from working import convert


def main():
    test_format()
    test_correct_time()
    
    
    
    
def test_format():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:32 PM") == "09:00 to 17:32"
    

def test_correct_time():
    assert convert("5:22 AM to 6:59 PM") == "05:22 to 18:59"
    
