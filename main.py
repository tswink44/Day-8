from art import logo

def caesar(direction,text,shift):
    if direction == "encode":
        cipher_text = ""
        for char in text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position + shift
                new_letter = alphabet[new_position]
                cipher_text += new_letter
            else:
                cipher_text += char
        print("The encoded text is " + cipher_text)
    elif direction == "decode":
        plain_text = ""
        for char in text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position - shift
                new_letter = alphabet[new_position]
                plain_text += new_letter
            else:
                plain_text += char
        print("The decoded text is " + plain_text)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
is_Active = True
while is_Active:
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(direction,text,shift)
    restart = input("Restart program? Type 'Yes' if so, otherwise type anything else ")
    if restart == "Yes":
        is_Active = True
    else:
        is_Active = False

