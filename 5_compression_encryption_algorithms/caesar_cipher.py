# Time complexity: O(n)
def caesar_cipher(plaintext, shift_key):
    # Caesar Cipher is a simple shift cipher that scim through entire alphabet shift_key times for plaintext letters,
    # and then you have ciphered text
    # so firstly uppercase and lowercase ascii refers where uppercase and lowercase letters start on ASCII table
    # (65 is A for example and 97 is a)
    # and amount letters is 26 because there are 26 letters in English alphabet
    # also it is all used for this one equation we use to encrypt letters for Caesar Cipher which is:
    # En(x) = (x+n) mod 26 where n is for shift key which can be between 0 and 25 (not 26 because it would simply be the
    # same as plaintext)
    # in if statement we simply calculate through this equation, depending on course whether the letter is upper or lower
    # and make some offsets within an ASCII table to actually match the letter that should transfer to
    result = ""
    upper_case_ascii = int(65)
    lower_case_ascii = int(97)
    amount_letters = int(26)

    for i in range(len(plaintext)):
        one_letter = plaintext[i]

        if one_letter.isupper():
            result += chr((ord(one_letter) + (shift_key - upper_case_ascii)) % amount_letters + upper_case_ascii)
        elif one_letter.islower():
            result += chr((ord(one_letter) + (shift_key - lower_case_ascii)) % amount_letters + lower_case_ascii)
    return result

print(caesar_cipher('Miau', 12))