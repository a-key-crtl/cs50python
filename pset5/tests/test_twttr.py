from twttr import shorten


def test_word_with_no_vowels():
    assert shorten("rhythm") == "rhythm"

def test_word_with_vowels():
    assert shorten("aeiou") == ""
    assert shorten("hello") == "hll"
    
def test_uppercase_word():
    assert shorten("FEdERaTioN") == "FdRTN"
    