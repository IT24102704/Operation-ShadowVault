import base64

KEY = "NIGHTFALL"

PLAINTEXT = """ASTERIA DYNAMICS - CIPHER RELAY

FLAG: SHADOW{relay_layers_unlocked}

STAGE4_INDICATOR: archive-gw.asteria.local
"""

def vigenere_encrypt(text, key):
    result = []
    key_index = 0

    for ch in text:
        if ch.isalpha():
            shift = ord(key[key_index % len(key)].upper()) - ord('A')

            if ch.isupper():
                base = ord('A')
            else:
                base = ord('a')

            encrypted = chr((ord(ch) - base + shift) % 26 + base)
            result.append(encrypted)

            key_index += 1
        else:
            result.append(ch)

    return ''.join(result)

ciphertext = vigenere_encrypt(PLAINTEXT, KEY)

transport = base64.b64encode(ciphertext.encode()).decode()

with open("cipher_relay.txt", "w", encoding="utf-8") as f:
    f.write("ASTERIA RELAY EXPORT\n")
    f.write("TRANSPORT: BASE64\n")
    f.write("CIPHER: VIGENERE\n")
    f.write("KEY: RECOVERED FROM PREVIOUS STAGE\n\n")
    f.write(transport)

print("Done!")
print("Created: cipher_relay.txt")