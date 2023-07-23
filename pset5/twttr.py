def main():
    word = input("Input: ")
    print(shorten(word))
    

def shorten(word):
    new_word = ""
    for letter in word:
        if letter.lower() not in ['a', 'e', 'i', 'o', 'u']:
            new_word = new_word + letter
    return new_word
if __name__ == "__main__":
    main()