import sys


def main(argv):
    if len(argv) > 2:
        print("Too many arguments\n")
    if len(argv) == 1:
        chaine = input("What is the text to count ?\n")
    else:
        chaine = sys.argv[1]

    majuscules = minuscules = chiffres = ponctuation = espaces = 0
    for caractere in chaine:
        if caractere.isupper():
            majuscules += 1
        elif caractere.islower():
            minuscules += 1
        elif caractere.isdigit():
            chiffres += 1
        elif caractere.isspace():
            espaces += 1
        elif caractere in [".", ",", ";", ":", "!", "?"]:
            ponctuation += 1

    print(f"The text contains {len(chaine)} characters:")
    print(f"{majuscules} upper letters")
    print(f"{minuscules} lower letters")
    print(f"{ponctuation} punctuation marks")
    print(f"{espaces} spaces")
    print(f"{chiffres} digits")


if __name__ == '__main__':

    main(sys.argv)
