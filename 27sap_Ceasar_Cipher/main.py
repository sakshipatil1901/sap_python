alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z']

def encryption(plain_text, shift_key):
    cipher_text = ""
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_key)%26
            cipher_text += alphabet[new_position]
        else:
            cipher_text += char
    print(f"The encoded text is {cipher_text}")

def decryption(cipher_text, shift_key):
    plain_text = ""
    for char in cipher_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position - shift_key)%26
            plain_text += alphabet[new_position]
        else:
            plain_text += char
    print(f"The decoded text is {plain_text}")

wanna_end=False
while not wanna_end:
    msg = input("Type 'encrypt' for encryption, Type 'decrypt' for decryption:\n")
    text = input("Your Message:\n").lower()
    shift = int(input("Type shift number:\n"))
    if msg == "encrypt":
        encryption(plain_text=text, shift_key=shift)
    elif msg == "decrypt":
        decryption(cipher_text=text, shift_key=shift)
    play_again=input("Type 'yes' to continue, type 'no' to exit.\n")
    if play_again=='no':
        wanna_end=True
        print("Goodbye!!")