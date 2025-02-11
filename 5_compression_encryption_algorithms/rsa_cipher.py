from random import choice

# that's ciphering using RSA,
# whole file consists mainly three parts: generating keys (public and private), encrypting the message (using public key)
# and at the end decrypting it using on the other hand private key
# as we should know, RSA is one of the first ciphers that implemented asynchronous cryptography to encrypt its messages
# meaning that instead of using one key (like commonly used in many shift ciphers) it uses two: public (for everyone to
# safely see) and private (intended for the receiver of the encrypted message)

# generating keys function has two sub-functions, which are basically a bunch of calculations to figure out what
# keys will be generated
def generate_key():

    def nwd(a, b):
        if b > 0:
            return nwd(b, a % b)
        return a

    def inverted_modulo(a, n):
        p0, p1, a0, n0 = 0, 1, a, n
        q, r = n0 // a0, n0 % a0

        while r:
            t = p0 - q * p1
            if t >= 0:
                t = t % n
            else:
                t = n - ((-t) % n)
                p0, p1, a0, n0 = p1, t, r, a0
                q, r = n0 // a0, n0 % a0
        return  p1

    prime = [11, 13, 17, 23, 29, 31]
    p = 0
    q = 0

    while p == q:
        p, q = choice(prime), choice(prime)
        phi, n = (p - 1) * (q - 1), p * q
        e = 3
        d = inverted_modulo(e, phi)
        while nwd(e, phi) != 1:
            e += 2
            d = inverted_modulo(e, phi)

    return (e, n), (d, n)


# encrypting uses public key to cipher the plaintext with an equation: E = M^e % n where M stands for every single
# letter in the plaintext message that will be turned firstly to ASCII numbering and calculated from an equation
# pretty simple
def encrypt_rsa(plaintext: str, pub_key: tuple):
    e, n = pub_key
    encryption = [(ord(t) ** e) % n for t in plaintext]
    return encryption

# in decrypting it's basically the same equation but instead of using public key we use private one
def decrypt_rsa(cipher: list, pri_key: tuple):
    d, n = pri_key
    plain = [chr((bit ** d) % n) for bit in cipher]
    return ''.join(plain)

user_input = str(input('Enter a plaintext to cipher through RSA:\n'))
public_key, private_key = generate_key()
cipher_text = encrypt_rsa(user_input, public_key)
print(f'Encrypted using RSA: {cipher_text}')
print(f'Decrypted using RSA: {decrypt_rsa(cipher_text, private_key)}')