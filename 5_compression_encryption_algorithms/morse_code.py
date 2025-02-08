# so going to a topic of encryption and compression
# first topic is codes like Huffman's or Morse's Code presented in this file
# we have two functions similar to converting positional systems
# we have: encryption to encode our plain text message into Morse Code
# decryption - to decode our message made in Morse Code to human-readable text, in English of course
# as a starter we need to create a dictionary (in other programming languages also called: map, associative array, or
# basically object of key-value pairs)

charset_morse = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
}

# helper functions, used for inverting key with values so that morse code could be as a key to access letters and digits
def invert_key_to_value(mapping: dict):
    result = {}
    for key, value in mapping.items():
        result[value] = key
    return result

# Time complexity: O(n)
def morse_to_english(morse_txt: str):
    # so here is a decoding function, firstly we use helper function to invert a new map of morse to english symbols
    # also we add at the end of the morse text given from user a space for code to reach final symbol
    reverse_morse_map = invert_key_to_value(charset_morse)
    morse_txt += ' '

    # current char morse tracks currently to-decipher morse code symbol, i for index of course
    result = ''
    curr_char_morse = ''
    i = 0

    # main loop that the script operates upon
    # so mainly it revolves around finding spaces between Morse Code, because they indicate that this is a new word
    # so that's why there are two main if's, if letter is not a white-space, then it resets i ('i' is mainly for keeping
    # track for spaces between letters, instead of outputting 'YOUAREME' it can detect that in fact, it is 'YOU ARE ME')
    # that's why i == 2 because one space indicate simple indentation to the next letter but two spaces mean it should
    # be a space between one letter and the other one
    # and at the end it finds from current char of morse the right letter in a map and resets the current char variable
    # to keep on finding another letters
    for letter in morse_txt:
        if letter != ' ':
            i = 0
            curr_char_morse += letter
        else:
            i += 1
            if i == 2:
                result += ' '
            else:
                result += reverse_morse_map[curr_char_morse]
                curr_char_morse = ''
    return result

# Time complexity: O(n)
def english_to_morse(plain_txt: str):
    result = ""
    for char in plain_txt:
        if char == ' ':
            result += ' '
        else:
            result += charset_morse[char.upper()] + ' '
    return result

print(english_to_morse('yes'))
print(morse_to_english('-.-- . ... --.-'))
