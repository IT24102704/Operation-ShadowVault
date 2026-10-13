import base64

KEY = "NIGHTFALL"

def vigenere_decrypt(text, key):
    result = []
    key_index = 0

    for ch in text:
        if ch.isalpha():
            shift = ord(key[key_index % len(key)].upper()) - ord('A')

            if ch.isupper():
                base = ord('A')
            else:
                base = ord('a')

            decrypted = chr((ord(ch) - base - shift) % 26 + base)
            result.append(decrypted)

            key_index += 1
        else:
            result.append(ch)

    return ''.join(result)

with open("cipher_relay.txt", "r", encoding="utf-8") as f:
    lines = f.read().splitlines()

encoded = lines[-1]

decoded = base64.b64decode(encoded).decode()

plaintext = vigenere_decrypt(decoded, KEY)

print(plaintext)