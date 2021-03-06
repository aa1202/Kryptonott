__author__ = 'andram1202'
alphabet = "abcdefghijklmnopqrstuvwxyzæøå"

# Encodes a single letter
def encode_letter(letter, secret):
    pos = alphabet.find(letter)
    new_pos = (pos + secret)
    if new_pos >= 29:
        new_pos -= 29
    return alphabet[new_pos]


# Decodes a single letter
def decode_letter(letter, secret):
    pos = alphabet.find(letter)
    new_pos = (pos - secret)
    if new_pos < 0:
        new_pos += 29
    return alphabet[new_pos]


# Encodes a message
def encode_msg(message, secret):
    encrypted_message = ""
    for character in message:
        if character in alphabet:

            encrypted_message = encrypted_message +  encode_letter(character, secret)
        else:
            # Checks for whitespace
            encrypted_message += character

    print("Decrypted message -", encrypted_message)
    return encrypted_message

# Decodes an unknown message when the secret is known
def decode_msg(message, secret):
    decrypted_message = ""
    for character in message:
        if character in alphabet:
            decrypted_message += decode_letter(character, secret)
        else:
            # Checks for whitespace
            decrypted_message += character
    #print("Encrypted message -", decrypted_message)
    print(decrypted_message)


# Decodes an encrypted message when the secret is unknown - Therefore returns many decoded strings
def decode_unknown_msg(message, secret):
    for secret in range(secret):
        decode_msg(message, secret)
        secret -= 1

#encode_msg("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj", 2)

def string_maketrans():
    dict = str.maketrans("abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab")
    value = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"
    result = value.translate(dict)
    print(result)