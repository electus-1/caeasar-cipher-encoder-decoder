from art import logo
from string import ascii_lowercase

alphabet = ascii_lowercase  # we will convert the text that user enters to lowercase. so we only need lowercase letters.

# takes the text, shifts it and prints it
def ceaser(text, shift, direction):
    crypted_text = ""
    # check if the user will encode or decode
    if direction == "encode":
        for char in text:
            # if character is in alphabet then shifts it, if not then it doesn't perform any operations on it
            if char.isalpha():
                crypted_text += alphabet[(alphabet.index(char) + (shift % 26)) % 26]
            else:
                crypted_text += char
    elif direction == "decode":
        for char in text:
            if char.isalpha():
                crypted_text += alphabet[
                    (alphabet.index(char) + 26 - (shift % 26)) % 26
                ]
            else:
                crypted_text += char
    else:
        print("Please try again and be mindful of the spelling.")
    print(crypted_text)


while True:
    print(logo)  # greets the user
    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt:\n"
    )  # will the user encode or decode
    text = input(
        "Type your message:\n"
    ).lower()  # converts the text to lowercase because we don't want to meddle with uppercase letters
    shift = int(input("Type the shift number:\n"))

    ceaser(text, shift, direction)
    # if the user wants to go again then doesn't end the programme, if not then bids them farewell
    want_to_go_again = input(
        "Type 'yes' if you want to run the programme again. Otherwise type 'no'.\n"
    )
    if want_to_go_again == "no":
        print("Goodbye.")
        break
    elif want_to_go_again == "yes":
        continue
    else:
        print("Please be mindful of your typing next time.")
        break
