# spell_it_out.py

def main():
    word = input("Enter a word to spell out: ")

    print("\nSpelling it out:")
    # Walk through data character-by-character using a for loop
    for letter in word:
        print(letter.upper())

if __name__ == "__main__":
    main()