def caesar(text, shift, encrypt=True):
    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = -shift

    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(),
                                      shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text


def encrypt(text, shift):
    return caesar(text, shift)


def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)


# User input
text = input("Enter the text: ")
shift = int(input("Enter the shift value (1-25): "))
choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").upper()

if choice == 'E':
    result = encrypt(text, shift)
    print(f"Encrypted text: {result}")
elif choice == 'D':
    result = decrypt(text, shift)
    print(f"Decrypted text: {result}")
else:
    print("Invalid choice! Please enter 'E' or 'D'.")
