import sys


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        raise AssertionError("Exactly one argument is required: a string ")

    if not all(char.isalnum() or char.isspace() for char in args[0]):
        raise AssertionError("The string must contain only alphanums and spaces")

    decode_input(args[0])
    return 0


def decode_input(str):
    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.',
        'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-',
        'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...',
        '8': '---..', '9': '----.',
        ' ': '/'
    }

# For example, to encode the string "HELLO WORLD" in Morse code:
    text = str
    decoded_text = ' '.join(morse_code_dict[char] for char in text.upper())

# Display the encoded text in Morse code
    print(decoded_text)


if __name__ == "__main__":
    main()
