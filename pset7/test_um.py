from um import count


def main():
    test_um_in_word()
    test_um_with_punctuation()
    test_um_different_combinations()
    
    
def test_um_in_word():
    assert count("tummy") == 0
    assert count("gum dump") == 0

def test_um_with_punctuation():
    assert count("um....") == 1
    assert count("hello, um, world") == 1
    
def test_um_different_combinations():
    assert count("um tumber! hello, tummmmmer um..um!!") == 3
    assert count("            um                      1") == 1
    assert count("UM UM uM te") == 3