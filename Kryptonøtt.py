alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅabcdefghijklmnopqrstuvwxyzæøå .,?-_;:+1234567890'
alphabet_length = len(alphabet)

def vigenere_encode(msg, key):
    encoded_word = ''
    key_length = len(key)

    for i, char in enumerate(msg):
        # Finds the position of the char
        msgInt = alphabet.find(char)
        '''
        Finds the position of the letter corresponding to the index in keyword.
        For example, if i = 3 and len(keyword) = 6 would give 2, leaving no rest.
        Then, alphabet.find(key[some_index]) returns a index in the alphabet.
        '''
        encInt = alphabet.find(key[i % key_length])
        if msgInt == -1 or encInt == -1:
            return ''
        #Returns the first encrypted letter
        encoded = (msgInt + encInt) % alphabet_length
        #Appends this to the final encoded word
        encoded_word += alphabet[encoded]
    return encoded_word


def vigenere_decode(coded_msg, key):
    decoded_word = ''
    key_length = len(key)

    for i, char in enumerate(coded_msg):
        # Finds the position of the char
        msgInt = alphabet.find(char)
        encInt = alphabet.find(key[i % key_length])
        if msgInt == -1 or encInt == -1:
            return ''
        #Returns the first encrypted letter
        encoded = (msgInt - encInt) % alphabet_length
        decoded_word += alphabet[encoded]
    return decoded_word

keyword = 'bil'

print(vigenere_encode("musematte", keyword))
print(vigenere_decode("5JK_B3BI7", keyword))


'''
If you want to decode the word manually, you would use the formula (x - y) % len(alphabet)
x equals the index of the first letter in the encrypted message, for example A in A65+A3K_3-D
y equals the index of the first letter in keyword, which would be 'k' in 'kake'
Finally, you would find the length of the alphabet, which in this case is 78

EXAMPLE:
In this case, the encrypted word is 5IJ_A3AH7. We take the first letter, which means 5, and find its index in the
alphabet list. We use the function print(alphabet.find("5")) which returns 71 as the index of the number 5.
Then, in order to find y we have to find the index of the first letter in b in the alphabet list. We use the function
print(alphabet.find("b")) which gives us 30. Now we can put these into the formula (71 - 30) % 78. This gives us 41,
which we use to find the letter corresponding using print(alphabet[41]). This gives us an 'm', which is the first letter
in message

We can do this for the other letters too, but we'll just do it for the following letter:
x = print(alphabet.find("6")) = 8 (5IJ_A3AH7)
y = print(alphabet.find("i")) = 37
(8 - 37) % 78 = 49
print(alphabet[49]) = u

At this point we've found 'mu', which is the first letters in message. If you want to find the whole word manually, you
can do so with this method
'''



