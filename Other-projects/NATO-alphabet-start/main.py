import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")


phonetic_dict = {row.letter: row.code for index, row in data.iterrows()}
print(phonetic_dict)


def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        phonetic_codes = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Invalid character. Please enter only letters.")
        generate_phonetic()
    else:
        print(phonetic_codes)


generate_phonetic()