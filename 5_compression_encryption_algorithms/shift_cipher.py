# this shift cipher is a little bit different from caesar cipher
# because it doesn't use a key as an amount to shift in the alphabet
# but rather amount of columns that would split desired text (meaning text - letters) to then shuffle letters
# and create from them a cipher (Warning! This cipher does not change letters to create a cipher, it actually changes
# arrangements of places of letters to 'shift' them in order to make a cipher)
# Time complexity: O(n)
def shift_cipher(plaintext, shift_key):
    result = ""
    # we use nested loops to iterate upon key amount of times and in inner loop we step key times to 'change rows'
    # in order to shuffle the letters to create a cipher, simple
    for i in range(0, shift_key):
        for j in range(i, len(plaintext), shift_key):
            one_letter = plaintext[j]
            if one_letter.isupper() or one_letter.islower():
                result += one_letter
    return result

print(shift_cipher('Miau', 3))